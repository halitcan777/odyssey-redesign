# -*- coding: utf-8 -*-
"""Генератор внутренних страниц: единые шапка/футер/обвязка по ДИЗАЙН-ПРАВИЛА.md.
Правка каркаса здесь = перегенерация всех страниц (python3 build_pages.py)."""
import json, os

ROOT = os.path.dirname(os.path.abspath(__file__))

NAV = [
    ("index.html", "Главная"),
    ("o-nas.html", "О нас"),
    ("ohrana.html", "Охрана"),
    ("tir.html", "Тир"),
    ("muzey.html", "Музей"),
    ("uc.html", "Обучение"),
    ("poligraf.html", "Полиграф"),
    ("dela.html", "Добрые дела"),
]

FAVICON = "лого/favicon.png"

LOGO_SVG = '<img src="лого/одиссей-щит.png" alt="" width="30" height="37">'

SCRIPT = """<script>
const bar=document.getElementById('progress');
addEventListener('scroll',()=>{const h=document.documentElement;bar.style.width=(h.scrollTop/(h.scrollHeight-h.clientHeight)*100)+'%'},{passive:true});
document.querySelector('.burger')?.addEventListener('click',e=>{e.currentTarget.classList.toggle('open');document.querySelector('.nav-links').classList.toggle('open')});
const reduced=matchMedia('(prefers-reduced-motion: reduce)').matches;
if(!reduced){
  const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('on');io.unobserve(e.target)}}),{threshold:.1});
  document.querySelectorAll('.rv').forEach(el=>io.observe(el));
  const cio=new IntersectionObserver(es=>es.forEach(e=>{
    if(!e.isIntersecting)return;
    const el=e.target,target=+el.dataset.count,t0=performance.now();
    const step=t=>{const p=Math.min((t-t0)/1200,1);el.textContent=Math.round(target*(p<.5?2*p*p:1-Math.pow(-2*p+2,2)/2));if(p<1)requestAnimationFrame(step)};
    requestAnimationFrame(step);cio.unobserve(el);
  }),{threshold:.6});
  document.querySelectorAll('[data-count]').forEach(el=>cio.observe(el));
}else{
  document.querySelectorAll('.rv').forEach(el=>el.classList.add('on'));
}
</script>"""


def shell(*, file, title, desc, content):
    """Обвязка страницы: head + шапка (активный пункт) + контент + футер + скрипты."""
    nav_links = "\n      ".join(
        f'<a href="{href}"{" class=\"active\"" if href == file else ""}>{label}</a>'
        for href, label in NAV if href != "index.html"
    )
    return f"""<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" href="{FAVICON}">
<link rel="stylesheet" href="fonts/fonts.css">
<link rel="stylesheet" href="styles.css">
</head>
<body>
<div id="progress"></div>

<header>
  <div class="wrap nav">
    <a class="logo" href="index.html">
      <span class="logo-mark">{LOGO_SVG}</span>
      <span>Одиссей<small>группа предприятий</small></span>
    </a>
    <nav class="nav-links">
      {nav_links}
    </nav>
    <a class="nav-phone" href="tel:+73422066911">+7 (342) 20-66-911<span>многоканальный</span></a>
    <button class="burger" aria-label="Меню"><span></span><span></span><span></span></button>
  </div>
</header>

{content}

<footer>
  <div class="wrap">
    <div class="f-grid">
      <div class="f-col"><b>Группа предприятий</b>
        <div>ООО ЧОП «Одиссей-СБ» — охрана</div>
        <div>ЧУ ДПО «УЦ Одиссей» — обучение</div>
        <div>ПРСОО ССК «Одиссей» — стрелковый клуб</div>
        <div>ООО Техцентр «Одиссей» — полиграф</div>
        <div>АНО ВПК «Патриот» — работа с молодёжью</div>
      </div>
      <div class="f-col"><b>Разделы</b>
        {"".join(f'<div><a href="{h}">{l}</a></div>' for h, l in NAV)}
      </div>
      <div class="f-col"><b>Дежурная часть</b>
        <div><a href="tel:+73422141911">+7 (342) 21-41-911</a></div>
        <div><a href="tel:+79223332911">+7 (922) 333-29-11</a></div>
        <div>круглосуточно</div>
        <div style="margin-top:12px">Пермь, ул. Стахановская, 54Л</div>
      </div>
    </div>
    <div class="f-bottom">
      <div>© 2009–2026 Группа предприятий «Одиссей», Пермь</div>
      <div>Прототип редизайна</div>
    </div>
  </div>
</footer>

{SCRIPT}
</body>
</html>
"""


def page_hero(kicker, h1, sub, cta=""):
    """Компактный герой внутренней страницы."""
    return f"""<section class="wrap">
  <div class="page-hero">
    <div class="kicker">{kicker}</div>
    <h1>{h1}</h1>
    <p class="hero-sub">{sub}</p>
    {cta}
  </div>
</section>"""


def data(name):
    return json.load(open(os.path.join(ROOT, "исходники_сайта", f"данные_{name}.json"), encoding="utf-8"))


def write(file, html):
    open(os.path.join(ROOT, file), "w", encoding="utf-8").write(html)
    print("✓", file, len(html), "байт")


if __name__ == "__main__":
    import pages_content  # генераторы контента страниц
    for file, builder in pages_content.PAGES.items():
        write(file, builder(shell=shell, page_hero=page_hero, data=data))
