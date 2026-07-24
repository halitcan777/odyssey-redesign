# -*- coding: utf-8 -*-
"""Прогон текстовых нод HTML-файлов через Типограф Лебедева (SOAP).
Использование: python3 typograf.py tir.html muzey.html ...
Вычищает <nobr>, которые Типограф вставляет в телефоны."""
import re, sys, html as H, urllib.request

ENDPOINT = "http://typograf.artlebedev.ru/webservices/typograf.asmx"
DELIM = "\n@@%@@\n"


def collect_nodes(src):
    body = src[src.find("</head>"):]
    nodes = set()
    for m in re.finditer(r">([^<>]+)<", body):
        t = m.group(1)
        if len(t.strip()) >= 4 and re.search(r"[а-яА-ЯёЁ]", t) and not re.fullmatch(r"[\s\d+()–\-—/₽%.,:«»·]+", t):
            nodes.add(t)
    return sorted(nodes)


def typograf(nodes):
    batch = DELIM.join(nodes)
    envelope = f"""<?xml version="1.0" encoding="UTF-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <ProcessText xmlns="http://typograf.artlebedev.ru/webservices/">
      <text>{H.escape(batch)}</text>
      <entityType>3</entityType>
      <useBr>0</useBr>
      <useP>0</useP>
      <maxNobr>0</maxNobr>
    </ProcessText>
  </soap:Body>
</soap:Envelope>"""
    req = urllib.request.Request(ENDPOINT, data=envelope.encode("utf-8"),
        headers={"Content-Type": "text/xml; charset=utf-8",
                 "SOAPAction": '"http://typograf.artlebedev.ru/webservices/ProcessText"'})
    resp = urllib.request.urlopen(req, timeout=40).read().decode("utf-8")
    result = re.search(r"<ProcessTextResult>(.*?)</ProcessTextResult>", resp, re.S).group(1)
    result = H.unescape(result)
    result = re.sub(r"<nobr[^>]*>(.*?)</nobr>", r"\1", result)
    fixed = re.split(r"\s*@@%@@\s*", result.strip("\n"))
    assert len(fixed) == len(nodes), f"разъехались ноды: {len(nodes)} → {len(fixed)}"
    return fixed


def process(path):
    src = open(path, encoding="utf-8").read()
    nodes = collect_nodes(src)
    if not nodes:
        print(f"{path}: нечего типографить")
        return
    fixed = typograf(nodes)
    changed = 0
    for old, new in zip(nodes, fixed):
        new = new.strip("\n")
        if old.strip() == new.strip():
            continue
        lead = old[:len(old) - len(old.lstrip())]
        trail = old[len(old.rstrip()):]
        src = src.replace(">" + old + "<", ">" + lead + new.strip() + trail + "<")
        changed += 1
    open(path, "w", encoding="utf-8").write(src)
    print(f"{path}: нод {len(nodes)}, изменено {changed}")


if __name__ == "__main__":
    for f in sys.argv[1:]:
        process(f)
