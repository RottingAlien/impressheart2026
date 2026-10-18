const {chromium}=require('playwright');const fs=require('fs');
(async()=>{const b=await chromium.launch();const base='http://localhost:8765/';
 // favicons
 const fp=await b.newPage();for(const [s,n] of [[32,'favicon-32.png'],[180,'apple-touch-icon.png']]){await fp.setViewportSize({width:s,height:s});await fp.setContent(`<style>body{margin:0}</style><img src="${base}img/favicon.svg" width=${s} height=${s}>`);await fp.waitForTimeout(300);await fp.screenshot({path:'site/img/'+n,omitBackground:true});}
 const seen=new Set(),queue=['index.html'],bad=[];const ctx=await b.newContext();const p=await ctx.newPage();
 p.on('response',r=>{if(r.status()>=400)bad.push(r.status()+' '+r.url())});
 while(queue.length){const u=queue.shift();if(seen.has(u))continue;seen.add(u);await p.goto(base+u,{waitUntil:'networkidle'});
  const info=await p.evaluate(()=>({links:[...document.querySelectorAll('a[href]')].map(a=>a.href),imgs:[...document.images].filter(i=>!i.complete||i.naturalWidth==0).map(i=>i.currentSrc||i.src),price:/€|preço|price/i.test(document.body.innerText)}));
  if(info.imgs.length)bad.push('broken img on '+u+': '+info.imgs);if(info.price)bad.push('price word on '+u);
  for(const l of info.links){if(l.startsWith(base)){const path=l.slice(base.length).split('#')[0]||'index.html';if(path.endsWith('.html')&&!seen.has(path))queue.push(path);else if(!path.endsWith('.html')){const r=await ctx.request.get(l);if(r.status()>=400)bad.push(r.status()+' '+l)}}}}
 console.log('pages',seen.size,[...seen].join(' '));console.log('BAD',bad);
 const shot=async(vp,u,f,full=true)=>{const c=await b.newContext({viewport:vp,deviceScaleFactor:vp.width<500?2:1});const q=await c.newPage();await q.goto(base+u,{waitUntil:'networkidle'});await q.evaluate(()=>document.querySelectorAll('img[loading=lazy]').forEach(i=>i.loading='eager'));await q.waitForTimeout(1200);await q.screenshot({path:'screenshots/'+f,fullPage:full});await c.close()};
 await shot({width:1440,height:900},'index.html','home-desktop.png');await shot({width:1440,height:900},'index.html','home-desktop-fold.png',false);
 await shot({width:390,height:844},'index.html','home-mobile.png');await shot({width:390,height:844},'index.html','home-mobile-fold.png',false);
 await shot({width:1440,height:900},'produtos/candeeiro-led-coracao-foto.html','produto-desktop.png');await shot({width:390,height:844},'produtos/caneca-mocho-feiticeiro.html','produto-mobile.png',false);
 await shot({width:1440,height:900},'contacto.html','contacto-desktop.png');await shot({width:1440,height:900},'sobre.html','sobre-desktop.png');
 await b.close()})();
