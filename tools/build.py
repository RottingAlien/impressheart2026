import os, shutil, html, json
from PIL import Image
ROOT='/workspace/impressart-2026'; SITE=ROOT+'/site'; A=ROOT+'/assets'
IG='https://www.instagram.com/impressheart2026/'; DM='https://ig.me/m/impressheart2026'
BASE='https://impressheart2026.web.app'
P=[
 dict(f='01_led_lamp_amizade',slug='candeeiro-led-quero-a-tua-amizade',name='Candeeiro LED “Quero a tua amizade”',cat='casa',catl='Casa & decoração',
  short='Uma placa iluminada com uma promessa de amizade para sempre.',
  alt='Candeeiro LED com placa branca de cantos arredondados, ilustração em aguarela de folhas e flores e a frase “Quero a tua amizade, hoje… amanhã… sempre!!”, sobre base de madeira clara',
  desc=['Há frases que merecem ficar à vista todos os dias. Este candeeiro tem uma placa de cantos arredondados com ilustração em aguarela — folhas de eucalipto e flores em verde suave, bege e azul — e a frase em caligrafia <em>“Quero a tua amizade… hoje… amanhã… sempre!!”</em>.',
        'A placa encaixa numa base em madeira clara, que lhe dá aquele toque acolhedor e natural. É o presente perfeito para dizer a alguém o quanto é especial. 💛'],
  pers=['A frase que quiseres — de amizade, de amor ou uma dedicatória especial','Nomes, datas ou uma mensagem só vossa','Outra ilustração ou uma fotografia']),
 dict(f='02_mug_owl_wizard',slug='caneca-mocho-feiticeiro',name='Caneca temática Mocho feiticeiro',cat='canecas',catl='Canecas',
  short='Um mocho branco de chapéu de feiticeiro, entre estrelas douradas.',
  alt='Caneca branca com asa e rebordo pretos, com ilustração de um mocho branco com chapéu de feiticeiro castanho, rodeado de pequenas estrelas douradas',
  desc=['Para quem acredita (ou quer acreditar) em magia. ✨ Esta caneca branca, com asa e rebordo pretos, tem a ilustração de um mocho branco de olhos grandes com um chapéu de feiticeiro castanho, rodeado de estrelinhas douradas.',
        'Ideal para fãs de mundos mágicos, para começar o dia com um sorriso ou para oferecer a quem tem sempre um livro na mão.'],
  pers=['Acrescenta o nome de quem vai receber','Escolhe outra ilustração temática','Junta uma frase ou mensagem especial']),
 dict(f='03_christmas_sweatshirts',slug='sweatshirts-natal-familia',name='Sweatshirts de Natal para a família',cat='natal',catl='Natal',
  short='Sweatshirts a condizer, de adulto e criança, com “Feliz Natal”.',
  alt='Duas sweatshirts brancas, uma de adulto e outra de criança, com estampa “Feliz Natal” em forma de árvore feita de presentes, com estrela dourada no topo',
  desc=['O espírito natalício está oficialmente ativado! (E o conforto também) 🎄✨',
        'Duas sweatshirts brancas a condizer — uma de adulto e outra de criança — com a estampa “Feliz Natal” desenhada em forma de árvore, com fitas, uma pilha de presentes em aguarela e uma estrela dourada no topo. Perfeitas para a foto de família, para a consoada ou para aquelas manhãs de pijama em dezembro.'],
  pers=['Os nomes de cada membro da família','Uma frase natalícia vossa','Outra ilustração de Natal','Conjuntos para toda a família ou para eventos de empresa']),
 dict(f='04_fridge_magnet_heart',slug='imanes-personalizados',name='Ímanes personalizados',cat='acessorios',catl='Acessórios',
  short='Um coração cheio de cor para alegrar o frigorífico.',
  alt='Íman em forma de coração com a frase “Smile, Be happy” em letras coloridas, um smile amarelo e pequenos corações coloridos à volta',
  desc=['Pequeno no tamanho, enorme na alegria. 😊 Este íman em forma de coração tem a frase <em>“Smile, Be happy”</em> em letras coloridas, um smile amarelo e dezenas de coraçõezinhos em rosa, azul, amarelo e vermelho.',
        'Uma lembrança doce para oferecer, para lembranças de eventos ou simplesmente para trazer um sorriso à cozinha todas as manhãs.'],
  pers=['A tua frase ou mensagem','Fotografias de quem mais gostas','Nomes, datas ou ilustrações','Lembranças para eventos e empresas (com logótipo)']),
 dict(f='05_tote_bag_xxl',slug='tote-bag-xxl-empresa',name='Tote bag XXL com logótipo de empresa',cat='empresas',catl='Empresas',
  short='Grande em tamanho, gigante em estilo. 🤍',
  alt='Tote bag XXL em tecido cor natural com alças compridas, estampada com o logótipo “Body Sereno by Cristiana – Bem-estar & Serenidade” e uma flor desenhada em castanho',
  desc=['Grande em tamanho, gigante em estilo. 🤍',
        'Uma tote bag XXL em tecido cor natural, com alças compridas, estampada com o logótipo de uma marca — neste exemplo, “Body Sereno by Cristiana · Bem-estar & Serenidade” — e uma ilustração de flor em traço castanho.',
        'A forma mais bonita (e útil!) de levar a tua marca a passear: para oferecer a clientes, usar em eventos ou vender na tua loja.'],
  pers=['O logótipo da tua empresa ou marca','Uma ilustração ou frase à tua escolha','Nomes ou mensagens para particulares e eventos']),
 dict(f='06_tshirt_mom_cool',slug='tshirt-cool-mom-club',name='T-shirt “Cool mom Club”',cat='vestuario',catl='Vestuário',
  short='Para as mães mais cool do clube. ❤️',
  alt='T-shirt branca com a frase “Cool mom Club” em letras bordeaux, com um coração no lugar do “o” de mom, sobre riscas verticais bege',
  desc=['Porque há mães que são simplesmente cool. 😎❤️ T-shirt branca com a frase <em>“Cool m♡m Club”</em> em letras bordeaux — com um coraçãozinho no lugar do “o” — sobre riscas verticais em bege.',
        'Um presente divertido para o Dia da Mãe, aniversários ou só porque sim. E pode combinar com a caneca “Cool mom Club”!'],
  pers=['Os nomes dos filhos','Outra frase (cool dad, cool avó… tu decides!)','Uma ilustração ou fotografia']),
 dict(f='07_cushion_best_friend_photo',slug='almofada-my-best-friend',name='Almofada “My best Friend” com foto',cat='casa',catl='Casa & decoração',
  short='Amigas para sempre, mesmo quando estamos longe. 👭',
  alt='Almofada branca com a frase “My best Friend” e um coração, com a fotografia de duas amigas sorridentes ao centro',
  desc=['Amigas para sempre, mesmo quando estamos longe. 👭',
        'Uma almofada branca com a vossa fotografia ao centro e as palavras <em>“My best Friend”</em>, acompanhadas de um coração desenhado. Um abraço que fica sempre por perto. 💌',
        'Encomendas abertas! 💌'],
  pers=['A vossa fotografia preferida','A frase que quiseres (em português ou inglês)','Nomes, datas ou uma mensagem especial']),
 dict(f='08_cushion_christmas',slug='almofada-natal-meia',name='Almofada de Natal “Meia de Natal”',cat='natal',catl='Natal',
  short='Uma meia de Natal dourada para aconchegar o sofá. 🎄',
  alt='Almofada branca com ilustração de uma meia de Natal em tons dourados e bege, com um presente, ramos de pinheiro e uma bengala doce, sobre um sofá ao lado de uma almofada verde-escura',
  desc=['Conforto com sabor a dezembro. 🎄✨ Almofada branca com a ilustração de uma meia de Natal em tons dourados e bege, com padrão rendilhado, de onde espreitam um presente, ramos de pinheiro e uma bengala doce.',
        'Fica linda no sofá, no quarto ou como presente para quem adora decorar a casa nesta época.'],
  pers=['O nome de quem vai receber (ou de toda a família)','Uma frase natalícia','Outra ilustração de Natal']),
 dict(f='09_cushion_sofa',slug='almofadas-natal-carrinhos',name='Almofadas decorativas “Carrinhos de Natal”',cat='natal',catl='Natal',
  short='Carrinhos vintage a levar a árvore para casa. 🚗🎄',
  alt='Duas almofadas brancas num sofá, uma com um carro vintage verde e outra com um carro vintage vermelho, ambos a transportar uma árvore de Natal no tejadilho',
  desc=['Há lá coisa mais natalícia do que ir buscar a árvore? 🚗🎄 Este par de almofadas brancas tem ilustrações de carrinhos vintage — um verde e outro vermelho — com uma árvore de Natal decorada presa no tejadilho.',
        'Um toque nostálgico e acolhedor para o sofá, que combina com tudo nesta época do ano.'],
  pers=['Nomes ou uma data especial','Uma frase à tua escolha','Outras ilustrações para todo o ano']),
 dict(f='10_mug_mothers_cool',slug='caneca-cool-mom-club',name='Caneca “Cool mom Club”',cat='canecas',catl='Canecas',
  short='Asa em forma de coração para a mãe mais cool. 💛',
  alt='Caneca branca com asa em forma de coração e a frase “Cool mom Club” em letras cor de canela, com um coração no lugar do “o”, sobre riscas verticais em aguarela amarelo-mostarda',
  desc=['O café da manhã sabe melhor numa caneca feita com amor. ❤️ Caneca branca com asa em forma de coração e a frase <em>“COOL M♡M CLUB”</em> em letras cor de canela, sobre riscas verticais em aguarela amarelo-mostarda.',
        'Para oferecer no Dia da Mãe, num aniversário ou sempre que te apetecer dizer “és a maior”.'],
  pers=['Os nomes dos filhos','Uma frase ou mensagem especial','Uma fotografia ou ilustração']),
 dict(f='11_led_lamp_personalized',slug='candeeiro-led-coracao-foto',name='Candeeiro LED personalizado com foto',cat='casa',catl='Casa & decoração',
  short='A vossa fotografia, iluminada num coração.',
  alt='Candeeiro LED em forma de coração com a fotografia de um casal, iluminado em tom quente, sobre uma base de madeira escura',
  desc=['Não dês apenas um presente, cria uma memória. 💡❤️',
        'Um candeeiro em forma de coração com a vossa fotografia, iluminado por uma luz quente e acolhedora a partir da base em madeira. Quando se acende, a memória ganha vida.',
        'Perfeito para o Dia dos Namorados, aniversários de casamento ou para quem tem saudades.'],
  pers=['A vossa fotografia preferida','Nomes, datas ou uma frase especial','Ideal para casais, família, amigos ou animais de estimação']),
]
CATS=[('todos','Todos'),('casa','Casa & decoração'),('canecas','Canecas'),('vestuario','Vestuário'),('natal','Natal'),('acessorios','Acessórios'),('empresas','Empresas')]

# images
for p in P:
    src=f"{A}/{p['f']}.jpg"; shutil.copy(src,f"{SITE}/img/originais/{p['f']}.jpg")
    im=Image.open(src).convert('RGB'); p['w'],p['h']=im.size
    for w,suf in ((900,''),(480,'-sm')):
        r=im.copy(); r.thumbnail((w,w*2)); p['rw'+suf]=r.size
        r.save(f"{SITE}/img/produtos/{p['slug']}{suf}.webp",'WEBP',quality=80,method=6)
        r.save(f"{SITE}/img/produtos/{p['slug']}{suf}.jpg",'JPEG',quality=82,optimize=True,progressive=True)
# OG image 1200x630
og=Image.new('RGB',(1200,630),(246,238,238))
for i,idx in enumerate([10,6,0]):
    im=Image.open(f"{A}/{P[idx]['f']}.jpg").convert('RGB')
    s=min(im.size); im=im.crop(((im.width-s)//2,(im.height-s)//2,(im.width+s)//2,(im.height+s)//2)).resize((380,380))
    og.paste(im,(30+i*390,125))
og.save(f"{SITE}/img/og-image.jpg",quality=85)

def head(title,desc,depth,path,img='img/og-image.jpg'):
    r='../'*depth
    return f'''<!doctype html>
<html lang="pt-PT">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<meta name="theme-color" content="#F6EEEE">
<link rel="canonical" href="{BASE}/{path}">
<meta property="og:type" content="website">
<meta property="og:locale" content="pt_PT">
<meta property="og:site_name" content="Impress Heart">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:url" content="{BASE}/{path}">
<meta property="og:image" content="{BASE}/{img}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{r}img/favicon.svg" type="image/svg+xml">
<link rel="icon" href="{r}img/favicon-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="{r}img/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600;700&family=Dancing+Script:wght@500;600&family=Nunito:wght@400;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{r}css/style.css">
<script src="{r}js/main.js" defer></script>
</head>
<body>
<a class="skip" href="#conteudo">Saltar para o conteúdo</a>
'''
IGSVG='<svg aria-hidden="true" viewBox="0 0 24 24" width="20" height="20"><rect x="3" y="3" width="18" height="18" rx="5" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="12" cy="12" r="4" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="17.5" cy="6.5" r="1.2" fill="currentColor"/></svg>'
def header(depth,active):
    r='../'*depth
    def a(h,l,k): return f'<li><a href="{r}{h}"{" aria-current=\"page\"" if k==active else ""}>{l}</a></li>'
    return f'''<header class="site-header">
 <div class="wrap nav-wrap">
  <a class="brand" href="{r}index.html" aria-label="Impress Heart — página inicial"><img src="{r}img/logo.svg" alt="" width="52" height="52"><span>Impress Heart</span></a>
  <button class="nav-toggle" aria-expanded="false" aria-controls="menu"><span class="sr">Abrir menu</span><span class="bar"></span></button>
  <nav id="menu" aria-label="Principal"><ul>
   {a("index.html","Início","home")}{a("index.html#produtos","Produtos","produtos")}{a("sobre.html","Sobre","sobre")}{a("contacto.html","Contacto","contacto")}
   <li><a class="ig-link" href="{IG}" target="_blank" rel="noopener">{IGSVG}<span>@impressheart2026</span></a></li>
  </ul></nav>
 </div>
</header>
<main id="conteudo">
'''
def footer(depth):
    r='../'*depth
    return f'''</main>
<footer class="site-footer">
 <div class="wrap foot">
  <div><img src="{r}img/logo.svg" alt="Impress Heart" width="96" height="96"></div>
  <div>
   <p class="script">Prints that touch the heart</p>
   <p>Criação de estampas e serviço de personalização, para particulares/eventos e empresas.</p>
  </div>
  <div>
   <p><a class="btn btn-ghost" href="{DM}" target="_blank" rel="noopener">💌 Pedir orçamento</a></p>
   <p><a class="ig-link" href="{IG}" target="_blank" rel="noopener">{IGSVG}<span>Segue-nos no Instagram</span></a></p>
  </div>
 </div>
 <p class="copy">© <span data-year>2026</span> Impress Heart · Feito com ❤️ em Portugal</p>
</footer>
</body>
</html>
'''
def pic(p,depth,sizes,lazy=True,cls=''):
    r='../'*depth; s=p['slug']
    w,h=p['rw']
    return f'''<picture>
 <source type="image/webp" srcset="{r}img/produtos/{s}-sm.webp 480w, {r}img/produtos/{s}.webp 900w" sizes="{sizes}">
 <img class="{cls}" src="{r}img/produtos/{s}.jpg" srcset="{r}img/produtos/{s}-sm.jpg 480w, {r}img/produtos/{s}.jpg 900w" sizes="{sizes}" width="{w}" height="{h}" alt="{html.escape(p['alt'])}"{' loading="lazy"' if lazy else ''} decoding="async">
</picture>'''
def card(p,depth):
    r='../'*depth
    return f'''<li class="card" data-cat="{p['cat']}">
 <a class="card-link" href="{r}produtos/{p['slug']}.html">
  <div class="card-img">{pic(p,depth,"(max-width: 600px) 90vw, 300px")}</div>
  <div class="card-body"><span class="tag">{p['catl']}</span><h3>{p['name']}</h3><p>{p['short']}</p><span class="more">Ver detalhes →</span></div>
 </a>
</li>'''

def write(path,s):
    os.makedirs(os.path.dirname(path),exist_ok=True); open(path,'w').write(s)

# index
chips=''.join(f'<button class="chip" type="button" data-filter="{k}" aria-pressed="{"true" if k=="todos" else "false"}">{l}</button>' for k,l in CATS)
hero=P[10]
idx=head('Impress Heart · Estampas e presentes personalizados','Criação de estampas e serviço de personalização para particulares, eventos e empresas. Canecas, almofadas, candeeiros LED, t-shirts e muito mais. Pede o teu orçamento sem compromisso!',0,'')+header(0,'home')+f'''
<section class="hero">
 <div class="wrap hero-grid">
  <div class="hero-text">
   <p class="eyebrow">✨ Estampas &amp; personalização</p>
   <h1>Não dês apenas um presente, <em>cria uma memória.</em> <span aria-hidden="true">💡❤️</span></h1>
   <p class="lead">Canecas, almofadas, candeeiros LED, t-shirts e muito mais — personalizados com a tua frase, as tuas fotos, os nomes de quem mais amas ou o logótipo da tua empresa.</p>
   <div class="cta-row">
    <a class="btn" href="{DM}" target="_blank" rel="noopener">💌 Pedir orçamento</a>
    <a class="btn btn-ghost" href="#produtos">Ver produtos</a>
   </div>
   <p class="note">Envia mensagem privada para pedir um orçamento sem compromisso!</p>
  </div>
  <div class="hero-art">
   <div class="polaroid p1">{pic(P[10],0,"(max-width: 800px) 60vw, 360px",lazy=False)}</div>
   <div class="polaroid p2">{pic(P[6],0,"(max-width: 800px) 40vw, 240px",lazy=False)}</div>
   <div class="polaroid p3">{pic(P[9],0,"(max-width: 800px) 40vw, 220px",lazy=False)}</div>
  </div>
 </div>
</section>

<section class="for-who wrap" aria-label="Para quem">
 <div class="pill-card"><span aria-hidden="true">🎁</span><h2>Particulares</h2><p>Presentes únicos para quem mais gostas: uma frase especial, os nomes dos filhos, aquela foto que diz tudo.</p></div>
 <div class="pill-card"><span aria-hidden="true">🥂</span><h2>Eventos</h2><p>Lembranças para casamentos, batizados, aniversários e festas — todas a condizer e cheias de significado.</p></div>
 <div class="pill-card"><span aria-hidden="true">💼</span><h2>Empresas</h2><p>O logótipo da tua marca em tote bags, canecas, t-shirts e outros artigos para a equipa ou para os clientes.</p></div>
</section>

<section id="produtos" class="products wrap">
 <div class="section-head">
  <p class="eyebrow">Feito com amor ❤️</p>
  <h2>Os nossos produtos</h2>
  <p>Cada peça é um ponto de partida: escolhe a que mais gostas e conta-nos como a queres personalizar.</p>
 </div>
 <div class="chips" role="group" aria-label="Filtrar produtos por categoria">{chips}</div>
 <ul class="grid" id="grelha">
{chr(10).join(card(p,0) for p in P)}
 </ul>
</section>

<section class="how">
 <div class="wrap">
  <div class="section-head"><p class="eyebrow">Simples assim ✨</p><h2>Como funciona</h2></div>
  <ol class="steps">
   <li><span>1</span><h3>Escolhe</h3><p>Escolhe o produto que mais gostas — ou inspira-te nos nossos trabalhos.</p></li>
   <li><span>2</span><h3>Conta-nos a tua ideia</h3><p>Envia-nos mensagem privada no Instagram com a frase, fotos, nomes ou logótipo.</p></li>
   <li><span>3</span><h3>Recebe o orçamento</h3><p>Respondemos com um orçamento sem compromisso, feito à tua medida. 💌</p></li>
  </ol>
  <p class="center"><a class="btn" href="{DM}" target="_blank" rel="noopener">💌 Enviar mensagem no Instagram</a></p>
 </div>
</section>

<section class="quote wrap">
 <blockquote><p>Amigas para sempre, mesmo quando estamos longe. 👭</p><p class="script">Encomendas abertas! 💌</p></blockquote>
</section>
'''+footer(0)
write(SITE+'/index.html',idx)

# products
for i,p in enumerate(P):
    prev=P[i-1]; nxt=P[(i+1)%len(P)]
    rel=[q for q in P if q['cat']==p['cat'] and q is not p]
    rel=(rel+[q for q in P if q is not p and q not in rel])[:3]
    title=f"{p['name'].replace('“','\"').replace('”','\"')} · Impress Heart"
    d=f"{p['short']} Personalizável com a tua frase, fotos, nomes ou logótipo. Pede orçamento sem compromisso por mensagem no Instagram."
    ld=dict({'@context':'https://schema.org','@type':'Product','name':p['name'],'image':f"{BASE}/img/produtos/{p['slug']}.jpg",'description':p['short'],'brand':{'@type':'Brand','name':'Impress Heart'}})
    s=head(title,d,1,f"produtos/{p['slug']}",f"img/produtos/{p['slug']}.jpg")+header(1,'produtos')+f'''
<nav class="crumbs wrap" aria-label="Navegação estrutural"><ol><li><a href="../index.html">Início</a></li><li><a href="../index.html#produtos">Produtos</a></li><li aria-current="page">{p['name']}</li></ol></nav>
<article class="product wrap">
 <div class="product-media">
  {pic(p,1,"(max-width: 860px) 92vw, 560px",lazy=False,cls='main-img')}
  <p class="orig"><a href="../img/originais/{p['f']}.jpg" target="_blank" rel="noopener">Ver fotografia em tamanho original</a></p>
 </div>
 <div class="product-info">
  <span class="tag">{p['catl']}</span>
  <h1>{p['name']}</h1>
  {''.join(f"<p>{x}</p>" for x in p['desc'])}
  <h2>Torna-o teu ✨</h2>
  <ul class="ticks">{''.join(f"<li>{x}</li>" for x in p['pers'])}</ul>
  <p class="small">Para particulares, eventos e empresas. Os detalhes (tamanhos, cores, quantidades) combinamos contigo por mensagem.</p>
  <div class="cta-box">
   <a class="btn btn-big" href="{DM}" target="_blank" rel="noopener">💌 Pedir orçamento</a>
   <p>Abre uma mensagem privada no Instagram. Orçamento sem compromisso!</p>
  </div>
 </div>
</article>
<nav class="pager wrap" aria-label="Outros produtos"><a href="{prev['slug']}.html">← {prev['name']}</a><a href="{nxt['slug']}.html">{nxt['name']} →</a></nav>
<section class="products wrap related"><h2>Também vais adorar</h2><ul class="grid">{''.join(card(q,1) for q in rel)}</ul></section>
<script type="application/ld+json">{json.dumps(ld,ensure_ascii=False)}</script>
'''+footer(1)
    write(f"{SITE}/produtos/{p['slug']}.html",s)

# sobre
sobre=head('Sobre · Impress Heart','Conhece a Impress Heart: criação de estampas e serviço de personalização para particulares, eventos e empresas.',0,'sobre')+header(0,'sobre')+f'''
<section class="page-hero"><div class="wrap narrow"><p class="eyebrow">Sobre nós</p><h1>Prints that touch <em>the heart</em> ❤️</h1></div></section>
<section class="wrap narrow prose">
 <img class="float-logo" src="img/logo.svg" alt="Logótipo Impress Heart: coração em aguarela vermelho e rosa" width="200" height="200">
 <p class="lead">A Impress Heart dedica-se à criação de estampas e ao serviço de personalização, para particulares, eventos e empresas.</p>
 <p>Acreditamos que os melhores presentes são aqueles que contam uma história. Por isso, transformamos as tuas ideias em peças únicas: uma frase especial, os nomes dos filhos, uma ilustração, as fotografias de que mais gostas, uma mensagem que só vocês percebem — ou o logótipo da tua empresa.</p>
 <p>Canecas, almofadas, candeeiros LED, t-shirts, sweatshirts, tote bags, ímanes… cada peça é pensada com carinho, para que quem a recebe sinta o mesmo que tu sentiste ao escolhê-la.</p>
 <p class="script big">Não dês apenas um presente, cria uma memória. 💡❤️</p>
 <h2>O que podemos personalizar</h2>
 <ul class="ticks cols">
  <li>Frases e mensagens especiais</li><li>Nomes (dos filhos, do casal, da família…)</li><li>Ilustrações</li><li>Fotografias</li><li>Logótipos de empresa</li><li>Lembranças para eventos</li>
 </ul>
 <div class="cta-box"><a class="btn btn-big" href="{DM}" target="_blank" rel="noopener">💌 Conta-nos a tua ideia</a><p>Envia mensagem privada para pedir um orçamento sem compromisso!</p></div>
</section>
'''+footer(0)
write(SITE+'/sobre.html',sobre)

contacto=head('Contacto · Impress Heart','Fala connosco por mensagem privada no Instagram @impressheart2026 e pede o teu orçamento sem compromisso.',0,'contacto')+header(0,'contacto')+f'''
<section class="page-hero"><div class="wrap narrow"><p class="eyebrow">Contacto</p><h1>Vamos criar algo <em>especial</em>? ✨</h1><p class="lead">Falamos contigo por mensagem privada no Instagram — é lá que tratamos de todos os orçamentos.</p></div></section>
<section class="wrap contact-grid">
 <div class="contact-card">
  <span class="big-emoji" aria-hidden="true">💌</span>
  <h2>Pede o teu orçamento</h2>
  <p>Envia-nos mensagem com a tua ideia: o produto, a frase, as fotos, os nomes ou o logótipo. Respondemos com um orçamento sem compromisso.</p>
  <a class="btn btn-big" href="{DM}" target="_blank" rel="noopener">Enviar mensagem privada</a>
 </div>
 <div class="contact-card">
  <span class="big-emoji" aria-hidden="true">📸</span>
  <h2>Segue-nos no Instagram</h2>
  <p>Vê os nossos trabalhos mais recentes, as novidades e as encomendas especiais.</p>
  <a class="btn btn-ghost btn-big" href="{IG}" target="_blank" rel="noopener">@impressheart2026</a>
 </div>
</section>
<section class="wrap narrow prose">
 <h2>Para te ajudarmos mais depressa, diz-nos:</h2>
 <ul class="ticks">
  <li>Que produto te interessa (podes enviar o link desta página 😉)</li>
  <li>O que queres personalizar: frase, nomes, fotografia, ilustração ou logótipo</li>
  <li>Quantas unidades precisas — é para ti, para um evento ou para a tua empresa?</li>
  <li>Se há alguma data especial em que precisas da encomenda</li>
 </ul>
</section>
'''+footer(0)
write(SITE+'/contacto.html',contacto)

e404=head('Página não encontrada · Impress Heart','Esta página não existe.',0,'404')+header(0,'')+f'''
<section class="page-hero"><div class="wrap narrow center"><p class="eyebrow">Erro 404</p><h1>Ups! Esta página perdeu-se 💔</h1><p class="lead">Mas há muitos presentes à tua espera.</p><p><a class="btn" href="/index.html">Voltar ao início</a></p></div></section>
'''+footer(0)
write(SITE+'/404.html',e404.replace('href="img/','href="/img/').replace('src="img/','src="/img/').replace('href="css/','href="/css/').replace('src="js/','src="/js/').replace('href="index.html','href="/index.html').replace('href="sobre.html','href="/sobre.html').replace('href="contacto.html','href="/contacto.html'))
write(SITE+'/robots.txt','User-agent: *\nAllow: /\n')
print('built',len(P))
