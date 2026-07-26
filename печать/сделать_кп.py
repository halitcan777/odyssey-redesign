# -*- coding: utf-8 -*-
"""Генератор фирменных КП «Одиссей» (А4, печать): единый шаблон + 3 наполнения.
Дизайн – фирстиль 2.0: крем/бордо/золото, Oswald+Inter, бенто с 1px линиями."""
import os, subprocess

ROOT = os.path.dirname(os.path.abspath(__file__))
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

CSS = """
@page{size:A4;margin:0}
*{margin:0;padding:0;box-sizing:border-box;border-radius:0}
:root{--bg:#FDFBF7;--cell:#FFFFFF;--line:#E4D9C4;--ink:#1F1A17;--muted:#79695A;--red:#93221B;--gold:#C9A227}
body{font-family:'Inter',sans-serif;color:var(--ink);background:#fff;font-size:10.5pt;line-height:1.55}
.page{width:210mm;height:296mm;background:var(--bg);padding:14mm 16mm 12mm;display:flex;flex-direction:column;page-break-after:always;position:relative;overflow:hidden}
h1,h2,h3,.disp{font-family:'Oswald',sans-serif;text-transform:uppercase;font-weight:700}
/* шапка */
.head{display:flex;align-items:center;gap:6mm;border-bottom:1px solid var(--line);padding-bottom:6mm}
.head img{width:16mm}
.head .nm{font-family:'Oswald',sans-serif;font-weight:700;font-size:20pt;letter-spacing:.08em;line-height:1}
.head .nm small{display:block;font-family:'Inter',sans-serif;font-weight:600;font-size:7pt;letter-spacing:.22em;color:var(--gold);margin-top:1.5mm}
.head .cnt{margin-left:auto;text-align:right;font-size:8.5pt;color:var(--muted);line-height:1.6}
.head .cnt b{color:var(--ink);font-size:10.5pt}
/* титул */
.kicker{font-size:8pt;font-weight:600;letter-spacing:.24em;text-transform:uppercase;color:var(--red);display:flex;align-items:center;gap:3mm;margin:8mm 0 2mm}
.kicker::before{content:"";width:8mm;height:2px;background:var(--red)}
.title{font-size:26pt;line-height:1.02;margin-bottom:3mm}
.lead{color:var(--muted);font-size:10pt;max-width:150mm}
/* бенто */
.bento{display:grid;gap:1px;background:var(--line);border:1px solid var(--line);margin-top:6mm}
.g2{grid-template-columns:1fr 1fr}.g3{grid-template-columns:1fr 1fr 1fr}.g4{grid-template-columns:repeat(4,1fr)}
.cell{background:var(--cell);padding:5mm 6mm}
.cell .nm{font-family:'Oswald',sans-serif;font-weight:600;text-transform:uppercase;font-size:10pt;letter-spacing:.04em;margin-bottom:1.5mm}
.cell .pr{font-family:'Oswald',sans-serif;font-weight:700;font-size:17pt;color:var(--red)}
.cell .pr small{font-family:'Inter',sans-serif;font-weight:400;font-size:8pt;color:var(--muted)}
.cell p{font-size:8.5pt;color:var(--muted);margin-top:1.5mm}
.cell.hd{background:var(--ink);color:#fff;font-family:'Oswald',sans-serif;text-transform:uppercase;font-size:9pt;letter-spacing:.14em;padding:4mm 6mm}
/* строки-прайс */
.row{display:flex;justify-content:space-between;gap:6mm;align-items:baseline}
.row .cost{font-family:'Oswald',sans-serif;font-weight:700;font-size:13pt;white-space:nowrap;color:var(--red)}
/* список */
.list{list-style:none;margin-top:2mm}
.list li{padding-left:5mm;position:relative;font-size:9.5pt;margin-bottom:1.8mm}
.list li::before{content:"";position:absolute;left:0;top:1.6mm;width:2.2mm;height:2.2mm;background:var(--red)}
.list.gold li::before{background:var(--gold)}
/* статы */
.stat b{font-family:'Oswald',sans-serif;font-weight:700;font-size:20pt;display:block;line-height:1;color:var(--red)}
.stat span{font-size:8pt;color:var(--muted)}
/* камуфляж-акцент */
.camo{position:absolute;top:0;right:0;opacity:.9}
/* футер */
.foot{margin-top:auto;border-top:1px solid var(--line);padding-top:4mm;display:flex;justify-content:space-between;gap:8mm;font-size:8pt;color:var(--muted)}
.foot b{color:var(--ink)}
.foot .mgr{text-align:right}
.mark{position:absolute;bottom:12mm;right:16mm;opacity:.06;width:60mm}
"""

CAMO = """<svg class="camo" width="140" height="90" viewBox="0 0 140 90"><g fill="#93221B"><rect x="40" y="0" width="25" height="25"/><rect x="65" y="12" width="25" height="25"/><rect x="115" y="0" width="25" height="25"/><rect x="90" y="37" width="25" height="25"/><rect x="115" y="62" width="25" height="25"/></g><g fill="#C9A227" opacity=".85"><rect x="15" y="12" width="25" height="25"/><rect x="115" y="25" width="25" height="25"/></g></svg>"""


def head():
    return f"""<div class="head">
  <img src="../лого/одиссей-щит.png" alt="">
  <div class="nm">Одиссей<small>ГРУППА ПРЕДПРИЯТИЙ</small></div>
  <div class="cnt"><b>+7 (342) 20-66-911</b><br>odyssey.security@mail.ru<br>Пермь, ул. Стахановская, 54</div>
</div>"""


def foot(org, extra, mgr="Мансуров Самат Асхатович", tel="+7 950 47-90-454"):
    return f"""<div class="foot">
  <div><b>{org}</b><br>{extra}</div>
  <div class="mgr"><b>Менеджер по работе с клиентами</b><br>{mgr} · <b>{tel}</b></div>
</div>
<img class="mark" src="../лого/одиссей-щит.png" alt="">"""


def page(title, kicker, lead, body, foot_html):
    return f"""<div class="page">{CAMO}{head()}
<div class="kicker">{kicker}</div>
<div class="title">{title}</div>
<p class="lead">{lead}</p>
{body}
{foot_html}</div>"""


FIZ = page(
    "Физическая охрана объектов", "Коммерческое предложение · ООО ЧОП «Одиссей-СБ»",
    "Постовая охрана любой категории сложности: офисы, магазины, стройплощадки, производственные территории, коттеджи. Лицензия Росгвардии ЧО № 056449.",
    """<div class="bento g4">
  <div class="cell stat"><b>2006</b><span>работаем с этого года</span></div>
  <div class="cell stat"><b>500+</b><span>сотрудников в штате</span></div>
  <div class="cell stat"><b>120+</b><span>постов охраны</span></div>
  <div class="cell stat"><b>5</b><span>экипажей ГБР</span></div>
</div>
<div class="bento g2">
  <div class="cell">
    <div class="nm">Услуги</div>
    <ul class="list">
      <li>Физическая охрана объектов любой сложности</li>
      <li>Пультовая охрана с выездом ГБР</li>
      <li>Инкассация и сопровождение грузов</li>
      <li>Консьержи, вахтёры, сторожа</li>
      <li>Телохранители, охрана VIP-персон</li>
    </ul>
  </div>
  <div class="cell">
    <div class="nm">Каждый сотрудник проходит</div>
    <ul class="list gold">
      <li>Психологическое тестирование при отборе</li>
      <li>Проверку на причастность к правонарушениям</li>
      <li>Подготовку и экзамены в собственном УЦ «Одиссей»</li>
      <li>Обязательную стажировку на объекте</li>
    </ul>
  </div>
</div>
<div class="bento">
  <div class="cell row"><div><div class="nm">Стоимость поста охраны</div><p>итоговая ставка зависит от сложности объекта и режима несения службы</p></div><div class="cost">от 80 ₽/час</div></div>
</div>
<div class="bento">
  <div class="cell"><div class="nm">Нам доверяют</div><p style="font-size:9pt;color:var(--ink)">МУП «Пермгорэлектротранс» · автосалоны «УралАвтоИмпорт» · стройплощадки «ПИК-Кама» · ТД «Лист» · ТСЖ центральных районов Перми · ОАО «Мотовилихинские заводы» · СК «Рекон»</p></div>
</div>""",
    foot("ООО ЧОП «Одиссей-СБ»", "Лицензия ЧО № 056449 · ОГРН 1115905002223 · ИНН 5905284767<br>614066, Пермь, ул. Стахановская, 54, литер Л · дежурная часть 24/7: <span style='white-space:nowrap'>+7 (342) 21-41-911</span>"),
)

TEH = page(
    "Техническая охрана и сигнализация", "Коммерческое предложение · пультовая охрана",
    "Охрана объектов средствами технической сигнализации с круглосуточным мониторингом и выездом групп быстрого реагирования. ГБР работают по Перми, Кукуштану, Платошино и Новобродовскому.",
    """<div class="bento">
  <div class="cell hd">Абонентская плата · техническое обслуживание включено</div>
  <div class="cell row"><div><div class="nm">ОС + ПС + тревожная кнопка</div><p>охранная, пожарная сигнализация и КТС – полный комплекс</p></div><div class="cost">от 1 500 ₽/мес</div></div>
  <div class="cell row"><div><div class="nm">Охранная сигнализация (ОС)</div><p>датчики проникновения с выводом на пульт</p></div><div class="cost">от 1 200 ₽/мес</div></div>
  <div class="cell row"><div><div class="nm">Кнопка тревожной сигнализации (КТС)</div><p>выезд ГБР по нажатию</p></div><div class="cost">от 1 000 ₽/мес</div></div>
</div>
<div class="bento g2">
  <div class="cell"><div class="nm">Монтаж и обслуживание</div><ul class="list"><li>Проектирование и монтаж ОС, ПС, КТС</li><li>Системы контроля и учёта доступа</li><li>Видеонаблюдение</li></ul></div>
  <div class="cell"><div class="nm">Почему «Одиссей»</div><ul class="list gold"><li>С 2006 года на рынке Пермского края</li><li>500+ объектов под охраной, 120+ постов</li><li>Собственный учебный центр и тир</li><li>Среди клиентов – «Мотовилихинские заводы», ГК «ПИК», СК «Рекон»</li></ul></div>
</div>
<div class="bento g3">
  <div class="cell"><div class="nm">Детекция лжи</div><p>проверки при приёме, хищениях, сделках – конфиденциально</p></div>
  <div class="cell"><div class="nm">Физическая охрана</div><p>посты, сопровождение грузов по всей России, VIP</p></div>
  <div class="cell"><div class="nm">Стрелковый тир</div><p>боевой, интерактивный, арбалетный; корпоративный досуг</p></div>
</div>""",
    foot("ООО ЧОП «Одиссей-СБ»", "Лицензия ЧО № 056449 · ОГРН 1115905002223 · ИНН 5905284767<br>614066, Пермь, ул. Стахановская, 54, литер Л · дежурная часть 24/7: <span style='white-space:nowrap'>+7 (342) 21-41-911</span>"),
)

TIR = page(
    "Корпоративный абонемент в боевой тир", "Коммерческое предложение · ССК «Одиссей»",
    "Первый закрытый частный стрелковый клуб Перми (с 2011 года). Стрелковая галерея 30 метров, боевое оружие, инструкторы, экспозиции оружия и военной техники.",
    """<div class="bento">
  <div class="cell row"><div><div class="nm">Абонемент для организации</div><p>всё включено, посещение по звонку ежедневно 10:00–19:00</p></div><div class="cost">50 000 ₽/мес</div></div>
</div>
<div class="bento g2">
  <div class="cell"><div class="nm">В абонемент входит</div>
    <ul class="list">
      <li>Неограниченное количество сотрудников</li>
      <li>Неограниченное число посещений</li>
      <li>Стрельбы из боевого оружия – 1 500 патронов в месяц</li>
      <li>Интерактивный тир</li>
      <li>Зал спортивной подготовки</li>
    </ul>
  </div>
  <div class="cell"><div class="nm">Дополнительно</div>
    <ul class="list gold">
      <li>Пневматическое оружие – 250 ₽/час</li>
      <li>Метание ножей – 250 ₽/час</li>
      <li>Корпоративные соревнования по стрельбе</li>
      <li>Семейный и детский отдых, экскурсии</li>
      <li>Выставочные стенды: 26 единиц легендарного оружия</li>
    </ul>
  </div>
</div>
<div class="bento g3">
  <div class="cell stat"><b>30 м</b><span>стрелковая галерея</span></div>
  <div class="cell stat"><b>26</b><span>единиц боевого оружия</span></div>
  <div class="cell stat"><b>11</b><span>единиц военной техники в музее</span></div>
</div>""",
    foot("ПРСОО «Спортивно-стрелковый клуб «Одиссей»", "614066, Пермь, ул. Стахановская, 54, литер П<br>тир: +7 (342) 20-66-161 (Ср–Вс 12:00–20:00) · odissey_uc@mail.ru · одиссейпермь.рф",
         mgr="Администратор клуба", tel="+7 (342) 20-66-161"),
)

HTML_HEAD = """<!DOCTYPE html><html lang="ru"><head><meta charset="UTF-8">
<link rel="stylesheet" href="../fonts/fonts.css"><style>{css}</style></head><body>"""

for name, content in [("КП_физическая_охрана", FIZ), ("КП_техническая_охрана", TEH), ("КП_тир_корпоративный", TIR)]:
    html_path = os.path.join(ROOT, f"_{name}.html")
    open(html_path, "w", encoding="utf-8").write(HTML_HEAD.format(css=CSS) + content + "</body></html>")
    pdf_path = os.path.join(ROOT, f"{name}.pdf")
    subprocess.run([CHROME, "--headless", "--disable-gpu", f"--print-to-pdf={pdf_path}",
                    "--no-pdf-header-footer", "--print-to-pdf-no-header", f"file://{html_path}"],
                   capture_output=True)
    print("✓", name, os.path.getsize(pdf_path) // 1024, "КБ")
