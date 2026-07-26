# -*- coding: utf-8 -*-
"""Брендбук «Одиссей» – фирменный стиль 2.0. А4 альбомный, 9 листов, print → PDF."""
import os, subprocess

ROOT = os.path.dirname(os.path.abspath(__file__))
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

CSS = """
@page{size:A4 landscape;margin:0}
*{margin:0;padding:0;box-sizing:border-box;border-radius:0}
:root{--bg:#FDFBF7;--cell:#FFF;--line:#E4D9C4;--ink:#1F1A17;--muted:#79695A;--red:#93221B;--alarm:#C8102E;--gold:#C9A227;--graphite:#101114;--gcell:#16181C;--gink:#F2F1EE}
body{font-family:'Inter',sans-serif;color:var(--ink);font-size:10pt;line-height:1.55}
.page{width:297mm;height:209mm;background:var(--bg);padding:12mm 16mm;display:flex;flex-direction:column;page-break-after:always;position:relative;overflow:hidden}
.page.dark{background:var(--graphite);color:var(--gink)}
h1,h2,h3{font-family:'Oswald',sans-serif;text-transform:uppercase;font-weight:700}
/* колонтитул */
.pagehead{display:flex;align-items:center;gap:5mm;border-bottom:1px solid var(--line);padding-bottom:4mm;margin-bottom:8mm}
.pagehead img{width:9mm}
.pagehead .t{font-family:'Oswald',sans-serif;font-weight:700;font-size:11pt;letter-spacing:.08em;text-transform:uppercase}
.pagehead .sec{margin-left:auto;font-family:'Oswald',sans-serif;font-weight:600;font-size:13pt;letter-spacing:.1em;text-transform:uppercase;color:var(--red)}
.pageno{position:absolute;bottom:8mm;right:16mm;font-size:8pt;color:var(--muted)}
/* сетки */
.cols{display:flex;gap:10mm;flex:1;min-height:0}
.col{flex:1;min-width:0}
.bento{display:grid;gap:1px;background:var(--line);border:1px solid var(--line)}
.cell{background:var(--cell);padding:6mm}
.swatch{height:26mm;display:flex;flex-direction:column;justify-content:flex-end;padding:4mm;color:#fff;font-size:8pt;line-height:1.5}
.swatch b{font-family:'Oswald',sans-serif;font-size:10pt;letter-spacing:.04em}
.note{font-size:9pt;color:var(--muted);margin-top:4mm;max-width:210mm}
.klabel{font-size:7.5pt;font-weight:600;letter-spacing:.2em;text-transform:uppercase;color:var(--red);margin-bottom:2mm}
.dark .klabel{color:var(--alarm)}
img.shot{width:100%;border:1px solid var(--line);display:block}
"""

CAMO = """<svg width="180" height="120" viewBox="0 0 180 120" style="position:absolute;top:0;right:0"><g fill="#93221B"><rect x="60" y="0" width="30" height="30"/><rect x="90" y="15" width="30" height="30"/><rect x="150" y="0" width="30" height="30"/><rect x="120" y="45" width="30" height="30"/><rect x="150" y="75" width="30" height="30"/></g><g fill="#C9A227" opacity=".85"><rect x="30" y="15" width="30" height="30"/><rect x="150" y="30" width="30" height="30"/></g></svg>"""


def ph(section):
    return f"""<div class="pagehead"><img src="ассеты/новый_знак.png"><span class="t">Одиссей · фирменный стиль 2.0</span><span class="sec">{section}</span></div>"""


P = []

# ── 1. Обложка
P.append(f"""<div class="page dark" style="align-items:center;justify-content:center;text-align:center">
{CAMO}
<img src="ассеты/новый_знак.png" style="width:34mm;margin-bottom:10mm">
<div style="font-family:'Oswald',sans-serif;font-weight:700;font-size:40pt;letter-spacing:.1em;line-height:1">ОДИССЕЙ</div>
<div style="font-size:9pt;letter-spacing:.34em;color:var(--gold);margin-top:3mm">ГРУППА ПРЕДПРИЯТИЙ · ПЕРМЬ</div>
<div style="margin-top:14mm;font-family:'Oswald',sans-serif;font-weight:600;font-size:15pt;letter-spacing:.14em;color:#9BA0A8;text-transform:uppercase">Фирменный стиль 2.0</div>
<div style="font-size:8.5pt;color:#9BA0A8;margin-top:2mm">брендбук · июль 2026</div>
</div>""")

# ── 2. Эволюция знака
P.append(f"""<div class="page">{ph('Фирменный знак')}
<div class="cols">
  <div class="col">
    <div class="klabel">Было · 2009</div>
    <div style="border:1px solid var(--line);background:#fff;display:flex;align-items:center;justify-content:center;height:105mm"><img src="ассеты/старый_знак.png" style="width:44mm"></div>
    <p class="note">Объёмный щит с градиентами и бликами – язык печатной полиграфии 2000-х. Плохо масштабируется в цифре: мелкие детали пропадают в фавиконе, интерфейсах и на шевронах.</p>
  </div>
  <div class="col">
    <div class="klabel">Стало · 2026</div>
    <div style="border:1px solid var(--line);background:#fff;display:flex;align-items:center;justify-content:center;height:105mm"><img src="ассеты/новый_знак.png" style="width:40mm"></div>
    <p class="note">Тот же щит и шлем греческого воина – очищенные до плоской формы. Один цвет, чёткий силуэт: работает от 12 мм на визитке до фасадной вывески, в светлой и тёмной средах.</p>
  </div>
</div>
<p class="note" style="margin-top:6mm"><b>Смысл сохранён:</b> щит – защита и стабильность, шлем – воин на страже. Знак читается за секунду и не требует пояснений.</p>
<div class="pageno">02</div></div>""")

# ── 3. Варианты знака и охранное поле
P.append(f"""<div class="page">{ph('Использование знака')}
<div class="cols">
  <div class="col">
    <div class="klabel">Исполнения</div>
    <div class="bento" style="grid-template-columns:1fr 1fr">
      <div class="cell" style="display:flex;align-items:center;justify-content:center;height:44mm"><img src="ассеты/новый_знак.png" style="width:22mm"></div>
      <div class="cell" style="background:var(--graphite);display:flex;align-items:center;justify-content:center"><img src="ассеты/новый_знак.png" style="width:22mm"></div>
      <div class="cell" style="display:flex;align-items:center;justify-content:center;height:44mm;filter:grayscale(1)"><img src="ассеты/новый_знак.png" style="width:22mm"></div>
      <div class="cell" style="background:var(--red);display:flex;align-items:center;justify-content:center"><img src="ассеты/новый_знак.png" style="width:22mm;filter:brightness(0) invert(1)"></div>
    </div>
    <p class="note">Основное – алый знак на светлом или графитовом фоне. Допустимы монохром и белая выворотка на бордовом.</p>
  </div>
  <div class="col">
    <div class="klabel">Охранное поле и минимальный размер</div>
    <div style="border:1px dashed var(--gold);display:flex;align-items:center;justify-content:center;height:64mm;position:relative;margin-bottom:4mm">
      <img src="ассеты/новый_знак.png" style="width:26mm">
      <span style="position:absolute;right:2mm;top:2mm;font-size:7.5pt;color:var(--muted)">поле = ½ высоты знака</span>
    </div>
    <ul style="list-style:none;font-size:9pt;color:var(--muted);line-height:2">
      <li>· Минимальный размер в печати – 12 мм по высоте</li>
      <li>· В цифре – 24 px (фавикон – упрощённый шлем)</li>
      <li>· Не наклонять, не перекрашивать, не добавлять тени и градиенты</li>
      <li>· На фотофоне – только на плашке фирменных цветов</li>
    </ul>
  </div>
</div>
<div class="pageno">03</div></div>""")

# ── 4. Палитра
P.append(f"""<div class="page">{ph('Цвет')}
<div class="cols">
  <div class="col">
    <div class="klabel">Печать и светлая среда</div>
    <div class="bento" style="grid-template-columns:1fr 1fr">
      <div class="cell swatch" style="background:#93221B"><b>Бордо</b>#93221B · RGB 147/34/27<br>CMYK 0/100/100/35 · Pantone 486C</div>
      <div class="cell swatch" style="background:#C9A227"><b>Золото</b>#C9A227 · RGB 201/162/39<br>Pantone 465C</div>
      <div class="cell swatch" style="background:#1F1A17"><b>Графит текста</b>#1F1A17</div>
      <div class="cell swatch" style="background:#FDFBF7;color:#1F1A17;border:1px solid #E4D9C4"><b>Крем-фон</b>#FDFBF7 · линии #E4D9C4</div>
    </div>
    <p class="note">Преемственность: бордо и золото – из первого брендбука (Pantone 486C/465C), теперь в плоском исполнении без градиентов.</p>
  </div>
  <div class="col">
    <div class="klabel">Цифровая тёмная среда</div>
    <div class="bento" style="grid-template-columns:1fr 1fr">
      <div class="cell swatch" style="background:#101114"><b>Графит-фон</b>#101114 · ячейки #16181C</div>
      <div class="cell swatch" style="background:#C8102E"><b>Алый акцент</b>#C8102E · hover #E01236</div>
      <div class="cell swatch" style="background:#16181C"><b>Ячейка</b>#16181C · линии #26282E</div>
      <div class="cell swatch" style="background:#F2F1EE;color:#1F1A17"><b>Светлый текст</b>#F2F1EE · вторичный #9BA0A8</div>
    </div>
    <p class="note">В тёмной теме сайта бордо уступает место алому – контраст и «тревожная» энергия службы 24/7. Золото – дозированно: метки лицензий и деталей.</p>
  </div>
</div>
<div class="pageno">04</div></div>""")

# ── 5. Типографика
P.append(f"""<div class="page">{ph('Типографика')}
<div class="cols">
  <div class="col">
    <div class="klabel">Заголовки · Oswald</div>
    <div style="font-family:'Oswald',sans-serif;font-weight:700;font-size:30pt;text-transform:uppercase;line-height:1.05">Безопасность, на которую можно положиться</div>
    <div style="font-family:'Oswald',sans-serif;font-weight:600;font-size:13pt;margin-top:4mm;color:var(--muted)">АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ<br>abcdefghijklmnopqrstuvwxyz 0123456789 ₽№</div>
    <p class="note">Oswald 600/700, всегда ВЕРХНИМ РЕГИСТРОМ. Замена антиквы старого стиля: жёстче, современнее, ближе к форме.</p>
  </div>
  <div class="col">
    <div class="klabel">Текст · Inter</div>
    <p style="font-size:11pt;max-width:120mm">Кадровую основу группы составляют бывшие сотрудники силовых структур. Дежурная часть отвечает круглосуточно: +7 (342) 21-41-911.</p>
    <div style="font-size:9.5pt;margin-top:3mm;color:var(--muted)">Inter Regular / Medium / Semibold · АаБбВв 0123456789</div>
    <div class="klabel" style="margin-top:8mm">Фирменные приёмы набора</div>
    <ul style="list-style:none;font-size:9pt;color:var(--muted);line-height:2">
      <li>· КИККЕР С ЧЕРТОЙ – красная строка-ярлык над заголовком</li>
      <li>· Цифры-статы Oswald 700 (2006 · 500+ · 24/7)</li>
      <li>· Только короткие тире (–), кавычки-«ёлочки»</li>
      <li>· Цены всегда со знаком ₽ и неразрывным пробелом</li>
    </ul>
  </div>
</div>
<div class="pageno">05</div></div>""")

# ── 6. Графический язык
P.append(f"""<div class="page">{ph('Графический язык')}
<div class="cols">
  <div class="col">
    <div class="klabel">Бенто-сетка</div>
    <div class="bento" style="grid-template-columns:1fr 1fr 1fr">
      <div class="cell" style="height:30mm"><b style="font-family:'Oswald',sans-serif;font-size:14pt;color:var(--red)">26</b><br><span style="font-size:8pt;color:var(--muted)">единиц оружия</span></div>
      <div class="cell"><b style="font-family:'Oswald',sans-serif;font-size:14pt;color:var(--red)">24/7</b><br><span style="font-size:8pt;color:var(--muted)">дежурная часть</span></div>
      <div class="cell"><b style="font-family:'Oswald',sans-serif;font-size:14pt;color:var(--red)">2011</b><br><span style="font-size:8pt;color:var(--muted)">первый закрытый клуб</span></div>
    </div>
    <p class="note">Блоки стыкуются общими линиями в 1 px – как посты одного периметра. Ноль скруглений, ноль теней: строгость и порядок.</p>
    <div class="klabel" style="margin-top:7mm">Пиксель-камуфляж</div>
    <svg width="220" height="60" viewBox="0 0 220 60"><g fill="#93221B"><rect x="0" y="0" width="20" height="20"/><rect x="20" y="20" width="20" height="20"/><rect x="60" y="10" width="20" height="20"/><rect x="90" y="30" width="20" height="20"/><rect x="140" y="0" width="20" height="20"/><rect x="170" y="20" width="20" height="20"/></g><g fill="#C9A227" opacity=".85"><rect x="40" y="35" width="20" height="20"/><rect x="120" y="15" width="20" height="20"/><rect x="200" y="35" width="20" height="20"/></g></svg>
    <p class="note">Кластеры квадратов – цифровой камуфляж. Акцент углов макетов, не фон.</p>
  </div>
  <div class="col">
    <div class="klabel">Выноски-плашки</div>
    <div style="background:#141519;color:#F5F0E6;border-left:3px solid var(--red);padding:4mm 5mm;max-width:70mm;margin-bottom:3mm">
      <div style="font-family:'Oswald',sans-serif;font-weight:600;font-size:9.5pt;text-transform:uppercase">Служебное оружие</div>
      <div style="font-size:8pt;color:#C8BEB0">подготовка и зачёты в собственном тире</div>
    </div>
    <p class="note">Аннотации к фото: тёмная плашка, красное ребро, Oswald-заголовок. Фотографии – ч/б с возвратом цвета при наведении (в цифре).</p>
    <div class="klabel" style="margin-top:7mm">Правила</div>
    <ul style="list-style:none;font-size:9pt;color:var(--muted);line-height:2">
      <li>✓ общие 1px-линии, воздух 96 px между полотнами</li>
      <li>✓ фото реальные, ч/б 85%</li>
      <li>✗ скругления, тени, градиенты, стоковые фото</li>
      <li>✗ более двух акцентных цветов в макете</li>
    </ul>
  </div>
</div>
<div class="pageno">06</div></div>""")

# ── 7. Цифровая среда
P.append(f"""<div class="page">{ph('Цифровая среда')}
<div class="cols">
  <div class="col"><div class="klabel">Светлая тема · одиссейпермь.рф</div><img class="shot" src="ассеты/сайт_светлая.jpg"></div>
  <div class="col"><div class="klabel">Тёмная тема</div><img class="shot" src="ассеты/сайт_тёмная.jpg"></div>
</div>
<p class="note" style="margin-top:5mm">Сайт группы: 8 разделов, две темы, реальные цены и документы. Герой – сотрудник в экипировке с аннотациями; арсенал тира – 26 карточек; музей техники – 11 единиц.</p>
<div class="pageno">07</div></div>""")

# ── 8. Деловая документация
P.append(f"""<div class="page">{ph('Документы')}
<div class="cols">
  <div class="col" style="flex:0 0 88mm"><img class="shot" src="ассеты/кп_превью.png"></div>
  <div class="col">
    <div class="klabel">Шаблон коммерческого предложения</div>
    <ul style="list-style:none;font-size:9.5pt;color:var(--muted);line-height:2.1">
      <li>· Шапка: знак + «Одиссей» + контакты в одну строку</li>
      <li>· Киккер с чертой и крупный Oswald-заголовок</li>
      <li>· Строка цифр-статов (2006 · 500+ · 120+ · 5 ГБР)</li>
      <li>· Бенто-таблицы услуг и цен с общими линиями</li>
      <li>· Цены – Oswald, бордо, всегда «от … ₽»</li>
      <li>· Подвал: реквизиты, лицензия ЧО № 056449, менеджер</li>
      <li>· Водяной знак-щит 6% в правом нижнем углу</li>
    </ul>
    <p class="note">Готовые файлы: КП «Физическая охрана», «Техническая охрана», «Корпоративный тир». Один лист А4 – читается за 40 секунд.</p>
  </div>
</div>
<div class="pageno">08</div></div>""")

# ── 9. Финал
P.append(f"""<div class="page dark" style="justify-content:center">
{CAMO}
<div style="max-width:170mm">
<div class="klabel">Одна группа – один стандарт</div>
<div style="font-family:'Oswald',sans-serif;font-weight:700;font-size:26pt;text-transform:uppercase;line-height:1.1;margin-bottom:6mm">Охрана · Тир · Обучение · Полиграф</div>
<p style="font-size:10pt;color:#9BA0A8;max-width:150mm">Фирменный стиль 2.0 объединяет все предприятия группы: сайт, документы, экипировку и носители. Хранитель стиля – дизайн-репозиторий проекта; правки согласуются с правилами настоящего брендбука.</p>
<div style="display:flex;gap:14mm;margin-top:10mm;font-size:9pt;color:#9BA0A8">
  <div><b style="color:#F2F1EE">одиссейпермь.рф</b><br>сайт группы</div>
  <div><b style="color:#F2F1EE">+7 (342) 20-66-911</b><br>многоканальный</div>
  <div><b style="color:#F2F1EE">Пермь, Стахановская, 54</b><br>охрана · тир · учебный центр</div>
</div>
</div>
<div class="pageno" style="color:#9BA0A8">09</div></div>""")

html = ("""<!DOCTYPE html><html lang="ru"><head><meta charset="UTF-8">
<link rel="stylesheet" href="../fonts/fonts.css"><style>""" + CSS + "</style></head><body>" + "\n".join(P) + "</body></html>")
path = os.path.join(ROOT, "_брендбук.html")
open(path, "w", encoding="utf-8").write(html)
pdf = os.path.join(ROOT, "БРЕНДБУК_Одиссей_2.0.pdf")
subprocess.run([CHROME, "--headless", "--disable-gpu", f"--print-to-pdf={pdf}", "--no-pdf-header-footer",
                "--virtual-time-budget=10000", f"file://{path}"], capture_output=True)
print("✓ БРЕНДБУК_Одиссей_2.0.pdf", os.path.getsize(pdf) // 1024, "КБ")
