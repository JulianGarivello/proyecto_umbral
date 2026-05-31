import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Proyecto Umbral",
    page_icon="\U0001f300",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
#MainMenu, header, footer,
[data-testid="stToolbar"],
[data-testid="stHeader"],
[data-testid="stSidebar"],
[data-testid="stDecoration"],
[data-testid="stStatusWidget"] { display: none !important; }
.block-container { padding: 0 !important; max-width: 100% !important; }
[data-testid="stMain"] > div { padding: 0 !important; }
html, body, [data-testid="stAppViewContainer"] {
    margin: 0 !important; padding: 0 !important;
    background: #08080C !important;
}
iframe { display: block; border: none; }
</style>
""", unsafe_allow_html=True)

HTML = """<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Proyecto Umbral</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;1,400&family=DM+Sans:wght@300;400;500&display=swap" rel="stylesheet">
<style>
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
:root{
  --bg:#08080C;--surface:rgba(18,18,26,0.82);--surface2:rgba(28,28,40,0.9);
  --border:rgba(255,255,255,0.09);--border-h:rgba(255,255,255,0.22);
  --text:#F0EEE8;--muted:rgba(240,238,232,0.52);--dim:rgba(240,238,232,0.28);
  --accent:#C8A96E;--r:16px;--rs:10px;
}
html,body{height:100%;overflow-x:hidden}
body{background:var(--bg);color:var(--text);font-family:'DM Sans',sans-serif;font-weight:300;min-height:100vh;display:flex;flex-direction:column}
#bgCanvas{position:fixed;inset:0;width:100%;height:100%;z-index:0;pointer-events:none}
.app{position:relative;z-index:1;display:flex;flex-direction:column;min-height:100vh}
header{padding:22px 48px;display:flex;align-items:center;justify-content:space-between;border-bottom:1px solid var(--border);backdrop-filter:blur(12px);background:rgba(8,8,12,0.5)}
.logo{font-family:'Playfair Display',serif;font-size:18px;letter-spacing:.04em}
.logo em{color:var(--accent);font-style:italic}
.htag{font-size:11px;letter-spacing:.14em;text-transform:uppercase;color:var(--dim);border:1px solid var(--border);padding:5px 14px;border-radius:99px}
.pw{padding:0 48px;margin-top:26px;margin-bottom:4px}
.pm{display:flex;justify-content:space-between;margin-bottom:8px;font-size:11px;letter-spacing:.1em;text-transform:uppercase;color:var(--dim)}
.pt{height:2px;background:var(--border);border-radius:99px;overflow:hidden}
.pf{height:100%;border-radius:99px;background:var(--accent);transition:width .5s cubic-bezier(.4,0,.2,1),background 1s}
.main{flex:1;display:flex;align-items:center;justify-content:center;padding:36px 48px}
.cnt{width:100%;max-width:780px}
.welcome{text-align:center;animation:fup .7s ease both}
.eb{font-size:11px;letter-spacing:.16em;text-transform:uppercase;color:var(--accent);margin-bottom:16px}
.welcome h1{font-family:'Playfair Display',serif;font-size:clamp(34px,6vw,58px);font-weight:400;line-height:1.12;margin-bottom:22px}
.welcome h1 em{color:var(--accent)}
.wintro{font-size:16px;color:var(--muted);line-height:1.9;max-width:560px;margin:0 auto 38px}
.ss{animation:fup .45s ease both}
.seb{font-size:11px;letter-spacing:.13em;text-transform:uppercase;color:var(--accent);margin-bottom:12px}
.sq{font-family:'Playfair Display',serif;font-size:clamp(22px,3.8vw,36px);font-weight:400;line-height:1.25;margin-bottom:30px}
.og{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-bottom:34px}
.opt{display:flex;align-items:center;gap:14px;padding:17px 18px;border-radius:var(--r);border:1px solid var(--border);background:var(--surface);cursor:pointer;text-align:left;transition:border-color .2s,background .2s,transform .15s;backdrop-filter:blur(10px)}
.opt:hover{border-color:var(--border-h);background:var(--surface2);transform:translateY(-1px)}
.opt.sel{border-color:var(--oc,var(--accent));background:var(--surface2)}
.oi{width:42px;height:42px;border-radius:9px;display:flex;align-items:center;justify-content:center;flex-shrink:0;font-size:21px;background:rgba(255,255,255,0.05)}
.ot{font-size:14px;font-weight:500;color:var(--text);flex:1;line-height:1.3}
.ock{width:20px;height:20px;border-radius:50%;border:1px solid var(--border);flex-shrink:0;display:flex;align-items:center;justify-content:center;transition:background .2s,border-color .2s}
.opt.sel .ock{background:var(--oc,var(--accent));border-color:var(--oc,var(--accent))}
/* Imagen step */
.oig{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-bottom:34px}
.oic{border-radius:var(--r);border:1px solid var(--border);background:var(--surface);cursor:pointer;overflow:hidden;transition:border-color .2s,transform .15s;backdrop-filter:blur(10px)}
.oic:hover{border-color:var(--border-h);transform:translateY(-2px)}
.oic.sel{border-color:var(--accent)}
.oicv{width:100%;height:136px;display:block}
.oil{padding:13px 15px;display:flex;align-items:center;gap:10px}
.oil .ot{flex:1}
/* Rueda */
.cww{display:flex;align-items:flex-start;justify-content:center;margin-bottom:34px;gap:24px;flex-wrap:wrap}
.cw-left{display:flex;flex-direction:column;align-items:center;gap:10px}
.cwi{position:relative;flex-shrink:0}
#wc{display:block;border-radius:50%}
/* zona de drop sobre la rueda — sin etiquetas dentro */
.drop-zone{position:absolute;inset:0;border-radius:50%;pointer-events:none}
/* columna de etiquetas a la derecha */
.cw-right{display:flex;flex-direction:column;justify-content:center;gap:10px;min-width:120px;padding-top:8px}
.el{font-family:'Playfair Display',serif;font-size:14px;font-weight:400;color:#F0EEE8;pointer-events:all;cursor:grab;user-select:none;padding:8px 14px;border-radius:8px;background:rgba(255,255,255,0.07);border:1px solid rgba(255,255,255,0.12);transition:background .2s,border-color .2s;white-space:nowrap;display:block;text-align:center;position:absolute}
.el:hover{background:rgba(255,255,255,0.13);border-color:rgba(255,255,255,0.25)}
.el.dragging{cursor:grabbing;z-index:100;background:rgba(255,255,255,0.18);border-color:rgba(255,255,255,0.4)}
.el.placed{border-color:rgba(255,255,255,0.35);background:rgba(0,0,0,0.5)}
.el-static{font-family:'Playfair Display',serif;font-size:14px;font-weight:400;color:#F0EEE8;pointer-events:all;cursor:grab;user-select:none;padding:8px 14px;border-radius:8px;background:rgba(255,255,255,0.07);border:1px solid rgba(255,255,255,0.12);transition:background .2s,border-color .2s,opacity .3s;white-space:nowrap;text-align:center}
.el-static:hover{background:rgba(255,255,255,0.13);border-color:rgba(255,255,255,0.25)}
.el-static.dragging-from{opacity:0.3}
.el-static.done{opacity:0.4;border-style:dashed}
.wi{font-size:12px;color:var(--muted);text-align:center;line-height:1.6;max-width:300px}
.pe{display:flex;flex-wrap:wrap;gap:8px;justify-content:center;min-height:28px}
.pp{font-size:12px;padding:4px 12px;border-radius:99px;border:1px solid rgba(255,255,255,.12);font-family:'DM Sans',sans-serif;transition:all .3s}
/* Free text */
.fiw{margin-bottom:34px}
.fi{width:100%;background:var(--surface);border:1px solid var(--border);border-radius:var(--rs);padding:18px 20px;font-family:'Playfair Display',serif;font-size:24px;color:var(--text);outline:none;transition:border-color .2s;backdrop-filter:blur(10px);letter-spacing:.02em}
.fi::placeholder{color:var(--dim);font-style:italic}
.fi:focus{border-color:var(--accent)}
.fih{font-size:12px;color:var(--dim);margin-top:8px;letter-spacing:.04em}
/* Nav */
.nr{display:flex;align-items:center;gap:12px}
.btn{display:inline-flex;align-items:center;gap:8px;padding:13px 28px;border-radius:var(--rs);font-family:'DM Sans',sans-serif;font-size:14px;font-weight:500;cursor:pointer;transition:all .2s;border:1px solid transparent;letter-spacing:.02em}
.bp{background:var(--accent);color:#08080C}
.bp:hover{background:#d4b87a;transform:translateY(-1px)}
.bp:disabled{opacity:.35;cursor:not-allowed;transform:none}
.bg{background:transparent;border-color:var(--border);color:var(--muted)}
.bg:hover{border-color:var(--border-h);color:var(--text);background:var(--surface2)}
.bo{background:transparent;border-color:var(--accent);color:var(--accent)}
.bo:hover{background:rgba(200,169,110,.12)}
/* Resultado */
.sr{animation:fup .7s ease both}
.rt{font-family:'Playfair Display',serif;font-size:clamp(30px,5vw,50px);font-weight:400;line-height:1.1;margin-bottom:6px}
.rs{font-size:14px;color:var(--muted);font-style:italic;margin-bottom:26px}
.rd{font-size:15px;color:var(--muted);line-height:1.85;border-left:2px solid var(--accent);padding:4px 0 4px 20px;font-style:italic;margin-bottom:30px}
.rcs{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-bottom:30px}
.rc{background:var(--surface);border:1px solid var(--border);border-radius:var(--r);padding:17px 19px;backdrop-filter:blur(10px)}
.rl{font-size:11px;letter-spacing:.1em;text-transform:uppercase;color:var(--dim);margin-bottom:11px}
.ps{display:flex;gap:8px;flex-wrap:wrap}
.sw{width:33px;height:33px;border-radius:8px;border:1px solid rgba(255,255,255,.08)}
.tr{display:flex;flex-wrap:wrap;gap:8px}
.tg{font-size:12px;padding:4px 12px;border-radius:99px;border:1px solid var(--border);color:var(--muted);background:rgba(255,255,255,.04)}
.sg{display:grid;grid-template-columns:1fr 1fr 1fr;gap:10px}
.si{background:rgba(255,255,255,.04);border:1px solid var(--border);border-radius:var(--rs);padding:12px 8px;font-size:12px;color:var(--muted);text-align:center;line-height:1.4}
footer{padding:16px 48px;border-top:1px solid var(--border);display:flex;align-items:center;justify-content:space-between;backdrop-filter:blur(12px);background:rgba(8,8,12,.4)}
footer span{font-size:11px;color:var(--dim)}
@keyframes fup{from{opacity:0;transform:translateY(20px)}to{opacity:1;transform:translateY(0)}}
@media(max-width:600px){
  header,.pw,.main,footer{padding-left:18px;padding-right:18px}
  .og,.oig,.rcs{grid-template-columns:1fr}
  .cwi{width:260px!important;height:260px!important}
  .sg{grid-template-columns:1fr}
  .welcome h1{font-size:28px}
}
</style>
</head>
<body>
<canvas id="bgCanvas"></canvas>
<div class="app">
  <header>
    <span class="logo">Proyecto <em>Umbral</em></span>
    <span class="htag">Experiencia análogo-virtual</span>
  </header>
  <div class="pw" id="pw" style="display:none">
    <div class="pm"><span>Tu recorrido</span><span id="pc">1 / 7</span></div>
    <div class="pt"><div class="pf" id="pf"></div></div>
  </div>
  <main class="main"><div class="cnt" id="cnt"></div></main>
  <footer>
    <span>Diseño centrado en el usuario · IA generativa</span>
    <span>Plutchik (1980) · Heller (2004) · Russell (1980)</span>
  </footer>
</div>

<script>
/* ── CANVAS BG ── */
const cv=document.getElementById('bgCanvas'),cx=cv.getContext('2d');
let W,H,frame=0,resultMode=false;
const MC=['#FFD60A','#FFA500','#FF4444','#CC0000','#00B4D8','#6B3FA0','#C0007A','#4A9BD4','#48CAE4','#FFEC6E','#FF6B35','#4A7C59','#F5E642','#9B6DC0','#E87D22','#2E6DA4'];

class P{
  constructor(){this.init()}
  init(){
    this.x=Math.random()*(W||innerWidth);
    this.y=Math.random()*(H||innerHeight);
    this.col=MC[Math.floor(Math.random()*MC.length)];
    this.targetCol=this.col;
    this.r=Math.random()*2.4+0.6;
    /* movimiento muy lento y aleatorio */
    this.vx=(Math.random()-.5)*0.4;
    this.vy=(Math.random()-.5)*0.4;
    /* titilación independiente */
    this.phase=Math.random()*Math.PI*2;
    this.speed=Math.random()*0.02+0.008;
    this.baseAlpha=Math.random()*0.55+0.2;
    /* transición de color al resultado */
    this.r0=0;this.g0=0;this.b0=0;
    this.r1=0;this.g1=0;this.b1=0;
    this.lerpT=1;
  }
  setTarget(hex){
    /* parsear color actual */
    const cur=this.col;
    this.r0=parseInt(cur.slice(1,3),16);this.g0=parseInt(cur.slice(3,5),16);this.b0=parseInt(cur.slice(5,7),16);
    this.r1=parseInt(hex.slice(1,3),16);this.g1=parseInt(hex.slice(3,5),16);this.b1=parseInt(hex.slice(5,7),16);
    this.lerpT=0;this.targetCol=hex;
  }
  update(){
    /* deriva suave — sin campo vectorial, solo deriva */
    this.x+=this.vx;this.y+=this.vy;
    /* rebotar en bordes */
    if(this.x<0){this.x=0;this.vx*=-1}
    if(this.x>W){this.x=W;this.vx*=-1}
    if(this.y<0){this.y=0;this.vy*=-1}
    if(this.y>H){this.y=H;this.vy*=-1}
    this.phase+=this.speed;
    /* interpolar color si hay transición activa */
    if(this.lerpT<1){
      this.lerpT=Math.min(1,this.lerpT+0.008);
      const t=this.lerpT;
      const r=Math.round(this.r0+(this.r1-this.r0)*t);
      const g=Math.round(this.g0+(this.g1-this.g0)*t);
      const b=Math.round(this.b0+(this.b1-this.b0)*t);
      this.col=`#${r.toString(16).padStart(2,'0')}${g.toString(16).padStart(2,'0')}${b.toString(16).padStart(2,'0')}`;
    }
  }
  draw(){
    const alpha=this.baseAlpha*(0.5+0.5*Math.sin(this.phase));
    cx.globalAlpha=alpha;
    cx.fillStyle=this.col;
    cx.beginPath();cx.arc(this.x,this.y,this.r,0,Math.PI*2);cx.fill();
  }
}

function resize(){W=cv.width=innerWidth;H=cv.height=innerHeight}
const parts=[];
function initP(){resize();for(let i=0;i<1800;i++)parts.push(new P())}
function animBg(){
  /* limpiar completamente — sin trail */
  cx.clearRect(0,0,W,H);
  cx.globalAlpha=1;
  for(const p of parts){p.update();p.draw()}
  requestAnimationFrame(animBg);
}
function setResPal(pal){
  /* asignar color destino a cada partícula y dejar que haga lerp */
  parts.forEach(p=>p.setTarget(pal[Math.floor(Math.random()*pal.length)]));
}
window.addEventListener('resize',resize);
initP();animBg();

/* ── CANVAS ESCENAS ── */
function drawScene(el,scene){
  const w=el.width=el.offsetWidth||320,h=el.height=136,c=el.getContext('2d');
  if(scene==='storm'){
    const g=c.createLinearGradient(0,0,0,h);g.addColorStop(0,'#080f1e');g.addColorStop(1,'#1a3a5c');
    c.fillStyle=g;c.fillRect(0,0,w,h);
    c.strokeStyle='rgba(91,141,184,0.35)';c.lineWidth=1.1;
    for(let y=8;y<h;y+=13){c.beginPath();for(let x=0;x<w;x+=3){const yy=y+Math.sin(x*.08+y*.1)*6+Math.sin(x*.03)*9;x===0?c.moveTo(x,yy):c.lineTo(x,yy)}c.stroke()}
    c.strokeStyle='rgba(180,200,255,0.7)';c.lineWidth=1.5;
    [[w*.58,0,w*.54,36],[w*.6,36,w*.56,66]].forEach(([x1,y1,x2,y2])=>{c.beginPath();c.moveTo(x1,y1);c.lineTo(x2,y2);c.stroke()});
    c.strokeStyle='rgba(140,170,210,0.25)';c.lineWidth=0.8;
    for(let i=0;i<60;i++){const rx=Math.random()*w,ry=Math.random()*h;c.beginPath();c.moveTo(rx,ry);c.lineTo(rx-2,ry+8);c.stroke()}
  } else if(scene==='rain'){
    const g=c.createLinearGradient(0,0,0,h);g.addColorStop(0,'#16162a');g.addColorStop(1,'#24243a');
    c.fillStyle=g;c.fillRect(0,0,w,h);
    c.fillStyle='rgba(72,72,96,0.5)';
    [[w*.2,14,100,18],[w*.6,7,118,16],[w*.42,24,88,15]].forEach(([cx2,cy2,ew,eh])=>{c.beginPath();c.ellipse(cx2,cy2,ew,eh,0,0,Math.PI*2);c.fill()});
    c.strokeStyle='rgba(170,182,205,0.22)';c.lineWidth=0.9;
    for(let i=0;i<130;i++){const rx=Math.random()*w,ry=Math.random()*h;c.beginPath();c.moveTo(rx,ry);c.lineTo(rx-1,ry+10);c.stroke()}
  } else if(scene==='wind'){
    const g=c.createLinearGradient(0,0,w,h);g.addColorStop(0,'#182818');g.addColorStop(.5,'#284a38');g.addColorStop(1,'#4a8a5a');
    c.fillStyle=g;c.fillRect(0,0,w,h);
    c.strokeStyle='rgba(190,225,195,0.28)';c.lineWidth=1.2;
    for(let i=0;i<10;i++){const yy=(h/10)*i+h/20;c.beginPath();c.moveTo(0,yy);c.bezierCurveTo(w*.3,yy-15+Math.random()*28,w*.7,yy+15-Math.random()*28,w,yy+Math.random()*10-5);c.stroke()}
    c.fillStyle='rgba(90,190,110,0.45)';
    for(let i=0;i<22;i++){const lx=Math.random()*w,ly=Math.random()*h;c.save();c.translate(lx,ly);c.rotate(Math.random()*Math.PI*2);c.beginPath();c.ellipse(0,0,4,2,0,0,Math.PI*2);c.fill();c.restore()}
  } else if(scene==='dawn'){
    const g=c.createLinearGradient(0,0,0,h);g.addColorStop(0,'#08081e');g.addColorStop(.45,'#38185a');g.addColorStop(.8,'#b85a18');g.addColorStop(1,'#e09830');
    c.fillStyle=g;c.fillRect(0,0,w,h);
    const sg=c.createRadialGradient(w/2,h,0,w/2,h,82);sg.addColorStop(0,'rgba(255,215,90,0.9)');sg.addColorStop(.4,'rgba(255,155,45,0.5)');sg.addColorStop(1,'rgba(255,90,18,0)');
    c.fillStyle=sg;c.beginPath();c.arc(w/2,h,82,0,Math.PI*2);c.fill();
    c.strokeStyle='rgba(255,175,75,0.18)';c.lineWidth=1;
    for(let y=h*.76;y<h;y+=8){c.beginPath();for(let x=0;x<w;x+=4){const yy=y+Math.sin(x*.05)*2;x===0?c.moveTo(x,yy):c.lineTo(x,yy)}c.stroke()}
  }
}

/* ── RUEDA ── */
const EW=['Alegría','Tristeza','Ira','Miedo','Asco','Sorpresa'];
let dragging=null,dOff={x:0,y:0},placed={},dragSource=null;

/* Ghost element que sigue al cursor durante el drag */
let ghost=null;

function hsl2rgb(h,s,l){let r,g,b;if(!s){r=g=b=l}else{const q=l<.5?l*(1+s):l+s-l*s,p=2*l-q;r=h2rgb(p,q,h+1/3);g=h2rgb(p,q,h);b=h2rgb(p,q,h-1/3)}return[Math.round(r*255),Math.round(g*255),Math.round(b*255)]}
function h2rgb(p,q,t){if(t<0)t+=1;if(t>1)t-=1;if(t<1/6)return p+(q-p)*6*t;if(t<.5)return q;if(t<2/3)return p+(q-p)*(2/3-t)*6;return p}

function drawWheel(el){
  const sz=el.width=el.height=el.offsetWidth||300;
  const ctx=el.getContext('2d'),cxw=sz/2,cyw=sz/2,rad=sz/2-1;
  const img=ctx.createImageData(sz,sz);
  for(let y=0;y<sz;y++)for(let x=0;x<sz;x++){
    const dx=x-cxw,dy=y-cyw,d=Math.sqrt(dx*dx+dy*dy);
    if(d>rad){img.data[(y*sz+x)*4+3]=0;continue}
    const ang=((Math.atan2(dy,dx)*180/Math.PI)+360)%360;
    const sat=d/rad;
    const[r,g,b]=hsl2rgb(ang/360,sat,.5);
    const i=(y*sz+x)*4;img.data[i]=r;img.data[i+1]=g;img.data[i+2]=b;img.data[i+3]=255;
  }
  ctx.putImageData(img,0,0);
  ctx.beginPath();ctx.arc(cxw,cyw,rad,0,Math.PI*2);ctx.strokeStyle='rgba(255,255,255,0.1)';ctx.lineWidth=1.5;ctx.stroke();
}

function createGhost(name,x,y){
  if(ghost)ghost.remove();
  ghost=document.createElement('div');
  ghost.className='el dragging';
  ghost.textContent=name;
  ghost.style.cssText=`position:fixed;left:${x}px;top:${y}px;z-index:1000;pointer-events:none;transform:translate(-50%,-50%);`;
  document.body.appendChild(ghost);
}

function setupDrag(wheelEl){
  /* drag desde la columna de etiquetas estáticas */
  document.querySelectorAll('.el-static').forEach(el=>{
    el.addEventListener('mousedown',e=>{
      const name=el.dataset.name;
      if(placed[name])return; /* ya colocada */
      dragSource=el;
      el.classList.add('dragging-from');
      createGhost(name,e.clientX,e.clientY);
      e.preventDefault();
    });
    el.addEventListener('touchstart',e=>{
      const name=el.dataset.name;
      if(placed[name])return;
      dragSource=el;
      el.classList.add('dragging-from');
      createGhost(name,e.touches[0].clientX,e.touches[0].clientY);
    },{passive:true});
  });

  document.addEventListener('mousemove',e=>{
    if(!ghost)return;
    ghost.style.left=e.clientX+'px';ghost.style.top=e.clientY+'px';
  });
  document.addEventListener('touchmove',e=>{
    if(!ghost)return;
    ghost.style.left=e.touches[0].clientX+'px';ghost.style.top=e.touches[0].clientY+'px';
  },{passive:true});

  document.addEventListener('mouseup',e=>endDrop(e.clientX,e.clientY,wheelEl));
  document.addEventListener('touchend',e=>{
    if(e.changedTouches.length)endDrop(e.changedTouches[0].clientX,e.changedTouches[0].clientY,wheelEl);
  });
}

function endDrop(clientX,clientY,wheelEl){
  if(!ghost||!dragSource){ghost&&ghost.remove();ghost=null;return}
  const name=dragSource.dataset.name;
  dragSource.classList.remove('dragging-from');

  /* ¿soltó sobre la rueda? */
  const wr=wheelEl.getBoundingClientRect();
  const dx=clientX-wr.left-wr.width/2;
  const dy=clientY-wr.top-wr.height/2;
  const dist=Math.sqrt(dx*dx+dy*dy);
  const rad=wr.width/2;

  if(dist<=rad){
    /* obtener color en ese punto */
    const ang=((Math.atan2(dy,dx)*180/Math.PI)+360)%360;
    const sat=Math.min(dist/rad,1);
    const[r,g,b]=hsl2rgb(ang/360,sat,.5);
    const hex=`#${r.toString(16).padStart(2,'0')}${g.toString(16).padStart(2,'0')}${b.toString(16).padStart(2,'0')}`;
    placed[name]={hex};
    /* marcar la etiqueta estática como colocada */
    const srcEl=document.querySelector(`.el-static[data-name="${name}"]`);
    if(srcEl){srcEl.classList.add('done');srcEl.style.borderColor=hex+'88';srcEl.style.color=hex;}
    updatePE();
  }

  ghost.remove();ghost=null;dragSource=null;
}

function updatePE(){
  const el=document.getElementById('pe');if(!el)return;
  el.innerHTML='';
  Object.entries(placed).forEach(([n,{hex}])=>{
    const p=document.createElement('span');p.className='pp';p.textContent=n;
    p.style.background=hex+'22';p.style.borderColor=hex+'66';p.style.color=hex;
    el.appendChild(p);
  });
}

/* ── DATOS ── */
const STEPS=[
  {ey:'Paso 1 de 7 — Punto de partida',q:'¿Cómo llegaste hoy a este espacio?',col:'#5B8DB8',
   opts:[{i:'☀️',l:'Con energía y buena disposición'},{i:'☁️',l:'Tranquilo/a pero sin mucha energía'},{i:'🌧️',l:'Con algo pesado en la cabeza'},{i:'❓',l:'No sé muy bien cómo estoy'}]},
  {ey:'Paso 2 de 7 — Señales del cuerpo',q:'¿Cómo sientes tu cuerpo en este momento?',col:'#6B3FA0',
   opts:[{i:'⚡',l:'Tenso/a o agitado/a'},{i:'🍃',l:'Relajado/a y liviano/a'},{i:'🏋️',l:'Pesado/a o cansado/a'},{i:'🌊',l:'Con mariposas o inquietud'}]},
  {ey:'Paso 3 de 7 — Tu mente ahora',q:'¿Qué tipo de pensamientos rondan tu cabeza hoy?',col:'#2E6DA4',
   opts:[{i:'🔁',l:'Pensamientos que se repiten'},{i:'🔭',l:'Anticipando algo que viene'},{i:'🌫️',l:'La mente en blanco o dispersa'},{i:'🌤️',l:'Pensamientos positivos y claros'}]},
  {ey:'Paso 4 de 7 — Lo que necesitas',q:'¿Qué necesitas que este espacio te dé?',col:'#4A7C59',
   opts:[{i:'🔥',l:'Liberarme y desahogarme'},{i:'🌙',l:'Calmarme y encontrar paz'},{i:'⭐',l:'Celebrar y sentir alegría'},{i:'👁️',l:'Reflexionar y entenderme'}]},
  {ey:'Paso 5 de 7 — Imagen interior',q:'¿Cuál de estas escenas se acerca más a tu estado emocional?',col:'#D15F00',type:'image',
   opts:[{sc:'storm',i:'⛈️',l:'Un lago en tormenta'},{sc:'wind',i:'💨',l:'Viento que despeja'},{sc:'rain',i:'🌧️',l:'Lluvia constante y gris'},{sc:'dawn',i:'🌅',l:'Un amanecer tranquilo'}]},
  {ey:'Paso 6 de 7 — Círculo cromático',q:'Arrastra cada emoción al color que sientas que le corresponde',col:'#C8A96E',type:'wheel'},
  {ey:'Paso 7 de 7 — Tu palabra',q:'¿Qué palabra resume lo que sientes ahora mismo?',col:'#993556',type:'free'},
];
const EMAP={'00':'alegria','01':'serenidad','02':'melancolia','03':'reflexion','10':'asombro','11':'serenidad','12':'ira','13':'miedo','20':'ira','21':'miedo','22':'melancolia','23':'reflexion','30':'reflexion','31':'serenidad','32':'melancolia','33':'asombro'};
const EMOTS={
  alegria:{name:'Alegría expansiva',sec:'Emoción secundaria: euforia · júbilo',desc:'Hay una energía luminosa que quiere moverse y expresarse. El salón responderá con composiciones visuales dinámicas y ritmos que amplifican esa vitalidad que traes contigo.',pal:['#FFD60A','#FFA520','#FFEC6E','#2D4A8A','#D4A017'],tags:['Luz intensa','Movimiento rápido','Ritmos festivos','Colores vivos'],stim:['Proyecciones luminosas cálidas','Composición musical en mayor','Visuales abstractos de explosión'],col:'#D4A017'},
  serenidad:{name:'Serenidad',sec:'Emoción secundaria: paz · calma',desc:'Un estado de equilibrio y apertura suave. El salón creará un entorno de quietud contemplativa con tonos fríos y movimientos lentos que invitan a la presencia plena.',pal:['#ADE8F4','#48CAE4','#4A7C59','#B8C8D8','#E8F4EC'],tags:['Luz difusa','Movimiento lento','Sonidos ambiente','Ondas suaves'],stim:['Proyecciones de agua o niebla','Música ambiental minimalista','Luces tenues fluctuantes'],col:'#4A7C59'},
  melancolia:{name:'Melancolía',sec:'Emoción secundaria: tristeza · nostalgia',desc:'Una emoción que merece ser vista y sostenida, no evitada. El salón acompañará ese estado con visuales contemplativos y tonos que permiten sentir sin juzgar.',pal:['#1A3A5C','#5C4A7A','#7BAFD4','#B8C8D8','#3D3D4A'],tags:['Luz tenue','Movimiento muy lento','Sonidos graves','Silencios'],stim:['Proyecciones de lluvia abstracta','Música en menor','Degradados lentos'],col:'#7BAFD4'},
  anticipacion:{name:'Anticipación',sec:'Emoción secundaria: esperanza · expectativa',desc:'Algo está por suceder y lo sientes en el cuerpo. El salón traducirá esa tensión hacia adelante en composiciones que acompañan tu movimiento interno.',pal:['#E87D22','#F5E642','#F5CBA7','#C0392B','#D15F00'],tags:['Luz en crescendo','Transiciones dinámicas','Ritmos de expansión','Naranjas y amarillos'],stim:['Visuales en espiral expansiva','Música con crescendo','Destellos cálidos'],col:'#E87D22'},
  ira:{name:'Ira o frustración',sec:'Emoción secundaria: rabia · indignación',desc:'Una energía que pide salida y reconocimiento. El salón la acompaña con intensidad visual para que puedas sentirla sin reprimirla, como primer paso hacia el alivio.',pal:['#CC0000','#8B0000','#FF6B35','#1C1C1C','#E63946'],tags:['Contraste extremo','Movimiento brusco','Percusión intensa','Rojos y negros'],stim:['Proyecciones angulares en rojo','Percusión y bajo profundo','Contrastes lumínicos bruscos'],col:'#E63946'},
  miedo:{name:'Miedo o angustia',sec:'Emoción secundaria: inquietud · ansiedad',desc:'Una emoción que prefiere la oscuridad pero necesita luz. El salón sostendrá ese estado acompañando la incomodidad con calma progresiva.',pal:['#1A0030','#6B3FA0','#3D5A3E','#4A4A4A','#9B6DC0'],tags:['Luz fragmentada','Silencios sostenidos','Movimiento que se calma','Violetas y grises'],stim:['Proyecciones de partículas','Drones sonoros graves','Luces que se estabilizan'],col:'#9B6DC0'},
  reflexion:{name:'Reflexión',sec:'Emoción secundaria: introspección · contemplación',desc:'Un estado de escucha interna que pide espacio. El salón se convertirá en un espejo visual que acompaña el pensamiento sin interrumpirlo.',pal:['#1A73C0','#4A9BD4','#4A7C59','#B89A3E','#0A4F8C'],tags:['Luz difusa','Movimiento sutil','Tonos medios','Geometrías lentas'],stim:['Formas geométricas que evolucionan','Música ambiental con piano','Luces azules en transición'],col:'#4A9BD4'},
  asombro:{name:'Asombro',sec:'Emoción secundaria: sorpresa · maravilla',desc:'Una apertura repentina hacia algo más grande que uno mismo. El salón responderá con composiciones que expanden la percepción y rompen lo esperado.',pal:['#00B4D8','#C0007A','#48CAE4','#0077A8','#F0F8FF'],tags:['Luz pulsante','Contrastes opuestos','Cambios inesperados','Patrones fractales'],stim:['Proyecciones fractales','Música con arpegios ascendentes','Destellos de luz que sorprenden'],col:'#00B4D8'},
};

/* ── ESTADO ── */
let scr='welcome',stp=0,ans={},fw='';
const chk='<svg viewBox="0 0 10 10" fill="none" stroke="white" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" width="10" height="10"><polyline points="2 5 4.5 7.5 8 3"/></svg>';

/* ── RENDER ── */
function render(){
  const cnt=document.getElementById('cnt'),pw=document.getElementById('pw'),pf=document.getElementById('pf'),pc=document.getElementById('pc');
  if(scr==='welcome'){
    pw.style.display='none';
    cnt.innerHTML=`<div class="welcome"><div class="eb">Experiencia análogo-virtual · 2025</div><h1>¿Qué emoción<br>llevas <em>dentro</em> hoy?</h1><p class="wintro">Estás a punto de ingresar a una experiencia inmersiva de luces, colores y sonidos que conectarán con tus emociones. Responde las siguientes preguntas con el fin de analizar tu estado emocional actual. No hay respuestas correctas ni incorrectas. Elige la que más resuene en tu ser.</p><button class="btn bp" onclick="go()">Comenzar experiencia →</button></div>`;
    return;
  }
  if(scr==='result'){
    pw.style.display='block';pf.style.width='100%';pf.style.background='#C8A96E';pc.textContent='Completo';
    const k=getKey(),em=EMOTS[k];setResPal(em.pal);
    const sw=em.pal.map(c=>`<div class="sw" style="background:${c}"></div>`).join('');
    const tg=em.tags.map(t=>`<span class="tg">${t}</span>`).join('');
    const st=em.stim.map(s=>`<div class="si">${s}</div>`).join('');
    const wd=fw?`<div class="rc" style="grid-column:1/-1"><div class="rl">Tu palabra</div><p style="font-family:'Playfair Display',serif;font-size:28px;color:${em.col};margin:0">${fw}</p></div>`:'';
    cnt.innerHTML=`<div class="sr"><div class="eb">Tu experiencia emocional</div><h2 class="rt" style="color:${em.col}">${em.name}</h2><p class="rs">${em.sec}</p><p class="rd">${em.desc}</p><div class="rcs"><div class="rc"><div class="rl">Paleta del salón</div><div class="ps">${sw}</div></div><div class="rc"><div class="rl">Parámetros visuales</div><div class="tr">${tg}</div></div>${wd}<div class="rc" style="grid-column:1/-1"><div class="rl">Estímulos activados</div><div class="sg">${st}</div></div></div><button class="btn bo" onclick="restart()">↺ Nueva experiencia</button></div>`;
    return;
  }
  // survey
  const s=STEPS[stp],tot=STEPS.length;
  pw.style.display='block';pf.style.width=Math.round((stp+1)/tot*100)+'%';pf.style.background=s.col;pc.textContent=`${stp+1} / ${tot}`;
  let body='';
  if(s.type==='image'){
    body=`<div class="oig">${s.opts.map((o,i)=>`<div class="oic ${ans[stp]===i?'sel':''}" onclick="selOpt(${i})"><canvas class="oicv" id="sc_${i}" width="320" height="136"></canvas><div class="oil"><span style="font-size:20px">${o.i}</span><span class="ot">${o.l}</span><div class="ock" style="${ans[stp]===i?`background:${s.col};border-color:${s.col}`:''}">${ans[stp]===i?chk:''}</div></div></div>`).join('')}</div>`;
  } else if(s.type==='wheel'){
    const wsz=Math.min(300,innerWidth-200);
    const shuffled=[...EW].sort(()=>Math.random()-.5);
    const labels=shuffled.map(n=>`<span class="el-static ${placed[n]?'done':''}" data-name="${n}" style="${placed[n]?`border-color:${placed[n].hex}88;color:${placed[n].hex}`:''}">  ${n}</span>`).join('');
    body=`<div class="cww"><div class="cw-left"><div class="cwi" id="cwi" style="width:${wsz}px;height:${wsz}px"><canvas id="wc" width="${wsz}" height="${wsz}" style="width:${wsz}px;height:${wsz}px;border-radius:50%"></canvas></div><p class="wi">Arrastra cada palabra hacia el color que sientas que le corresponde</p></div><div class="cw-right" id="cwRight">${labels}</div></div><div class="pe" id="pe" style="margin-bottom:20px"></div>`; 
  } else if(s.type==='free'){
    body=`<div class="fiw"><input class="fi" id="fi" type="text" placeholder="Escribe una palabra…" value="${fw}" oninput="fw=this.value" maxlength="40" autocomplete="off" spellcheck="false"><p class="fih">Una sola palabra que capture lo que estás sintiendo ahora mismo</p></div>`;
  } else {
    body=`<div class="og">${s.opts.map((o,i)=>`<button class="opt ${ans[stp]===i?'sel':''}" style="--oc:${s.col}" onclick="selOpt(${i})"><div class="oi">${o.i}</div><span class="ot">${o.l}</span><div class="ock">${ans[stp]===i?chk:''}</div></button>`).join('')}</div>`;
  }
  const canN=s.type==='wheel'||s.type==='free'?true:ans[stp]!==undefined;
  cnt.innerHTML=`<div class="ss"><p class="seb">${s.ey}</p><h2 class="sq">${s.q}</h2>${body}<div class="nr">${stp>0?`<button class="btn bg" onclick="back()">← Anterior</button>`:''}<button class="btn bp" onclick="nxt()" ${canN?'':'disabled'}>${stp===STEPS.length-1?'Ver mi experiencia →':'Continuar →'}</button></div></div>`;
  // post-render
  if(s.type==='image'){s.opts.forEach((o,i)=>{const c=document.getElementById(`sc_${i}`);if(c)requestAnimationFrame(()=>{c.width=c.offsetWidth||320;drawScene(c,o.sc)})})}
  if(s.type==='wheel'){const wc=document.getElementById('wc');if(wc)requestAnimationFrame(()=>drawWheel(wc));const cwi=document.getElementById('cwi');if(cwi)setupDrag(cwi);setTimeout(updatePE,50)}
  if(s.type==='free'){const fi=document.getElementById('fi');if(fi)setTimeout(()=>fi.focus(),80)}
}

function getKey(){const a0=ans[0]??0,a3=ans[3]??0;return EMAP[`${Math.min(a0,3)}${Math.min(a3,3)}`]||'reflexion'}
function go(){scr='survey';stp=0;render()}
function back(){if(stp>0){stp--;render()}}
function nxt(){if(stp<STEPS.length-1){stp++;render()}else{scr='result';render()}}
function selOpt(i){ans[stp]=i;render()}
function restart(){scr='welcome';stp=0;ans={};fw='';placed={};ghost&&ghost.remove();ghost=null;dragSource=null;parts.forEach(p=>{p.col=MC[Math.floor(Math.random()*MC.length)];p.lerpT=1;p.targetCol=p.col;});render()}

render();
</script>
</body>
</html>
"""

components.html(HTML, height=820, scrolling=True)
