# Impress Heart · @impressheart2026

Site estático da **Impress Heart** — criação de estampas e serviço de personalização para particulares, eventos e empresas.

🌐 **Site publicado:** https://impressheart2026.web.app
📸 **Instagram:** https://www.instagram.com/impressheart2026/
💌 **Pedir orçamento (DM):** https://ig.me/m/impressheart2026

> A marca não publica preços: todos os produtos têm o botão **“Pedir orçamento”**, que abre uma mensagem privada no Instagram.

## Estrutura

```
site/                  ← pasta publicada no Firebase Hosting
  index.html           ← início (hero, para quem, grelha de produtos com filtros, como funciona)
  sobre.html
  contacto.html        ← só Instagram (DM + perfil)
  404.html
  produtos/*.html      ← uma página por produto (11)
  css/style.css
  js/main.js           ← menu mobile + filtros por categoria
  img/logo.svg         ← logótipo recriado em SVG
  img/favicon.svg, favicon-32.png, apple-touch-icon.png, og-image.jpg
  img/produtos/        ← fotos otimizadas (webp + jpg, 900px e 480px)
  img/originais/       ← fotos originais (fallback / tamanho original)
tools/build.py         ← gera as páginas HTML e as imagens otimizadas
tools/check.js         ← verificação de links/imagens + screenshots (Playwright)
firebase.json, .firebaserc
```

## ⚠️ Imagens (pendente)

As imagens binárias (`site/img/produtos/*`, `site/img/originais/*`, `favicon-32.png`, `apple-touch-icon.png`, `og-image.jpg`) ainda não estão neste repositório: o primeiro commit foi feito por uma via que só aceita ficheiros de texto. O site publicado em https://impressheart2026.web.app já inclui todas as imagens. Para as adicionar aqui, faz `git add site/img && git commit && git push` a partir de uma cópia completa da pasta.

## Editar produtos

Os textos dos produtos estão na lista `P` em `tools/build.py`. Para regenerar:

```bash
pip install pillow
python3 tools/build.py      # espera as fotos originais em ./assets/
```

(Também podes editar diretamente os ficheiros HTML em `site/`.)

## Ver localmente

```bash
python3 -m http.server 8080 -d site
# abre http://localhost:8080
```

## Publicar no Firebase Hosting

Projeto Firebase: **impressheart2026** (já configurado em `.firebaserc`).

```bash
npm install -g firebase-tools   # ou: npx firebase-tools
firebase login
firebase deploy --only hosting
```

O site fica disponível em https://impressheart2026.web.app (e https://impressheart2026.firebaseapp.com).
Para usar um domínio próprio: Firebase Console → Hosting → *Adicionar domínio personalizado*.

---
Feito com ❤️ — *Prints that touch the heart*
