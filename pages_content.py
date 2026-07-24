# -*- coding: utf-8 -*-
"""Контент внутренних страниц. Каждый билдер получает shell/page_hero/data из build_pages."""
import html as H
import json, os, re

ROOT = os.path.dirname(os.path.abspath(__file__))
PHOTO_MAP_FILE = os.path.join(ROOT, "фото", "карта_фото.json")


def photo_for(path):
    """Локальное фото для страницы старого сайта (кладёт задача подготовки фото)."""
    if os.path.exists(PHOTO_MAP_FILE):
        m = json.load(open(PHOTO_MAP_FILE, encoding="utf-8"))
        return m.get(path)
    return None


def esc(s):
    return H.escape(s, quote=False)


def snippet(text, maxlen=220):
    """Первые предложения текста, обрезка по границе предложения."""
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) <= maxlen:
        return text
    cut = text[:maxlen]
    dot = max(cut.rfind(". "), cut.rfind("! "), cut.rfind("? "))
    return cut[:dot + 1] if dot > 60 else cut.rsplit(" ", 1)[0] + "…"


def wcard(num, title, text, img, meta=""):
    shot = (f'<div class="shot"><img src="{img}" alt="{esc(title)}" loading="lazy"></div>' if img
            else '<div class="shot ph" style="min-height:0"><span>Нужен материал:<br>фото</span></div>')
    meta_html = f'<div class="meta">{esc(meta)}</div>' if meta else ""
    return f"""<div class="cell wcard">
  {shot}
  <div class="body"><span class="num">{num:02d} /</span><h3>{esc(title)}</h3><p>{esc(text)}</p>{meta_html}</div>
</div>"""


def sec_head(kicker, h2, p=""):
    p_html = f"<p>{esc(p)}</p>" if p else ""
    return f"""<div class="bento rv">
    <div class="cell cell--big cell--static sec-cell">
      <span class="kicker">{esc(kicker)}</span>
      <h2>{esc(h2)}</h2>
      {p_html}
    </div>
  </div>"""


def clean_title(t):
    return re.sub(r"\s*[»|].*$", "", t).strip()


def cta_cell(title, text, btn):
    """Ячейка-CTA, закрывающая пустой хвост бенто-сетки."""
    return f"""<div class="cell cell-flex cell--static" style="background:var(--red)">
  <h3 style="margin-bottom:12px;color:#fff">{esc(title)}</h3>
  <p style="font-size:13px;color:rgba(255,255,255,.85)">{esc(text)}</p>
  <div class="bottom"><a class="btn" style="border:1px solid #fff;color:#fff" href="index.html#kontakty">{esc(btn)}</a></div>
</div>"""


# ────────────────────────── ТИР ──────────────────────────

def build_tir(shell, page_hero, data):
    weapons = data("оружие")
    cards = "\n".join(
        wcard(i + 1, clean_title(w["title"]), snippet(w["text"], 170), photo_for(w["path"]))
        for i, w in enumerate(weapons)
    )
    hero = page_hero(
        "ССК «Одиссей» · первый закрытый клуб Перми · с 2011 года",
        "Боевой стрелковый тир",
        "Стрельба из боевого оружия под руководством инструкторов, метание ножей, экспозиции оружия и техники времён Великой Отечественной. Работаем по курсам стрельб КС МВД РФ.",
        '<div class="cta-row"><a class="btn btn-red" href="index.html#kontakty">Записаться</a><a class="btn btn-line" href="#arsenal">Смотреть арсенал</a></div>',
    )
    return shell(file="tir.html", title="Боевой стрелковый тир «Одиссей» — Пермь",
                 desc="Первый закрытый частный стрелковый клуб Перми: 30-метровая галерея, 26 единиц боевого оружия, метание ножей, подарочные карты.",
                 content=f"""{hero}

<section class="wrap canvas">
  <div class="bento g-4 rv">
    <div class="cell cell--compact stat"><b><span data-count="30">30</span><i> м</i></b><span>стрелковая галерея</span></div>
    <div class="cell cell--compact stat"><b data-count="26">26</b><span>единиц оружия: от ПМ до пулемёта Максим</span></div>
    <div class="cell cell--compact stat"><b data-count="2011">2011</b><span>год основания клуба</span></div>
    <div class="cell cell--compact stat"><b>Ср–Вс</b><span>12:00–20:00 · +7 (342) 20-66-161</span></div>
  </div>
  <div class="bento g-3 bento--seamtop rv">
    <div class="cell cell-flex pr-cell">
      <div class="nm">Стрельба из пистолета</div>
      <div class="pr">2 680 ₽</div>
      <p>занятие с инструктором; патроны считаются отдельно — пистолетный от 150 ₽</p>
    </div>
    <div class="cell cell-flex pr-cell">
      <div class="nm">Винтовка / автомат</div>
      <div class="pr">3 680 ₽</div>
      <p>длинноствольное оружие, стрелковая галерея 30 метров</p>
    </div>
    <div class="cell cell-flex pr-cell">
      <div class="nm">Метание ножей</div>
      <div class="pr">1 000 ₽</div>
      <p>30 минут, отдельные рабочие места</p>
    </div>
  </div>
</section>

<section class="wrap canvas" style="margin-top:96px">
  {sec_head("Подарочные карты", "Подарить стрельбу", "Три курса под уровень: от первого знакомства с оружием до уверенного владения.")}
  <div class="bento g-3 bento--seamtop rv">
    <div class="cell cell-flex pr-cell">
      <div class="nm">«Базовый»</div>
      <div class="pr">5 680 ₽</div>
      <p>знакомство с оружием, инструктаж, стрельба из пистолета под контролем инструктора</p>
    </div>
    <div class="cell cell-flex pr-cell">
      <div class="nm">«Универсальный стрелок»</div>
      <div class="pr">7 880 ₽</div>
      <p>пистолет и длинноствольное оружие, больше выстрелов и упражнений</p>
    </div>
    <div class="cell cell-flex pr-cell">
      <div class="nm">«Профессионал»</div>
      <div class="pr">11 000 ₽</div>
      <p>полный курс: тактика, скоростная стрельба, работа из разных положений</p>
    </div>
  </div>
</section>

<section class="wrap canvas" id="arsenal" style="margin-top:96px">
  {sec_head("Арсенал клуба", "26 единиц оружия", "Каждая единица — легенда: от пистолета Макарова до пулемёта Максим. Всё оружие боевое, стрельба только с инструктором.")}
  <div class="bento g-4 bento--seamtop rv">
    {cards}
  </div>
</section>

<section class="wrap canvas" style="margin-top:96px">
  <div class="bento g-3 rv">
    <div class="cell cell-flex">
      <span class="kicker">Правила</span>
      <h3 style="margin:8px 0 12px">Поведение в тире</h3>
      <p style="font-size:13px;color:var(--muted)">Оружие всегда направлено в сторону мишеней, работа строго по командам инструктора, наушники и очки обязательны. Полные правила — при инструктаже.</p>
    </div>
    <div class="cell cell-flex">
      <span class="kicker">Сервис</span>
      <h3 style="margin:8px 0 12px">Ремонт оружия</h3>
      <p style="font-size:13px;color:var(--muted)">Мастерская клуба: диагностика, чистка, ремонт и обслуживание гражданского и служебного оружия.</p>
    </div>
    <div class="cell cell-flex">
      <span class="kicker">Экскурсии</span>
      <h3 style="margin:8px 0 12px">Музей и полигон</h3>
      <p style="font-size:13px;color:var(--muted)">Экспозиции оружия и военной техники, выезды на полигон, программы для школ — бесплатно.</p>
      <div class="bottom"><a class="btn btn-line" href="muzey.html">В музей</a></div>
    </div>
  </div>
</section>""")


# ────────────────────────── МУЗЕЙ ──────────────────────────

def build_muzey(shell, page_hero, data):
    tech = data("техника")
    cards = "\n".join(
        wcard(i + 1, clean_title(t["title"]), snippet(t["text"], 200), photo_for(t["path"]),
              meta=_year_of(t["title"]))
        for i, t in enumerate(tech)
    )
    cards += cta_cell("Хотите увидеть вживую?", "Экскурсии для школ и организаций — бесплатно. Техника на ходу.", "Записаться на экскурсию")
    hero = page_hero(
        "Изюминка группы · техника на ходу",
        "Музей военной техники",
        "Одиннадцать единиц: от бронеавтомобиля БА-64 образца 1943 года до БРДМ-2. Техника участвует в парадах, выставках и экскурсиях — и заводится.",
        '<div class="cta-row"><a class="btn btn-red" href="index.html#kontakty">Записаться на экскурсию</a></div>',
    )
    return shell(file="muzey.html", title="Музей военной техники «Одиссей» — Пермь",
                 desc="11 единиц военной техники на ходу: БРДМ-2, ГАЗ-67, миномёт ПМ-38, пулемёт Максим. Экскурсии для школ бесплатно.",
                 content=f"""{hero}

<section class="wrap canvas">
  <div class="bento g-3 rv">
    {cards}
  </div>
</section>""")


def _year_of(title):
    m = re.search(r"(19\d\d)", title)
    return f"образца {m.group(1)} года" if m else ""


# ────────────────────────── УЧЕБНЫЙ ЦЕНТР ──────────────────────────

def build_uc(shell, page_hero, data):
    progs = data("уц")
    cells = []
    for i, p in enumerate(progs):
        prices = _prices_of(p["text"])
        price_html = f'<div class="meta" style="color:var(--ink)">{esc(prices)}</div>' if prices else ""
        cells.append(f"""<div class="cell cell-flex">
  <span class="num">{i + 1:02d} /</span>
  <h3 style="margin:8px 0 12px">{esc(clean_title(p["title"]))}</h3>
  <p style="font-size:13px;color:var(--muted)">{esc(snippet(p["text"], 260))}</p>
  <div class="bottom">{price_html}</div>
</div>""")
    hero = page_hero(
        "ЧУ ДПО «УЦ Одиссей» · лицензия № 6801",
        "Учебный центр",
        "Подготовка и повышение квалификации частных охранников 4–6 разрядов, курсы по оружию для граждан, подготовка руководителей ЧОП. Свой тир для практики, экзамены на месте.",
        '<div class="cta-row"><a class="btn btn-red" href="index.html#kontakty">Записаться</a><a class="btn btn-line" href="tel:+73422061911">+7 (342) 20-61-911</a></div>',
    )
    return shell(file="uc.html", title="Учебный центр «Одиссей» — подготовка охранников в Перми",
                 desc="Профподготовка и повышение квалификации охранников 4–6 разрядов, периодические проверки, курсы по оружию. Лицензия № 6801.",
                 content=f"""{hero}

<section class="wrap canvas">
  {sec_head("Программы", "Восемь программ обучения", "Периодическую проверку принимают сотрудники Росгвардии. Курсы по оружию можно пройти в выходные.")}
  <div class="bento g-4 bento--seamtop rv">
    {"".join(cells)}
  </div>
  <div class="bento bento--seamtop rv">
    <div class="cell cell--compact cell--static">
      <div class="gold-note">Лицензия № 6801 от 14.07.2020, Министерство образования и науки Пермского края · учебные планы и отчётность — по запросу в центре</div>
    </div>
  </div>
</section>""")


def _prices_of(text):
    rows = re.findall(r"([4-6] разряд)\s*[-—]\s*([\d\s]{3,6})руб", text)
    if rows:
        return " · ".join(f"{r} {p.strip()} ₽" for r, p in rows[:3])
    m = re.search(r"Стоимость[^\d]{0,30}([\d\s]{3,7})руб", text)
    return f"{m.group(1).strip()} ₽" if m else ""


# ────────────────────────── ОХРАНА ──────────────────────────

PULT_PRICE = [
    ("Кнопка тревожной сигнализации (КТС)", "1 500 ₽/мес"),
    ("Охранная сигнализация (ОС)", "1 500 ₽/мес"),
    ("Пожарная + тревожная (ПС+КТС)", "2 000 ₽/мес"),
    ("Комбинированный комплекс (ОС+ПС+КТС)", "2 500 ₽/мес"),
    ("Квартиры", "500 ₽/мес"),
    ("Коттеджи", "1 500 ₽/мес"),
    ("Гаражи", "500 ₽/мес"),
    ("SMS-информирование", "100 ₽/мес"),
]


def build_ohrana(shell, page_hero, data):
    services = data("охрана")
    order = ["fizicheskaja", "pultovaja", "telohranitel", "meroprijatij"]
    services.sort(key=lambda s: next((i for i, k in enumerate(order) if k in s["path"]), 9))
    svc_cells = []
    for i, s in enumerate(services):
        img = photo_for(s["path"])
        svc_cells.append(f"""<div class="cell cell--big cell--static">
  <span class="num">{i + 1:02d} /</span>
  <h3 style="margin:8px 0 12px">{esc(clean_title(s["title"]))}</h3>
  <div class="prose"><p>{esc(snippet(s["text"], 420))}</p></div>
</div>""")
    price_rows = "\n".join(
        f'<div class="cell cell--compact trow trow--2"><div class="prog">{esc(n)}</div><div class="cost">{esc(p)}</div></div>'
        for n, p in PULT_PRICE
    )
    hero = page_hero(
        "ООО ЧОП «Одиссей-СБ» · лицензия Росгвардии",
        "Охранное предприятие",
        "Кадровая основа — бывшие сотрудники силовых структур. Дежурная часть отвечает круглосуточно, группа быстрого реагирования выезжает по тревоге.",
        '<div class="cta-row"><a class="btn btn-red" href="index.html#kontakty">Получить расчёт</a><a class="btn btn-line" href="tel:+73422141911">Дежурная часть</a></div>',
    )
    return shell(file="ohrana.html", title="Охранное предприятие «Одиссей-СБ» — Пермь",
                 desc="Физическая и пультовая охрана, телохранители, охрана мероприятий в Перми. Пультовая охрана от 500 ₽/мес.",
                 content=f"""{hero}

<section class="wrap canvas">
  {sec_head("Услуги", "Четыре услуги", "Режим и состав поста подбираем под объект: офис, склад, ТЦ, стройка, частный дом.")}
  <div class="bento g-2 bento--seamtop rv">
    {"".join(svc_cells)}
  </div>
</section>

<section class="wrap canvas" style="margin-top:96px">
  {sec_head("Прайс", "Пультовая охрана — открытые цены", "Абонентская плата в месяц. Оборудование и монтаж считаются отдельно по объекту.")}
  <div class="bento bento--seamtop rv">
    {price_rows}
  </div>
</section>""")


# ────────────────────────── ПОЛИГРАФ ──────────────────────────

def build_poligraf(shell, page_hero, data):
    hero = page_hero(
        "ООО Техцентр «Одиссей»",
        "Центр детекции лжи",
        "Проверки на профессиональном полиграфе «РИФ»: приём на ответственные должности, служебные расследования, периодический контроль персонала.",
        '<div class="cta-row"><a class="btn btn-red" href="index.html#kontakty">Записаться на проверку</a></div>',
    )
    return shell(file="poligraf.html", title="Центр детекции лжи «Одиссей» — проверки на полиграфе в Перми",
                 desc="Проверки на полиграфе «РИФ» в Перми: кандидаты, служебные расследования. Достоверность 95–99 %, 5000 ₽ за человека.",
                 content=f"""{hero}

<section class="wrap canvas">
  <div class="bento g-3 rv">
    <div class="cell cell--big cell--static sec-cell span2">
      <span class="kicker">Виды проверок</span>
      <h2>Что проверяем</h2>
      <ul class="list" style="margin-top:16px">
        <li>Кандидаты при приёме на ответственные должности</li>
        <li>Служебные расследования: хищения, утечки информации, злоупотребления</li>
        <li>Периодический контроль действующего персонала</li>
        <li>Частные вопросы физических лиц — конфиденциально</li>
      </ul>
    </div>
    <div class="cell cell--static" style="display:flex;flex-direction:column;justify-content:center">
      <div class="poly-big">95–99<small> %</small></div>
      <span style="font-size:13px;color:var(--muted);margin-top:12px">достоверность результатов при работе подготовленного специалиста</span>
    </div>
  </div>
  <div class="bento g-3 bento--seamtop rv">
    <div class="cell cell-flex pr-cell">
      <div class="nm">Тестирование</div>
      <div class="pr">5 000 ₽</div>
      <p>один человек, включая заключение для заказчика</p>
    </div>
    <div class="cell cell-flex">
      <span class="kicker">Оборудование</span>
      <h3 style="margin:8px 0 12px">Полиграф «РИФ»</h3>
      <p style="font-size:13px;color:var(--muted)">Профессиональный прибор; с испытуемым работает сертифицированный специалист — от этого зависит точность.</p>
    </div>
    <div class="ph" style="min-height:220px"><span>Нужен материал:<br>фото прибора «РИФ»</span></div>
  </div>
</section>""")


# ────────────────────────── ДОБРЫЕ ДЕЛА ──────────────────────────

def build_dela(shell, page_hero, data):
    deeds = data("дела")
    cards = "\n".join(
        wcard(i + 1, clean_title(d["title"]), snippet(d["text"], 180), photo_for(d["path"]))
        for i, d in enumerate(deeds)
    )
    cards += cta_cell("Ваш класс следующий", "Тир, музей техники и полевая кухня — бесплатная экскурсия для школ Перми.", "Привести класс")
    hero = page_hero(
        "АНО ВПК «Патриот»",
        "Добрые дела",
        "Бесплатные экскурсии для школ Перми: тир, музей техники, полевая кухня. Военно-патриотический клуб работает круглый год.",
        '<div class="cta-row"><a class="btn btn-red" href="index.html#kontakty">Привести класс</a></div>',
    )
    return shell(file="dela.html", title="Добрые дела — экскурсии и клуб «Патриот» | Одиссей Пермь",
                 desc="Бесплатные экскурсии для школьников Перми: стрелковый тир, музей военной техники, полевая кухня. Клуб «Патриот».",
                 content=f"""{hero}

<section class="wrap canvas">
  <div class="bento g-3 rv">
    {cards}
  </div>
</section>""")


PAGES = {
    "tir.html": lambda **kw: build_tir(**kw),
    "muzey.html": lambda **kw: build_muzey(**kw),
    "uc.html": lambda **kw: build_uc(**kw),
    "ohrana.html": lambda **kw: build_ohrana(**kw),
    "poligraf.html": lambda **kw: build_poligraf(**kw),
    "dela.html": lambda **kw: build_dela(**kw),
}
