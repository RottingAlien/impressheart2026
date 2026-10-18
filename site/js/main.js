document.addEventListener('DOMContentLoaded',()=>{
  const t=document.querySelector('.nav-toggle'),m=document.getElementById('menu');
  if(t&&m){t.addEventListener('click',()=>{const o=t.getAttribute('aria-expanded')==='true';t.setAttribute('aria-expanded',String(!o));m.classList.toggle('open',!o);});
    m.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>{t.setAttribute('aria-expanded','false');m.classList.remove('open');}));}
  const chips=document.querySelectorAll('.chip'),cards=document.querySelectorAll('#grelha .card');
  chips.forEach(c=>c.addEventListener('click',()=>{const f=c.dataset.filter;chips.forEach(x=>x.setAttribute('aria-pressed',String(x===c)));
    cards.forEach(card=>{card.hidden=!(f==='todos'||card.dataset.cat===f);});}));
  document.querySelectorAll('[data-year]').forEach(e=>e.textContent=new Date().getFullYear());
});
