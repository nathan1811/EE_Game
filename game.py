"""
Closet Consumerism + Fashion Tycoon + Save The Earth
Streamlit wrapper — embeds the full game as an HTML component.

To run locally:
    pip install streamlit
    streamlit run app.py

To deploy:
    Push to GitHub, then deploy on Streamlit Community Cloud (share.streamlit.io)
    or any platform that supports Streamlit (Railway, Render, Hugging Face Spaces, etc.)
"""

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Closet Consumerism + Fashion Tycoon + Save The Earth",
    page_icon="👗",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Hide Streamlit's default chrome so the game fills the viewport
st.markdown(
    """
    <style>
        /* Remove all Streamlit padding / header / footer */
        #root > div:first-child { height: 100vh; }
        .stApp { background: #080808; }
        header[data-testid="stHeader"] { display: none !important; }
        footer { display: none !important; }
        .block-container {
            padding: 0 !important;
            max-width: 100% !important;
        }
        /* Hide the vertical scroll-bar Streamlit sometimes adds */
        html, body { overflow: hidden; }
    </style>
    """,
    unsafe_allow_html=True,
)

GAME_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Closet Consumerism + Fashion Tycoon + Save The Earth</title>
<link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400&family=DM+Mono:wght@300;400;500&display=swap" rel="stylesheet">
<style>
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
:root{
  --bg:#080808;--deep:#0d0d0d;--surface:#161616;--card:#1e1e1e;
  --border:#2c2c2c;--border2:#3a3a3a;--smoke:#555;--ash:#888;
  --silver:#bbb;--cream:#f0ebe3;--gold:#c9a96e;--gold2:#e8c98a;
  --red:#e63946;--red-bg:#1a0608;--red-dim:#7a1a20;
  --green:#52b26a;--green-bg:#061208;--green-dim:#1a4a28;
  --amber:#e8a020;--blue:#4a9eff;--purple:#a855f7;
  --teal:#2ec4b6;--teal-dark:#1a7a73;
}
html,body{height:100%}
body{background:var(--bg);color:var(--cream);font-family:'DM Mono',monospace;overflow:hidden}
#bgCanvas{position:fixed;inset:0;z-index:0;pointer-events:none}

.screen{position:fixed;inset:0;z-index:10;opacity:0;pointer-events:none;transition:opacity .3s ease;overflow-y:auto}
.screen.active{opacity:1;pointer-events:all}
#s-splash{display:flex;flex-direction:column;align-items:center;justify-content:center;background:var(--bg);text-align:center;padding:40px}
#s-intro{display:flex;align-items:center;justify-content:center;background:var(--bg);padding:30px 20px;min-height:100%}
#s-game.active{display:flex!important;flex-direction:column}
#s-end{display:flex;align-items:flex-start;justify-content:center;background:var(--bg);padding:40px 20px;min-height:100%}
#s-end.active{display:flex!important}
#s-tycoon-intro{display:flex;align-items:center;justify-content:center;background:var(--bg);padding:30px 20px;min-height:100%}
#s-tycoon.active{display:flex!important;flex-direction:column}
#s-tycoon-end{display:flex;align-items:flex-start;justify-content:center;background:var(--bg);padding:40px 20px;min-height:100%}
#s-tycoon-end.active{display:flex!important}
#s-earth-ask{display:flex;align-items:center;justify-content:center;background:var(--bg);padding:30px 20px;min-height:100%}
#s-earth.active{display:block}
#s-earth-end{display:flex;align-items:center;justify-content:center;background:var(--bg);padding:40px 20px;min-height:100%}
#s-earth-end.active{display:flex!important}

/* SPLASH */
.splash-logo{font-family:'Bebas Neue',sans-serif;font-size:clamp(3.5rem,12vw,9.5rem);line-height:.88;letter-spacing:2px}
.splash-logo .ol{-webkit-text-stroke:1.5px var(--border2);color:transparent}
.splash-sub{font-family:'Cormorant Garamond',serif;font-style:italic;font-size:1rem;color:var(--ash);letter-spacing:6px;text-transform:uppercase;margin-top:18px}
.splash-btn{margin-top:48px;background:transparent;border:1px solid var(--border2);color:var(--ash);font-family:'DM Mono',monospace;font-size:.68rem;letter-spacing:4px;text-transform:uppercase;padding:14px 52px;cursor:pointer;transition:all .3s;position:relative;overflow:hidden}
.splash-btn::after{content:'';position:absolute;inset:0;background:var(--gold);transform:translateX(-100%);transition:transform .4s cubic-bezier(.16,1,.3,1);z-index:-1}
.splash-btn:hover{color:var(--bg);border-color:var(--gold)}
.splash-btn:hover::after{transform:translateX(0)}
.splash-version{margin-top:16px;font-size:.55rem;letter-spacing:3px;color:var(--smoke)}

/* INTRO */
.intro-wrap{display:grid;grid-template-columns:1fr 1fr;max-width:920px;width:100%;border:1px solid var(--border)}
@media(max-width:620px){.intro-wrap{grid-template-columns:1fr}}
.intro-l{padding:48px 40px;border-right:1px solid var(--border)}
.intro-r{padding:40px 32px;background:var(--deep);display:flex;flex-direction:column;gap:0}
.eyebrow{font-size:.58rem;letter-spacing:5px;text-transform:uppercase;color:var(--gold);margin-bottom:14px}
.intro-h{font-family:'Bebas Neue',sans-serif;font-size:clamp(2.6rem,5vw,4.2rem);line-height:.9;margin-bottom:18px}
.intro-h span{color:var(--gold);display:block}
.intro-body{font-family:'Cormorant Garamond',serif;font-size:1rem;line-height:1.9;color:var(--silver);margin-bottom:28px}
.diff-label{font-size:.58rem;letter-spacing:4px;text-transform:uppercase;color:var(--smoke);margin-bottom:12px;padding-bottom:10px;border-bottom:1px solid var(--border)}
.diff-btns{display:flex;gap:8px;margin-bottom:28px;flex-wrap:wrap}
.diff-btn{flex:1;min-width:80px;padding:10px 8px;background:var(--surface);border:1px solid var(--border);color:var(--ash);font-family:'DM Mono',monospace;font-size:.62rem;letter-spacing:2px;text-transform:uppercase;cursor:pointer;transition:all .2s;text-align:center}
.diff-btn:hover{border-color:var(--border2);color:var(--cream)}
.diff-btn.active{border-color:var(--gold);color:var(--gold);background:#1a1408}
.diff-btn .diff-sub{display:block;font-size:.5rem;color:var(--smoke);margin-top:3px;letter-spacing:1px}
.diff-btn.active .diff-sub{color:var(--gold);opacity:.7}
.intro-btns{display:flex;gap:10px;flex-wrap:wrap}
.rt{font-size:.58rem;letter-spacing:4px;text-transform:uppercase;color:var(--smoke);padding-bottom:12px;border-bottom:1px solid var(--border);margin-bottom:4px}
.rule-r{display:flex;gap:12px;align-items:flex-start;padding:12px 0;border-bottom:1px solid var(--border)}
.rule-r:last-of-type{border:none}
.ri{font-size:1.2rem;width:30px;text-align:center;flex-shrink:0}
.rule-r b{display:block;font-size:.64rem;letter-spacing:2px;text-transform:uppercase;color:var(--cream);margin-bottom:3px}
.rule-r span{font-size:.7rem;color:var(--ash);line-height:1.5}
.score-t{margin-top:20px}
.sc-row{display:flex;justify-content:space-between;align-items:center;padding:8px 0;border-bottom:1px solid var(--border);font-size:.7rem;color:var(--ash)}
.sc-row:last-child{border:none}
.pill{font-size:.62rem;padding:3px 9px;border-radius:2px;font-weight:600;letter-spacing:1px}
.pill.neg{background:var(--red-dim);color:#f5a0a5}
.pill.pos{background:var(--green-dim);color:#9fe8b0}
.pill.gld{background:#2a1e08;color:var(--gold2)}
.pill.teal{background:var(--teal-dark);color:#a0f0eb}

/* SHARED BUTTONS */
.btn-gold{background:var(--gold);border:none;color:var(--bg);font-family:'DM Mono',monospace;font-size:.63rem;letter-spacing:3px;text-transform:uppercase;padding:12px 30px;cursor:pointer;font-weight:600;transition:all .2s}
.btn-gold:hover{background:var(--gold2);transform:translateY(-2px)}
.btn-ghost{background:transparent;border:1px solid var(--border);color:var(--ash);font-family:'DM Mono',monospace;font-size:.6rem;letter-spacing:3px;text-transform:uppercase;padding:12px 22px;cursor:pointer;transition:all .2s}
.btn-ghost:hover{border-color:var(--border2);color:var(--cream)}
.btn-teal{background:var(--teal);border:none;color:var(--bg);font-family:'DM Mono',monospace;font-size:.63rem;letter-spacing:3px;text-transform:uppercase;padding:12px 30px;cursor:pointer;font-weight:600;transition:all .2s}
.btn-teal:hover{opacity:.85;transform:translateY(-2px)}
.btn-earth{background:var(--green);border:none;color:var(--bg);font-family:'DM Mono',monospace;font-size:.63rem;letter-spacing:3px;text-transform:uppercase;padding:12px 30px;cursor:pointer;font-weight:600;transition:all .2s}
.btn-earth:hover{opacity:.85;transform:translateY(-2px)}

/* GAME HEADER */
.g-top{flex-shrink:0;display:flex;align-items:center;gap:16px;padding:12px 24px;border-bottom:1px solid var(--border);background:rgba(8,8,8,.96);position:sticky;top:0;z-index:50}
.g-logo{font-family:'Bebas Neue',sans-serif;font-size:1.25rem;letter-spacing:2px;white-space:nowrap}
.g-logo em{color:var(--gold);font-style:normal}
.g-dots{flex:1;display:flex;gap:3px;flex-wrap:wrap;align-items:center}
.dot{width:7px;height:7px;border-radius:50%;background:var(--border);transition:all .3s;flex-shrink:0}
.dot.d-ff{background:var(--red)}.dot.d-eco{background:var(--green)}.dot.d-cur{background:var(--gold);box-shadow:0 0 6px var(--gold);animation:blink 1.2s infinite}
.g-hud{display:flex;align-items:center;gap:10px;flex-shrink:0}
.hud-lbl{font-size:.52rem;letter-spacing:3px;text-transform:uppercase;color:var(--smoke)}
.hud-track{width:80px;height:4px;background:var(--border);border-radius:2px;overflow:hidden}
.hud-fill{height:100%;border-radius:2px;transition:width .7s ease,background .4s}
.hud-val{font-size:.7rem;color:var(--silver);min-width:32px;text-align:right}
.score-hud{display:flex;align-items:center;gap:6px;flex-shrink:0;border-left:1px solid var(--border);padding-left:16px}
.score-pts{font-family:'Bebas Neue',sans-serif;font-size:1.3rem;color:var(--gold);letter-spacing:1px;transition:all .3s}
.score-lv{font-size:.52rem;letter-spacing:2px;color:var(--smoke);text-transform:uppercase}
.streak-badge{background:var(--green-dim);border:1px solid var(--green);color:var(--green);padding:3px 8px;font-size:.55rem;letter-spacing:2px;text-transform:uppercase;display:none}
.streak-badge.show{display:block;animation:popIn .3s ease}

/* GAME BODY */
.g-body{flex:1;display:grid;grid-template-columns:260px 1fr 250px;min-height:0}
@media(max-width:900px){.g-body{grid-template-columns:1fr}}
.g-left{border-right:1px solid var(--border);background:var(--deep);display:flex;flex-direction:column;gap:16px;padding:20px 16px;overflow-y:auto}
.col-lbl{font-size:.54rem;letter-spacing:4px;text-transform:uppercase;color:var(--smoke);padding-bottom:10px;border-bottom:1px solid var(--border)}
.closet-rod{width:100%;height:2px;background:linear-gradient(90deg,transparent,var(--border2),transparent)}
.hooks-grid{display:grid;grid-template-columns:repeat(5,1fr);gap:5px;padding-top:4px}
.hanger{display:flex;flex-direction:column;align-items:center}
.hanger-wire{width:1.5px;height:14px;background:var(--border2);transition:background .3s}
.hanger-item{width:40px;height:48px;border:1px solid var(--border);border-radius:5px 5px 7px 7px;background:var(--surface);display:flex;align-items:center;justify-content:center;font-size:1.15rem;transition:all .25s;cursor:default;position:relative}
.hanger-item.is-ff{background:#120404;border-color:#7a1a2055}
.hanger-item.is-eco{background:#040c06;border-color:#1a4a2855}
.hanger-item.empty{border-style:dashed;opacity:.25}
.hanger-item.removable{cursor:pointer;border-color:var(--red)!important;animation:glowRed .8s infinite alternate}
.hanger-item.removable:hover{transform:scale(.86) rotate(-5deg)}
.hanger.is-ff .hanger-wire{background:#7a1a2055}
.hanger.is-eco .hanger-wire{background:#1a4a2855}
.hanger-tag{font-size:.34rem;letter-spacing:.5px;text-transform:uppercase;color:var(--smoke);margin-top:2px}
.cap-bar-wrap{height:4px;background:var(--border);border-radius:2px;overflow:hidden;margin-top:6px}
.cap-bar-fill{height:100%;border-radius:2px;background:var(--green);transition:width .5s ease,background .3s}
.cap-txt{text-align:center;font-size:.6rem;color:var(--smoke);margin-top:4px}
.cap-txt b{color:var(--cream)}
.ach-mini{display:flex;flex-direction:column;gap:4px}
.ach-chip{display:flex;align-items:center;gap:8px;padding:6px 8px;border:1px solid var(--border);font-size:.58rem;color:var(--smoke);transition:all .3s}
.ach-chip.unlocked{border-color:#2a1e08;background:#0e0a02;color:var(--gold2)}
.ach-chip .ach-ico{font-size:.9rem;flex-shrink:0}
.ach-chip .ach-nm{font-size:.6rem;letter-spacing:1px}
.quit-link{background:transparent;border:1px solid var(--border);color:var(--smoke);font-family:'DM Mono',monospace;font-size:.54rem;letter-spacing:3px;text-transform:uppercase;padding:9px;cursor:pointer;width:100%;transition:all .2s;margin-top:auto}
.quit-link:hover{color:var(--ash);border-color:var(--border2)}

/* CENTER */
.g-center{display:flex;flex-direction:column;gap:18px;padding:24px 28px;overflow-y:auto}
.sc-eye{font-size:.55rem;letter-spacing:5px;text-transform:uppercase;color:var(--gold);margin-bottom:10px}
.sc-head{font-family:'Bebas Neue',sans-serif;font-size:clamp(1.8rem,3.6vw,3rem);line-height:.95;color:var(--cream);margin-bottom:12px}
.sc-price{display:inline-flex;align-items:baseline;gap:3px;background:var(--red);color:#fff;padding:5px 18px 5px 11px;clip-path:polygon(0 0,100% 0,90% 100%,0 100%);margin-bottom:16px}
.sc-price .d{font-size:.62rem}
.sc-price .a{font-family:'Bebas Neue',sans-serif;font-size:1.8rem;line-height:1}
.sc-div{display:flex;align-items:center;gap:12px;margin-bottom:16px}
.sc-div::before,.sc-div::after{content:'';flex:1;height:1px;background:var(--border)}
.sc-div span{font-size:.5rem;letter-spacing:4px;color:var(--smoke);text-transform:uppercase}
.event-banner{display:none;padding:14px 16px;font-size:.72rem;line-height:1.6;border:1px solid;margin-bottom:4px;position:relative}
.event-banner.show{display:block;animation:fadeUp .4s ease}
.event-banner.positive{background:#061008;border-color:var(--green-dim);color:#9fe8b0}
.event-banner.negative{background:var(--red-bg);border-color:var(--red-dim);color:#f5a0a5}
.event-banner.neutral{background:#0a0a02;border-color:#2a2a08;color:var(--gold2)}
.event-tag{font-size:.5rem;letter-spacing:3px;text-transform:uppercase;display:block;margin-bottom:4px;opacity:.7}
.discard-warn{display:none;background:var(--red-bg);border:1px solid var(--red-dim);padding:12px 16px;font-size:.7rem;color:#f5a0a5;line-height:1.6;margin-bottom:4px}
.discard-warn.show{display:block}
.choices{display:grid;grid-template-columns:1fr 1fr;gap:12px}
@media(max-width:500px){.choices{grid-template-columns:1fr}}
.choice{background:var(--surface);border:1px solid var(--border);cursor:pointer;text-align:left;padding:0;transition:all .22s cubic-bezier(.4,0,.2,1);position:relative;overflow:hidden}
.choice::before{content:'';position:absolute;top:0;left:0;right:0;height:2px;transition:height .25s}
.choice.ff-c::before{background:var(--red)}
.choice.eco-c::before{background:var(--green)}
.choice:hover:not(:disabled){transform:translateY(-4px)}
.choice.ff-c:hover:not(:disabled){border-color:var(--red-dim);box-shadow:0 14px 40px rgba(230,57,70,.1)}
.choice.eco-c:hover:not(:disabled){border-color:var(--green-dim);box-shadow:0 14px 40px rgba(82,178,106,.1)}
.choice:hover:not(:disabled)::before{height:3px}
.choice:disabled{opacity:.35;cursor:not-allowed;transform:none!important}
.c-inner{padding:18px 20px}
.c-top{display:flex;align-items:center;gap:9px;margin-bottom:10px}
.c-emoji{font-size:1.7rem;line-height:1}
.c-type{font-size:.54rem;letter-spacing:4px;text-transform:uppercase}
.ff-c .c-type{color:var(--red)}
.eco-c .c-type{color:var(--green)}
.c-name{font-size:.82rem;color:var(--cream);font-weight:500;margin-bottom:5px}
.c-desc{font-size:.67rem;color:var(--ash);line-height:1.6;margin-bottom:12px}
.c-effect{font-size:.6rem;letter-spacing:1px;padding:7px 10px;display:flex;align-items:center;gap:6px}
.ff-c .c-effect{background:var(--red-dim);color:#f5a0a5}
.eco-c .c-effect{background:var(--green-dim);color:#9fe8b0}
.c-pts{font-size:.55rem;color:var(--smoke);margin-top:4px;text-align:right}
.kb-hint{display:flex;gap:16px;font-size:.55rem;color:var(--smoke);letter-spacing:1px}
.kb-key{border:1px solid var(--border);padding:2px 7px;border-radius:3px;color:var(--ash)}
.eco-tip-box{background:var(--deep);border:1px solid var(--border);padding:14px 16px}
.eco-tip-label{font-size:.5rem;letter-spacing:4px;text-transform:uppercase;color:var(--green);margin-bottom:6px;display:flex;align-items:center;gap:6px}
.eco-tip-text{font-family:'Cormorant Garamond',serif;font-style:italic;font-size:.9rem;color:var(--silver);line-height:1.6}
.log-panel{border:1px solid var(--border);background:var(--deep)}
.log-head{padding:8px 13px;border-bottom:1px solid var(--border);font-size:.5rem;letter-spacing:4px;text-transform:uppercase;color:var(--smoke)}
.log-body{max-height:130px;overflow-y:auto;padding:8px 13px;display:flex;flex-direction:column;gap:3px;scrollbar-width:thin;scrollbar-color:var(--border) transparent}
.log-row{display:grid;grid-template-columns:72px 1fr 54px;gap:8px;align-items:center;padding:4px 0;border-bottom:1px solid #1a1a1a;font-size:.6rem;animation:fadeUp .2s ease}
.log-time{color:var(--smoke);opacity:.6}
.log-text.ff{color:#f5a0a5}.log-text.eco{color:#9fe8b0}.log-text.warn{color:#f5cc80}.log-text.event{color:var(--blue)}.log-text.ach{color:var(--gold)}
.log-delta{text-align:right;font-weight:600}
.log-delta.neg{color:var(--red)}.log-delta.pos{color:var(--green)}.log-delta.gld{color:var(--gold)}

/* RIGHT panel */
.g-right{border-left:1px solid var(--border);background:var(--deep);display:flex;flex-direction:column;overflow-y:auto}
.stat-sec{padding:18px 18px;border-bottom:1px solid var(--border)}
.planet-wrap{display:flex;justify-content:center;margin-bottom:10px;position:relative}
#planetSvg{transition:all .5s ease}
.planet-lbl{text-align:center;font-size:.52rem;letter-spacing:3px;text-transform:uppercase;transition:color .4s}
.planet-big{font-family:'Bebas Neue',sans-serif;font-size:3.8rem;line-height:1;text-align:center;transition:color .4s}
.planet-bar{height:4px;background:var(--border);border-radius:2px;overflow:hidden;margin-top:8px}
.planet-bar-fill{height:100%;border-radius:2px;transition:width .7s ease,background .4s}
.score-display{text-align:center;padding:14px 18px;border-bottom:1px solid var(--border)}
.sd-pts{font-family:'Bebas Neue',sans-serif;font-size:2.8rem;color:var(--gold);letter-spacing:1px}
.sd-lv{font-size:.52rem;letter-spacing:3px;text-transform:uppercase;color:var(--smoke);margin-bottom:6px}
.xp-bar-wrap{height:4px;background:var(--border);border-radius:2px;overflow:hidden}
.xp-bar-fill{height:100%;border-radius:2px;background:var(--gold);transition:width .5s ease}
.stat-list{display:flex;flex-direction:column}
.s-it{padding:11px 18px;border-bottom:1px solid var(--border);display:flex;flex-direction:column;gap:3px}
.s-it:last-child{border:none}
.s-k{font-size:.5rem;letter-spacing:3px;text-transform:uppercase;color:var(--smoke)}
.s-v{font-family:'Bebas Neue',sans-serif;font-size:1.35rem;letter-spacing:1px}
.s-v.red{color:var(--red)}.s-v.grn{color:var(--green)}.s-v.gld{color:var(--gold)}
.mini-bars{display:flex;gap:2px;align-items:flex-end;height:22px;margin-top:3px}
.m-bar{flex:1;border-radius:1px 1px 0 0;min-height:2px;transition:height .3s ease}

/* END SCREEN (CLOSET) */
.end-wrap{max-width:740px;width:100%}
.end-stripe{height:3px;width:100%;margin-bottom:36px}
.report-card{border:1px solid var(--border);margin-bottom:2px;overflow:hidden}
.rc-header{display:flex;align-items:stretch;border-bottom:1px solid var(--border)}
.rc-grade{width:100px;display:flex;align-items:center;justify-content:center;flex-direction:column;border-right:1px solid var(--border);padding:24px 10px}
.grade-letter{font-family:'Bebas Neue',sans-serif;font-size:4rem;line-height:1}
.grade-label{font-size:.48rem;letter-spacing:3px;text-transform:uppercase;color:var(--smoke);margin-top:4px}
.rc-title-block{flex:1;padding:24px 28px;display:flex;flex-direction:column;justify-content:center}
.rc-verdict{font-size:.58rem;letter-spacing:4px;text-transform:uppercase;margin-bottom:8px}
.rc-verdict.good{color:var(--green)}.rc-verdict.mid{color:var(--amber)}.rc-verdict.bad{color:var(--red)}
.rc-title{font-family:'Bebas Neue',sans-serif;font-size:clamp(1.8rem,3.5vw,2.8rem);line-height:.95;margin-bottom:8px}
.rc-desc{font-family:'Cormorant Garamond',serif;font-style:italic;font-size:.95rem;line-height:1.7;color:var(--silver)}
.rc-stats{display:grid;grid-template-columns:1fr 1fr;border-top:1px solid var(--border)}
@media(max-width:520px){.rc-stats{grid-template-columns:1fr}}
.rc-stat{padding:16px 20px;border-right:1px solid var(--border);border-bottom:1px solid var(--border)}
.rc-stat:nth-child(even){border-right:none}
.rc-stat:nth-last-child(-n+2){border-bottom:none}
.rc-sk{font-size:.52rem;letter-spacing:3px;text-transform:uppercase;color:var(--smoke);margin-bottom:5px}
.rc-sv{font-family:'Bebas Neue',sans-serif;font-size:1.6rem;letter-spacing:1px}
.rc-sv.red{color:var(--red)}.rc-sv.grn{color:var(--green)}.rc-sv.gld{color:var(--gold)}.rc-sv.blue{color:var(--blue)}
.score-hero{border:1px solid var(--border);background:var(--deep);padding:24px 28px;margin-bottom:2px;display:flex;align-items:center;gap:32px;flex-wrap:wrap}
.sh-score{font-family:'Bebas Neue',sans-serif;font-size:5.5rem;line-height:1;letter-spacing:-2px}
.sh-meta{display:flex;flex-direction:column;gap:6px}
.sh-label{font-size:.55rem;letter-spacing:4px;text-transform:uppercase;color:var(--smoke)}
.sh-status{font-family:'Cormorant Garamond',serif;font-style:italic;font-size:1.25rem;color:var(--silver)}
.sh-bar-wrap{width:160px;height:5px;background:var(--border);border-radius:2px;overflow:hidden;margin-top:4px}
.sh-bar-fill{height:100%;border-radius:2px;width:0;transition:width 1.4s cubic-bezier(.4,0,.2,1) .2s}
.ach-end{border:1px solid var(--border);background:var(--deep);padding:20px;margin-bottom:2px}
.ach-end-title{font-size:.54rem;letter-spacing:4px;text-transform:uppercase;color:var(--smoke);margin-bottom:12px;padding-bottom:10px;border-bottom:1px solid var(--border)}
.ach-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:8px}
@media(max-width:500px){.ach-grid{grid-template-columns:repeat(2,1fr)}}
.ach-end-chip{border:1px solid var(--border);padding:10px 8px;text-align:center;transition:all .3s}
.ach-end-chip.unlocked{border-color:#2a1e08;background:#0e0a02}
.ach-end-chip.locked{opacity:.3;filter:grayscale(1)}
.aec-icon{font-size:1.4rem;margin-bottom:4px}
.aec-name{font-size:.52rem;letter-spacing:1px;color:var(--gold2);line-height:1.3}
.aec-name.locked{color:var(--smoke)}
.end-actions{display:flex;gap:2px;margin-top:2px;flex-wrap:wrap}
.end-btn{flex:1;min-width:100px;padding:15px 8px;background:var(--surface);border:1px solid var(--border);color:var(--ash);font-family:'DM Mono',monospace;font-size:.58rem;letter-spacing:3px;text-transform:uppercase;cursor:pointer;transition:all .22s}
.end-btn:hover{background:var(--card);color:var(--cream)}
.end-btn.primary{background:var(--gold);color:var(--bg);border-color:var(--gold);font-weight:600}
.end-btn.primary:hover{background:var(--gold2)}
.end-btn.tycoon{background:var(--teal-dark);color:#a0f0eb;border-color:var(--teal);font-weight:600}
.end-btn.tycoon:hover{background:var(--teal);color:var(--bg)}
.end-btn.earth{background:var(--green-dim);color:#9fe8b0;border-color:var(--green);font-weight:600}
.end-btn.earth:hover{background:var(--green);color:var(--bg)}

/* TYCOON INTRO */
.tycoon-wrap{display:grid;grid-template-columns:1fr 1fr;max-width:920px;width:100%;border:1px solid var(--teal-dark)}
@media(max-width:620px){.tycoon-wrap{grid-template-columns:1fr}}
.tycoon-l{padding:48px 40px;border-right:1px solid var(--teal-dark)}
.tycoon-r{padding:40px 32px;background:var(--deep)}
.tycoon-eyebrow{font-size:.58rem;letter-spacing:5px;text-transform:uppercase;color:var(--teal);margin-bottom:14px}
.tycoon-h{font-family:'Bebas Neue',sans-serif;font-size:clamp(2.6rem,5vw,4.2rem);line-height:.9;margin-bottom:18px}
.tycoon-h span{color:var(--teal);display:block}
.tycoon-rules-title{font-size:.58rem;letter-spacing:4px;text-transform:uppercase;color:var(--smoke);padding-bottom:12px;border-bottom:1px solid var(--border);margin-bottom:4px}

/* TYCOON GAME */
.t-top{flex-shrink:0;display:flex;align-items:center;gap:16px;padding:12px 24px;border-bottom:1px solid var(--teal-dark);background:rgba(8,8,8,.96);position:sticky;top:0;z-index:50}
.t-logo{font-family:'Bebas Neue',sans-serif;font-size:1.25rem;letter-spacing:2px;white-space:nowrap}
.t-logo em{color:var(--teal);font-style:normal}
.t-spacer{flex:1}
.t-hud-group{display:flex;align-items:center;gap:18px}
.t-hud{display:flex;align-items:center;gap:8px}
.t-hud-lbl{font-size:.52rem;letter-spacing:3px;text-transform:uppercase;color:var(--smoke)}
.t-hud-track{width:80px;height:4px;border-radius:2px;overflow:hidden}
.t-hud-track.profit-track{background:#0a1a0a}
.t-hud-track.pollute-track{background:#1a0a0a}
.t-hud-fill{height:100%;border-radius:2px;transition:width .7s ease,background .4s}
.t-hud-val{font-size:.7rem;color:var(--silver);min-width:44px;text-align:right}
.t-body{flex:1;display:grid;grid-template-columns:260px 1fr 260px;min-height:0}
@media(max-width:900px){.t-body{grid-template-columns:1fr}}
.t-left{border-right:1px solid var(--teal-dark);background:var(--deep);display:flex;flex-direction:column;overflow-y:auto}
.t-section{padding:18px 18px;border-bottom:1px solid var(--border)}
.t-section-title{font-size:.52rem;letter-spacing:4px;text-transform:uppercase;color:var(--smoke);margin-bottom:12px}
.factory-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:5px;margin-bottom:12px}
.factory-unit{height:34px;border-radius:3px;border:1px solid var(--border);display:flex;align-items:center;justify-content:center;font-size:1rem;transition:all .3s}
.factory-unit.ff-u{background:#120404;border-color:#7a1a2044}
.factory-unit.eco-u{background:#040c06;border-color:#1a4a2844}
.factory-unit.rec-u{background:#041214;border-color:#1a4a4a44}
.factory-unit.empty-u{opacity:.2;border-style:dashed}
.company-name{font-family:'Bebas Neue',sans-serif;font-size:1.5rem;color:var(--teal);letter-spacing:1px;margin-bottom:3px}
.company-tagline{font-size:.6rem;color:var(--smoke);font-family:'Cormorant Garamond',serif;font-style:italic}
.t-stat{padding:10px 18px;border-bottom:1px solid var(--border);display:flex;flex-direction:column;gap:2px}
.t-stat:last-child{border:none}
.t-sk{font-size:.5rem;letter-spacing:3px;text-transform:uppercase;color:var(--smoke)}
.t-sv{font-family:'Bebas Neue',sans-serif;font-size:1.3rem;letter-spacing:1px}
.t-sv.grn{color:var(--green)}.t-sv.red{color:var(--red)}.t-sv.gld{color:var(--gold)}.t-sv.teal{color:var(--teal)}
.pollute-meter{margin:4px 0 8px}
.pollute-track-big{height:7px;background:var(--border);border-radius:4px;overflow:hidden}
.pollute-fill-big{height:100%;border-radius:4px;transition:width .7s ease,background .4s}
.pollute-numbers{display:flex;justify-content:space-between;font-size:.56rem;color:var(--smoke);margin-top:4px}
.climate-gauge{text-align:center;padding:8px 0}
.gauge-num{font-family:'Bebas Neue',sans-serif;font-size:3.5rem;line-height:1;transition:color .4s}
.gauge-lbl{font-size:.52rem;letter-spacing:3px;text-transform:uppercase;margin-top:2px;transition:color .4s}
.gauge-limit{font-size:.48rem;color:var(--smoke);margin-top:4px}
.t-quit{background:transparent;border:1px solid var(--border);color:var(--smoke);font-family:'DM Mono',monospace;font-size:.54rem;letter-spacing:3px;text-transform:uppercase;padding:9px;cursor:pointer;width:calc(100% - 36px);margin:auto 18px 18px;transition:all .2s}
.t-quit:hover{color:var(--ash);border-color:var(--border2)}
.t-center{display:flex;flex-direction:column;gap:18px;padding:24px 28px;overflow-y:auto}
.t-round-eye{font-size:.55rem;letter-spacing:5px;text-transform:uppercase;color:var(--teal);margin-bottom:10px}
.t-headline{font-family:'Bebas Neue',sans-serif;font-size:clamp(1.8rem,3.4vw,2.8rem);line-height:.95;color:var(--cream);margin-bottom:8px}
.t-subline{font-family:'Cormorant Garamond',serif;font-style:italic;font-size:.92rem;color:var(--ash);line-height:1.7;margin-bottom:16px}
.t-crisis-warn{display:none;background:#1a0608;border:1px solid var(--red-dim);padding:12px 16px;font-size:.72rem;color:#f5a0a5;line-height:1.6;animation:pulseRed 1s infinite}
.t-crisis-warn.show{display:block}
.t-choices{display:grid;grid-template-columns:1fr 1fr 1fr;gap:12px}
@media(max-width:600px){.t-choices{grid-template-columns:1fr}}
.t-choice{background:var(--surface);border:1px solid var(--border);cursor:pointer;text-align:left;padding:0;transition:all .22s cubic-bezier(.4,0,.2,1);position:relative;overflow:hidden}
.t-choice::before{content:'';position:absolute;top:0;left:0;right:0;height:2px;transition:height .25s}
.t-choice.ff-p::before{background:var(--red)}.t-choice.eco-p::before{background:var(--green)}.t-choice.rec-p::before{background:var(--teal)}
.t-choice:hover:not(:disabled){transform:translateY(-4px)}
.t-choice.ff-p:hover:not(:disabled){border-color:var(--red-dim);box-shadow:0 12px 36px rgba(230,57,70,.1)}
.t-choice.eco-p:hover:not(:disabled){border-color:var(--green-dim);box-shadow:0 12px 36px rgba(82,178,106,.1)}
.t-choice.rec-p:hover:not(:disabled){border-color:var(--teal-dark);box-shadow:0 12px 36px rgba(46,196,182,.1)}
.t-choice:hover:not(:disabled)::before{height:3px}
.t-choice:disabled{opacity:.3;cursor:not-allowed;transform:none!important}
.tc-inner{padding:16px 15px}
.tc-top{display:flex;align-items:center;gap:9px;margin-bottom:9px}
.tc-emoji{font-size:1.5rem;line-height:1}
.tc-type{font-size:.52rem;letter-spacing:3px;text-transform:uppercase}
.ff-p .tc-type{color:var(--red)}.eco-p .tc-type{color:var(--green)}.rec-p .tc-type{color:var(--teal)}
.tc-name{font-size:.78rem;color:var(--cream);font-weight:500;margin-bottom:5px}
.tc-desc{font-size:.64rem;color:var(--ash);line-height:1.6;margin-bottom:10px}
.tc-effects{display:flex;flex-direction:column;gap:4px}
.tc-eff{font-size:.58rem;padding:5px 8px;display:flex;align-items:center;gap:5px;border-radius:1px}
.tc-eff.profit{background:#0a1a0a;color:#9fe8b0}.tc-eff.pollute{background:var(--red-bg);color:#f5a0a5}.tc-eff.reduce{background:#041214;color:#a0f0eb}
.t-log-panel{border:1px solid var(--border);background:var(--deep)}
.t-log-head{padding:8px 13px;border-bottom:1px solid var(--border);font-size:.5rem;letter-spacing:4px;text-transform:uppercase;color:var(--smoke)}
.t-log-body{max-height:130px;overflow-y:auto;padding:8px 13px;display:flex;flex-direction:column;gap:3px;scrollbar-width:thin;scrollbar-color:var(--border) transparent}
.t-log-row{display:grid;grid-template-columns:52px 1fr auto;gap:8px;align-items:center;padding:4px 0;border-bottom:1px solid #1a1a1a;font-size:.6rem;animation:fadeUp .2s ease}
.t-log-type{font-size:.48rem;letter-spacing:2px;text-transform:uppercase;padding:2px 5px;border-radius:1px}
.t-log-type.ff{background:var(--red-dim);color:#f5a0a5}.t-log-type.eco{background:var(--green-dim);color:#9fe8b0}.t-log-type.rec{background:var(--teal-dark);color:#a0f0eb}.t-log-type.sys{background:var(--border);color:var(--ash)}
.t-log-msg{color:var(--ash)}.t-log-profit{font-weight:600;color:var(--green)}
.t-right{border-left:1px solid var(--teal-dark);background:var(--deep);display:flex;flex-direction:column;overflow-y:auto}
.t-r-section{padding:18px 18px;border-bottom:1px solid var(--border)}
.t-r-section:last-child{border:none}
.t-r-title{font-size:.52rem;letter-spacing:4px;text-transform:uppercase;color:var(--smoke);margin-bottom:12px}
.demand-bars{display:flex;flex-direction:column;gap:8px}
.demand-row{display:flex;align-items:center;gap:8px}
.demand-lbl{font-size:.54rem;text-transform:uppercase;letter-spacing:2px;color:var(--ash);width:54px;flex-shrink:0}
.demand-bar-wrap{flex:1;height:5px;background:var(--border);border-radius:3px;overflow:hidden}
.demand-bar-fill{height:100%;border-radius:3px;transition:width .8s ease}
.demand-val{font-size:.58rem;color:var(--silver);min-width:26px;text-align:right}
.hist-chart{display:flex;gap:3px;align-items:flex-end;height:46px}
.h-bar-group{display:flex;flex-direction:column;gap:1px;align-items:center;flex:1}
.h-bar{width:100%;border-radius:1px 1px 0 0;transition:height .4s ease}
.h-bar-lbl{font-size:.36rem;color:var(--smoke);margin-top:2px}

/* TYCOON END */
.t-end-wrap{max-width:740px;width:100%}
.t-end-stripe{height:3px;margin-bottom:36px}
.t-end-hero{border:1px solid var(--border);background:var(--deep);padding:24px 28px;margin-bottom:2px;display:flex;align-items:center;gap:32px;flex-wrap:wrap}
.t-end-profit-big{font-family:'Bebas Neue',sans-serif;font-size:5.5rem;line-height:1;letter-spacing:-2px}
.t-end-hero-meta{display:flex;flex-direction:column;gap:6px}
.t-end-hero-label{font-size:.55rem;letter-spacing:4px;text-transform:uppercase;color:var(--smoke)}
.t-end-hero-status{font-family:'Cormorant Garamond',serif;font-style:italic;font-size:1.25rem;color:var(--silver)}
.t-report-card{border:1px solid var(--border);margin-bottom:2px;overflow:hidden}
.t-rc-header{display:flex;align-items:stretch;border-bottom:1px solid var(--border)}
.t-rc-grade{width:100px;display:flex;align-items:center;justify-content:center;flex-direction:column;border-right:1px solid var(--border);padding:24px 10px}
.t-rc-title-block{flex:1;padding:24px 28px;display:flex;flex-direction:column;justify-content:center}
.t-rc-verdict{font-size:.58rem;letter-spacing:4px;text-transform:uppercase;margin-bottom:8px}
.t-rc-verdict.good{color:var(--teal)}.t-rc-verdict.mid{color:var(--amber)}.t-rc-verdict.bad{color:var(--red)}
.t-rc-stats.rc-stats{display:grid;grid-template-columns:1fr 1fr;border-top:1px solid var(--border)}
@media(max-width:520px){.t-rc-stats.rc-stats{grid-template-columns:1fr}}
.t-end-actions{display:flex;gap:2px;margin-top:2px;flex-wrap:wrap}
.t-end-btn{flex:1;min-width:100px;padding:15px 8px;background:var(--surface);border:1px solid var(--border);color:var(--ash);font-family:'DM Mono',monospace;font-size:.58rem;letter-spacing:3px;text-transform:uppercase;cursor:pointer;transition:all .22s}
.t-end-btn:hover{background:var(--card);color:var(--cream)}
.t-end-btn.primary{background:var(--teal);color:var(--bg);border-color:var(--teal);font-weight:600}
.t-end-btn.primary:hover{opacity:.85}
.t-end-btn.gold-btn{background:var(--gold);color:var(--bg);border-color:var(--gold);font-weight:600}
.t-end-btn.gold-btn:hover{background:var(--gold2)}
.t-end-btn.earth-btn{background:var(--green-dim);color:#9fe8b0;border-color:var(--green);font-weight:600}
.t-end-btn.earth-btn:hover{background:var(--green);color:var(--bg)}

/* SAVE THE EARTH — ASK */
.ask-wrap{max-width:600px;width:100%;border:1px solid var(--green-dim);background:var(--deep);padding:0;overflow:hidden}
.ask-header{background:linear-gradient(135deg,#061208,#0a1f0e);padding:48px 40px 32px;border-bottom:1px solid var(--green-dim)}
.ask-eyebrow{font-size:.58rem;letter-spacing:5px;text-transform:uppercase;color:var(--green);margin-bottom:14px}
.ask-title{font-family:'Bebas Neue',sans-serif;font-size:clamp(3rem,7vw,5.5rem);line-height:.88;color:var(--cream);margin-bottom:16px}
.ask-title span{color:var(--green);display:block}
.ask-body{font-family:'Cormorant Garamond',serif;font-size:1.05rem;line-height:1.9;color:var(--silver)}
.ask-rules{padding:28px 40px;display:flex;flex-direction:column;gap:0}
.ask-rule{display:flex;gap:14px;align-items:flex-start;padding:12px 0;border-bottom:1px solid var(--border)}
.ask-rule:last-child{border:none}
.ask-rule-icon{font-size:1.4rem;flex-shrink:0;width:36px;text-align:center}
.ask-rule-text b{display:block;font-size:.64rem;letter-spacing:2px;text-transform:uppercase;color:var(--cream);margin-bottom:3px}
.ask-rule-text span{font-size:.7rem;color:var(--ash);line-height:1.5}
.ask-actions{padding:20px 40px 36px;display:flex;gap:12px;flex-wrap:wrap}

/* SAVE THE EARTH — GAME */
#s-earth{background:#000;position:fixed;inset:0;overflow:hidden}
#earthCanvas{display:block;width:100%;height:100%}
.earth-hud{position:fixed;top:0;left:0;right:0;z-index:20;display:flex;align-items:center;gap:16px;padding:10px 22px;background:rgba(0,0,0,.88);border-bottom:1px solid rgba(82,178,106,.2)}
.earth-logo{font-family:'Bebas Neue',sans-serif;font-size:1.2rem;letter-spacing:2px;color:var(--green)}
.earth-logo span{color:var(--cream)}
.earth-spacer{flex:1}
.earth-stat{display:flex;align-items:center;gap:8px}
.earth-stat-lbl{font-size:.5rem;letter-spacing:3px;text-transform:uppercase;color:var(--smoke)}
.earth-stat-bar{width:100px;height:5px;border-radius:3px;overflow:hidden}
.earth-stat-bar.earth-poll-track{background:#1a0608}
.earth-stat-fill{height:100%;border-radius:3px;transition:width .4s ease,background .3s}
.earth-stat-val{font-size:.72rem;min-width:30px;text-align:right}
.earth-score-disp{font-family:'Bebas Neue',sans-serif;font-size:1.4rem;color:var(--gold);letter-spacing:1px;border-left:1px solid var(--border);padding-left:14px}
.earth-score-lbl{font-size:.46rem;letter-spacing:2px;text-transform:uppercase;color:var(--smoke);display:block;line-height:1}
.earth-pause-btn{background:transparent;border:1px solid var(--border);color:var(--ash);font-family:'DM Mono',monospace;font-size:.54rem;letter-spacing:3px;text-transform:uppercase;padding:7px 14px;cursor:pointer;transition:all .2s}
.earth-pause-btn:hover{color:var(--cream);border-color:var(--border2)}

/* EARTH END */
.earth-end-wrap{max-width:580px;width:100%}
.earth-end-header{border:1px solid var(--border);background:var(--deep);padding:28px 32px;margin-bottom:2px;text-align:center}
.earth-end-icon{font-size:4rem;margin-bottom:12px}
.earth-end-title{font-family:'Bebas Neue',sans-serif;font-size:clamp(2rem,5vw,3.5rem);line-height:.95;margin-bottom:8px}
.earth-end-sub{font-family:'Cormorant Garamond',serif;font-style:italic;font-size:1rem;color:var(--silver);line-height:1.7}
.earth-end-stats{display:grid;grid-template-columns:1fr 1fr 1fr;border:1px solid var(--border);background:var(--deep);margin-bottom:2px}
.earth-end-stat{padding:16px 12px;text-align:center;border-right:1px solid var(--border)}
.earth-end-stat:last-child{border:none}
.ees-val{font-family:'Bebas Neue',sans-serif;font-size:2rem;letter-spacing:1px;margin-bottom:3px}
.ees-lbl{font-size:.5rem;letter-spacing:3px;text-transform:uppercase;color:var(--smoke)}
.earth-end-actions{display:flex;gap:2px;flex-wrap:wrap}
.earth-end-btn{flex:1;min-width:100px;padding:14px 8px;background:var(--surface);border:1px solid var(--border);color:var(--ash);font-family:'DM Mono',monospace;font-size:.58rem;letter-spacing:3px;text-transform:uppercase;cursor:pointer;transition:all .22s}
.earth-end-btn:hover{background:var(--card);color:var(--cream)}
.earth-end-btn.primary{background:var(--green);color:var(--bg);border-color:var(--green);font-weight:600}
.earth-end-btn.primary:hover{opacity:.85}

/* TOAST */
.toast{position:fixed;bottom:28px;left:50%;transform:translateX(-50%);background:var(--card);border:1px solid var(--border2);padding:10px 24px;font-size:.68rem;letter-spacing:1px;z-index:9999;pointer-events:none;white-space:nowrap;animation:toastUp .3s ease both}
.toast.bad{border-color:var(--red-dim);color:#f5a0a5}.toast.good{border-color:var(--green-dim);color:#9fe8b0}.toast.ach{border-color:#2a1e08;color:var(--gold2)}.toast.event-t{border-color:var(--blue);color:var(--blue)}.toast.lvup{border-color:var(--purple);color:#c4b5fd;background:#0e0a18}.toast.info{border-color:var(--teal-dark);color:#a0f0eb}

/* KEYFRAMES */
@keyframes fadeUp{from{opacity:0;transform:translateY(10px)}to{opacity:1;transform:translateY(0)}}
@keyframes toastUp{from{opacity:0;transform:translateX(-50%) translateY(8px)}to{opacity:1;transform:translateX(-50%) translateY(0)}}
@keyframes blink{0%,100%{opacity:1}50%{opacity:.35}}
@keyframes glowRed{from{box-shadow:0 0 4px rgba(230,57,70,.3)}to{box-shadow:0 0 14px rgba(230,57,70,.7)}}
@keyframes popIn{from{opacity:0;transform:scale(.88)}to{opacity:1;transform:scale(1)}}
@keyframes planetPulse{0%,100%{transform:scale(1)}50%{transform:scale(1.04)}}
@keyframes pulseRed{0%,100%{border-color:var(--red-dim)}50%{border-color:var(--red)}}
@keyframes swing{0%,100%{transform:rotate(-6deg)}50%{transform:rotate(6deg)}}
</style>
</head>
<body>
<canvas id="bgCanvas"></canvas>

<!-- SPLASH -->
<div class="screen active" id="s-splash">
  <div class="splash-logo"><div>CLOSET</div><div class="ol">CONSUMER</div><div>ISM</div></div>
  <div class="splash-sub">A Fashion Waste Simulator</div>
  <button class="splash-btn" onclick="goIntro()">Enter the Closet</button>
  <div class="splash-version">v1.0 · Feature Edition + Fashion Tycoon + Save The Earth</div>
</div>

<!-- CLOSET INTRO -->
<div class="screen" id="s-intro">
  <div class="intro-wrap">
    <div class="intro-l">
      <div class="eyebrow">🏷️ Interactive Simulation · 15 Rounds</div>
      <div class="intro-h">Closet<span>Consumerism</span></div>
      <div class="intro-body">You manage a closet with <strong style="color:var(--cream)">10 slots</strong>. Every round you face a real fast-fashion dilemma. Random events, combos, and achievements make every run unique.</div>
      <div class="diff-label">Select Difficulty</div>
      <div class="diff-btns">
        <button class="diff-btn" onclick="setDiff('easy')" id="d-easy">Easy<span class="diff-sub">+Planet buffer</span></button>
        <button class="diff-btn active" onclick="setDiff('normal')" id="d-normal">Normal<span class="diff-sub">Balanced</span></button>
        <button class="diff-btn" onclick="setDiff('hard')" id="d-hard">Hard<span class="diff-sub">Unforgiving</span></button>
      </div>
      <div class="intro-btns">
        <button class="btn-gold" onclick="startGame()">▶ Start Game</button>
        <button class="btn-ghost" onclick="goSplash()">← Back</button>
      </div>
    </div>
    <div class="intro-r">
      <div class="rt">How It Works</div>
      <div class="rule-r"><div class="ri">🧥</div><div><b>10-Slot Closet</b><span>Limited space forces tough choices. Fill it wisely.</span></div></div>
      <div class="rule-r"><div class="ri">🌍</div><div><b>Planet Health</b><span>Starts at 100. Fast fashion drains it. Reach zero = game over.</span></div></div>
      <div class="rule-r"><div class="ri">⚡</div><div><b>Eco Streaks</b><span>Chain sustainable choices for combo multipliers and bonus points.</span></div></div>
      <div class="rule-r"><div class="ri">🎲</div><div><b>Random Events</b><span>Every few rounds a surprise event changes the rules.</span></div></div>
      <div class="rule-r"><div class="ri">🏆</div><div><b>Achievements</b><span>12 hidden achievements unlock throughout your run.</span></div></div>
      <div class="score-t">
        <div class="sc-row"><span>Buy fast fashion</span><span class="pill neg">−10 Planet</span></div>
        <div class="sc-row"><span>Sustainable choice</span><span class="pill pos">+5 Planet · +100pts</span></div>
        <div class="sc-row"><span>Discard an item</span><span class="pill neg">−5 Planet</span></div>
        <div class="sc-row"><span>Eco combo ×3+</span><span class="pill gld">Bonus points!</span></div>
      </div>
    </div>
  </div>
</div>

<!-- CLOSET GAME -->
<div class="screen" id="s-game">
  <div class="g-top">
    <div class="g-logo">Closet <em>Consumerism</em></div>
    <div class="g-dots" id="gDots"></div>
    <div class="streak-badge" id="streakBadge">🔥 Streak</div>
    <div class="g-hud">
      <div class="hud-lbl">Planet</div>
      <div class="hud-track"><div class="hud-fill" id="hudFill" style="width:100%;background:var(--green)"></div></div>
      <div class="hud-val" id="hudVal">100</div>
    </div>
    <div class="score-hud">
      <div>
        <div class="score-lv" id="scoreLv">LV 1</div>
        <div class="score-pts" id="scorePts">0</div>
      </div>
    </div>
  </div>
  <div class="g-body">
    <div class="g-left">
      <div class="col-lbl">Your Closet</div>
      <div class="closet-rod"></div>
      <div class="hooks-grid" id="hooksGrid"></div>
      <div class="cap-bar-wrap"><div class="cap-bar-fill" id="capBarFill" style="width:0"></div></div>
      <div class="cap-txt"><b id="capNum">0</b> / 10 slots</div>
      <div class="col-lbl" style="margin-top:4px">Achievements</div>
      <div class="ach-mini" id="achMini"></div>
      <button class="quit-link" onclick="endGame()">End Game Early</button>
    </div>
    <div class="g-center">
      <div>
        <div class="sc-eye" id="scEye">Round 1 of 15</div>
        <div class="sc-head" id="scHead">Loading...</div>
        <div class="sc-price"><span class="d">$</span><span class="a" id="scAmt">0</span></div>
      </div>
      <div class="event-banner" id="eventBanner">
        <span class="event-tag" id="eventTag">⚡ Random Event</span>
        <span id="eventText">Event description</span>
      </div>
      <div class="sc-div"><span>Make your choice</span></div>
      <div class="discard-warn" id="discardWarn">⚠️ Closet full — click a garment on the left to discard it.</div>
      <div class="choices">
        <button class="choice ff-c" onclick="choose('ff')">
          <div class="c-inner">
            <div class="c-top"><div class="c-emoji" id="cFfE">🛍️</div><div class="c-type">Fast Fashion  [A]</div></div>
            <div class="c-name" id="cFfN">Item</div>
            <div class="c-desc" id="cFfD">Desc</div>
            <div class="c-effect">🔴 &nbsp;−10 Planet</div>
            <div class="c-pts" id="cFfPts"></div>
          </div>
        </button>
        <button class="choice eco-c" onclick="choose('eco')">
          <div class="c-inner">
            <div class="c-top"><div class="c-emoji" id="cEcoE">🌱</div><div class="c-type">Sustainable  [B]</div></div>
            <div class="c-name" id="cEcoN">Option</div>
            <div class="c-desc" id="cEcoD">Desc</div>
            <div class="c-effect" id="cEcoEff">🟢 &nbsp;+5 Planet · +100pts</div>
            <div class="c-pts" id="cEcoPts"></div>
          </div>
        </button>
      </div>
      <div class="kb-hint">
        <span>Keyboard:</span>
        <span><span class="kb-key">A</span> Fast Fashion</span>
        <span><span class="kb-key">B</span> Sustainable</span>
        <span><span class="kb-key">T</span> Eco Tip</span>
      </div>
      <div class="eco-tip-box" id="ecoTipBox" style="display:none">
        <div class="eco-tip-label">🌿 Eco Tip <button onclick="nextTip()" style="background:none;border:none;color:var(--green);cursor:pointer;font-size:.6rem;margin-left:auto">Next →</button></div>
        <div class="eco-tip-text" id="ecoTipText">Loading tip...</div>
      </div>
      <div class="log-panel">
        <div class="log-head">Activity Log</div>
        <div class="log-body" id="logBody"></div>
      </div>
    </div>
    <div class="g-right">
      <div class="stat-sec">
        <div class="col-lbl" style="margin-bottom:12px">Planet Health</div>
        <div class="planet-wrap">
          <svg id="planetSvg" width="80" height="80" viewBox="0 0 80 80">
            <defs>
              <radialGradient id="pg" cx="40%" cy="35%">
                <stop offset="0%" stop-color="#52b26a" id="pgStop1"/>
                <stop offset="100%" stop-color="#1a4a28" id="pgStop2"/>
              </radialGradient>
            </defs>
            <circle cx="40" cy="40" r="36" fill="url(#pg)" id="planetCircle"/>
            <ellipse cx="40" cy="40" rx="36" ry="10" fill="none" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>
            <circle cx="40" cy="40" r="36" fill="none" stroke="rgba(255,255,255,0.05)" stroke-width="2"/>
          </svg>
        </div>
        <div class="planet-big" id="pBig" style="color:var(--green)">100</div>
        <div class="planet-lbl" id="pLbl" style="color:var(--green)">🌳 Thriving</div>
        <div class="planet-bar"><div class="planet-bar-fill" id="pBarFill" style="width:100%;background:var(--green)"></div></div>
      </div>
      <div class="score-display">
        <div class="sd-lv" id="sdLv">Level 1 — Newcomer</div>
        <div class="sd-pts" id="sdPts">0</div>
        <div class="xp-bar-wrap"><div class="xp-bar-fill" id="xpFill" style="width:0"></div></div>
      </div>
      <div class="stat-list">
        <div class="s-it"><div class="s-k">Round</div><div class="s-v gld" id="sRound">1 / 15</div></div>
        <div class="s-it"><div class="s-k">Eco Streak</div><div class="s-v grn" id="sStreak">0 🔥</div></div>
        <div class="s-it"><div class="s-k">Fast Fashion</div><div class="s-v red" id="sFf">0</div><div class="mini-bars" id="bFf"></div></div>
        <div class="s-it"><div class="s-k">Sustainable</div><div class="s-v grn" id="sEco">0</div><div class="mini-bars" id="bEco"></div></div>
        <div class="s-it"><div class="s-k">Items Discarded</div><div class="s-v red" id="sDiscard">0</div></div>
        <div class="s-it"><div class="s-k">Money Spent (FF)</div><div class="s-v gld" id="sSpent">$0</div></div>
      </div>
    </div>
  </div>
</div>

<!-- CLOSET END -->
<div class="screen" id="s-end">
  <div class="end-wrap">
    <div class="end-stripe" id="endStripe"></div>
    <div class="score-hero">
      <div class="sh-score" id="shScore" style="color:var(--gold)">0</div>
      <div class="sh-meta">
        <div class="sh-label">Final Score</div>
        <div class="sh-status" id="shStatus">—</div>
        <div class="sh-bar-wrap"><div class="sh-bar-fill" id="shBarFill"></div></div>
      </div>
    </div>
    <div class="report-card">
      <div class="rc-header">
        <div class="rc-grade">
          <div class="grade-letter" id="gradeLetter" style="color:var(--green)">A</div>
          <div class="grade-label">Grade</div>
        </div>
        <div class="rc-title-block">
          <div class="rc-verdict" id="rcVerdict">Verdict</div>
          <div class="rc-title" id="rcTitle">Title</div>
          <div class="rc-desc" id="rcDesc">Description</div>
        </div>
      </div>
      <div class="rc-stats" id="rcStats"></div>
    </div>
    <div class="ach-end">
      <div class="ach-end-title">Achievements Unlocked</div>
      <div class="ach-grid" id="achGrid"></div>
    </div>
    <div class="end-actions">
      <button class="end-btn primary" onclick="startGame()">▶ Play Again</button>
      <button class="end-btn tycoon" onclick="goTycoonIntro()">🏭 Fashion Tycoon</button>
      <button class="end-btn earth" onclick="goEarthAsk()">🌍 Save The Earth</button>
      <button class="end-btn" onclick="goIntro()">Change Difficulty</button>
      <button class="end-btn" onclick="goSplash()">Main Menu</button>
    </div>
  </div>
</div>

<!-- TYCOON INTRO -->
<div class="screen" id="s-tycoon-intro">
  <div class="tycoon-wrap">
    <div class="tycoon-l">
      <div class="tycoon-eyebrow">🏭 Business Simulation · 12 Quarters</div>
      <div class="tycoon-h">Fashion<span>Tycoon</span></div>
      <div class="intro-body">You run a clothing empire. Each quarter choose how to produce. Chase profit — but if <strong style="color:var(--red)">pollution exceeds 100</strong> a climate crisis ends your company. Can you grow rich without burning the world?</div>
      <div class="intro-btns">
        <button class="btn-teal" onclick="startTycoon()">▶ Start Tycoon</button>
        <button class="btn-ghost" onclick="goSplash()">← Main Menu</button>
      </div>
    </div>
    <div class="tycoon-r">
      <div class="tycoon-rules-title">Production Options</div>
      <div class="rule-r"><div class="ri">🏭</div><div><b>Fast Fashion</b><span>+$30k profit per quarter. Adds +10 pollution. Maximum growth, maximum damage.</span></div></div>
      <div class="rule-r"><div class="ri">🌿</div><div><b>Sustainable</b><span>+$15k profit per quarter. Adds only +2 pollution. Slower but responsible growth.</span></div></div>
      <div class="rule-r"><div class="ri">♻️</div><div><b>Recycle</b><span>+$5k profit per quarter. Reduces pollution by 8. Saves the planet at a cost to revenue.</span></div></div>
      <div class="score-t">
        <div class="sc-row"><span>Pollution limit</span><span class="pill neg">100 MAX</span></div>
        <div class="sc-row"><span>Exceed limit</span><span class="pill neg">Climate Crisis!</span></div>
        <div class="sc-row"><span>Survive 12 quarters</span><span class="pill pos">You Win!</span></div>
      </div>
    </div>
  </div>
</div>

<!-- TYCOON GAME -->
<div class="screen" id="s-tycoon">
  <div class="t-top">
    <div class="t-logo">Fashion <em>Tycoon</em></div>
    <div class="t-spacer"></div>
    <div class="t-hud-group">
      <div class="t-hud">
        <div class="t-hud-lbl">Profit</div>
        <div class="t-hud-track profit-track"><div class="t-hud-fill" id="tHudProfit" style="width:0%;background:var(--green)"></div></div>
        <div class="t-hud-val" id="tHudProfitVal">$0</div>
      </div>
      <div class="t-hud">
        <div class="t-hud-lbl">Pollution</div>
        <div class="t-hud-track pollute-track"><div class="t-hud-fill" id="tHudPollute" style="width:0%;background:var(--green)"></div></div>
        <div class="t-hud-val" id="tHudPolluteVal">0</div>
      </div>
    </div>
  </div>
  <div class="t-body">
    <div class="t-left">
      <div class="t-section">
        <div class="t-section-title">Your Company</div>
        <div class="company-name" id="tCompanyName">LUXE CO.</div>
        <div class="company-tagline" id="tCompanyTagline">Building an empire...</div>
      </div>
      <div class="t-section">
        <div class="t-section-title">Factory History</div>
        <div class="factory-grid" id="tFactory"></div>
      </div>
      <div class="t-section">
        <div class="t-section-title">Pollution Level</div>
        <div class="climate-gauge">
          <div class="gauge-num" id="tPolluteBig" style="color:var(--green)">0</div>
          <div class="gauge-lbl" id="tPolluteLabel" style="color:var(--green)">🌤 Clear Skies</div>
          <div class="gauge-limit">Limit: 100</div>
        </div>
        <div class="pollute-meter">
          <div class="pollute-track-big"><div class="pollute-fill-big" id="tPolluteFill" style="width:0%;background:var(--green)"></div></div>
          <div class="pollute-numbers"><span>0</span><span style="color:var(--red)">⚠ 100</span></div>
        </div>
      </div>
      <div class="stat-list" style="flex:1">
        <div class="t-stat"><div class="t-sk">Quarter</div><div class="t-sv teal" id="tRound">1 / 12</div></div>
        <div class="t-stat"><div class="t-sk">Total Profit</div><div class="t-sv grn" id="tProfit">$0</div></div>
        <div class="t-stat"><div class="t-sk">FF Runs</div><div class="t-sv red" id="tFFCount">0</div></div>
        <div class="t-stat"><div class="t-sk">Eco Runs</div><div class="t-sv grn" id="tEcoCount">0</div></div>
        <div class="t-stat"><div class="t-sk">Recycles</div><div class="t-sv teal" id="tRecCount">0</div></div>
      </div>
      <button class="t-quit" onclick="endTycoon(true)">End Game Early</button>
    </div>
    <div class="t-center">
      <div>
        <div class="t-round-eye" id="tRoundEye">Quarter 1 of 12</div>
        <div class="t-headline" id="tHeadline">Choose Production Strategy</div>
        <div class="t-subline" id="tSubline">Your board is watching. Make a decision.</div>
      </div>
      <div class="t-crisis-warn" id="tCrisisWarn">🚨 DANGER — Pollution approaching critical threshold! Recycle now or face a climate crisis!</div>
      <div class="t-choices">
        <button class="t-choice ff-p" onclick="tChoose('ff')">
          <div class="tc-inner">
            <div class="tc-top"><div class="tc-emoji">🏭</div><div class="tc-type">Fast Fashion</div></div>
            <div class="tc-name">Mass Production Run</div>
            <div class="tc-desc">Flood the market with cheap, trendy pieces. Maximum volume, minimal cost per unit.</div>
            <div class="tc-effects">
              <div class="tc-eff profit">💰 +$30,000 Profit</div>
              <div class="tc-eff pollute">☁️ +10 Pollution</div>
            </div>
          </div>
        </button>
        <button class="t-choice eco-p" onclick="tChoose('eco')">
          <div class="tc-inner">
            <div class="tc-top"><div class="tc-emoji">🌿</div><div class="tc-type">Sustainable</div></div>
            <div class="tc-name">Ethical Collection</div>
            <div class="tc-desc">Use organic materials and fair wages. Slower growth, but customers respect it.</div>
            <div class="tc-effects">
              <div class="tc-eff profit">💰 +$15,000 Profit</div>
              <div class="tc-eff pollute">☁️ +2 Pollution</div>
            </div>
          </div>
        </button>
        <button class="t-choice rec-p" onclick="tChoose('rec')">
          <div class="tc-inner">
            <div class="tc-top"><div class="tc-emoji">♻️</div><div class="tc-type">Recycle</div></div>
            <div class="tc-name">Upcycle Drive</div>
            <div class="tc-desc">Take back old garments and repurpose them. Minimal revenue but actively restores the environment.</div>
            <div class="tc-effects">
              <div class="tc-eff profit">💰 +$5,000 Profit</div>
              <div class="tc-eff reduce">🌿 −8 Pollution</div>
            </div>
          </div>
        </button>
      </div>
      <div class="t-log-panel">
        <div class="t-log-head">Company Log</div>
        <div class="t-log-body" id="tLogBody"></div>
      </div>
    </div>
    <div class="t-right">
      <div class="t-r-section">
        <div class="t-r-title">Consumer Demand</div>
        <div class="demand-bars" id="tDemand"></div>
      </div>
      <div class="t-r-section">
        <div class="t-r-title">Production History</div>
        <div class="hist-chart" id="tHistChart"></div>
      </div>
      <div class="t-r-section">
        <div class="t-r-title">Market Pressure</div>
        <div id="tPressure" style="font-size:.7rem;color:var(--ash);line-height:1.8">Your shareholders want returns. Consumers increasingly demand sustainability.</div>
      </div>
      <div class="t-r-section">
        <div class="t-r-title">Pollution Forecast</div>
        <div id="tForecast" style="font-size:.68rem;color:var(--ash);line-height:1.8">At current pace, you have room to grow.</div>
      </div>
    </div>
  </div>
</div>

<!-- TYCOON END -->
<div class="screen" id="s-tycoon-end">
  <div class="t-end-wrap">
    <div class="t-end-stripe" id="tEndStripe"></div>
    <div class="t-end-hero">
      <div class="t-end-profit-big" id="tEndProfit" style="color:var(--teal)">$0</div>
      <div class="t-end-hero-meta">
        <div class="t-end-hero-label">Final Company Profit</div>
        <div class="t-end-hero-status" id="tEndStatus">—</div>
      </div>
    </div>
    <div class="t-report-card">
      <div class="t-rc-header">
        <div class="t-rc-grade">
          <div class="grade-letter" id="tGradeLetter" style="color:var(--teal)">A</div>
          <div class="grade-label">Grade</div>
        </div>
        <div class="t-rc-title-block">
          <div class="t-rc-verdict" id="tRcVerdict">Verdict</div>
          <div class="rc-title" id="tRcTitle">Title</div>
          <div class="rc-desc" id="tRcDesc">Description</div>
        </div>
      </div>
      <div class="t-rc-stats rc-stats" id="tRcStats"></div>
    </div>
    <div class="t-end-actions">
      <button class="t-end-btn primary" onclick="startTycoon()">▶ Play Again</button>
      <button class="t-end-btn gold-btn" onclick="startGame()">🧥 Closet Game</button>
      <button class="t-end-btn earth-btn" onclick="goEarthAsk()">🌍 Save The Earth</button>
      <button class="t-end-btn" onclick="goSplash()">Main Menu</button>
    </div>
  </div>
</div>

<!-- SAVE THE EARTH — ASK -->
<div class="screen" id="s-earth-ask">
  <div class="ask-wrap">
    <div class="ask-header">
      <div class="ask-eyebrow">🌿 Mini-Game · Arcade · Endless</div>
      <div class="ask-title">Save<span>The Earth</span></div>
      <div class="ask-body">Trees and factories rain from the sky. Move your basket left and right to catch them. Your choices have consequences — just like in real life.</div>
    </div>
    <div class="ask-rules">
      <div class="ask-rule">
        <div class="ask-rule-icon">🌳</div>
        <div class="ask-rule-text"><b>Catch a Tree</b><span>Pollution decreases by 5. Score +10 points. The forest breathes again.</span></div>
      </div>
      <div class="ask-rule">
        <div class="ask-rule-icon">🏭</div>
        <div class="ask-rule-text"><b>Catch a Factory</b><span>Pollution increases by 8. Score −5 points. Dodge these at all costs!</span></div>
      </div>
      <div class="ask-rule">
        <div class="ask-rule-icon">☁️</div>
        <div class="ask-rule-text"><b>Pollution Limit: 100</b><span>If pollution hits 100, the climate collapses and it's game over.</span></div>
      </div>
      <div class="ask-rule">
        <div class="ask-rule-icon">⏱️</div>
        <div class="ask-rule-text"><b>Speed Increases</b><span>Objects fall faster every 30 seconds. Survive as long as you can!</span></div>
      </div>
    </div>
    <div class="ask-actions">
      <button class="btn-earth" onclick="startEarth()">🌍 Play Save The Earth</button>
      <button class="btn-ghost" onclick="goSplash()">← Main Menu</button>
    </div>
  </div>
</div>

<!-- SAVE THE EARTH — GAME -->
<div class="screen" id="s-earth">
  <div class="earth-hud">
    <div class="earth-logo">Save <span>The Earth</span></div>
    <div class="earth-spacer"></div>
    <div class="earth-stat">
      <div class="earth-stat-lbl">Pollution</div>
      <div class="earth-stat-bar earth-poll-track"><div class="earth-stat-fill" id="ePollFill" style="width:0%;background:var(--green)"></div></div>
      <div class="earth-stat-val" id="ePollVal" style="color:var(--green)">0</div>
    </div>
    <div style="border-left:1px solid var(--border);padding-left:14px;display:flex;flex-direction:column;align-items:flex-end">
      <div class="earth-score-lbl">Score</div>
      <div class="earth-score-disp" id="eScoreDisp">0</div>
    </div>
    <div style="border-left:1px solid var(--border);padding-left:14px;display:flex;flex-direction:column;align-items:flex-end">
      <div class="earth-score-lbl">Trees</div>
      <div class="earth-score-disp" id="eTreeDisp" style="color:var(--green)">0</div>
    </div>
    <div style="border-left:1px solid var(--border);padding-left:14px;display:flex;flex-direction:column;align-items:flex-end">
      <div class="earth-score-lbl">Factories</div>
      <div class="earth-score-disp" id="eFactDisp" style="color:var(--red)">0</div>
    </div>
    <button class="earth-pause-btn" id="ePauseBtn" onclick="earthTogglePause()">Pause</button>
  </div>
  <canvas id="earthCanvas"></canvas>
</div>

<!-- SAVE THE EARTH — END -->
<div class="screen" id="s-earth-end">
  <div class="earth-end-wrap">
    <div class="earth-end-header">
      <div class="earth-end-icon" id="earthEndIcon">🌍</div>
      <div class="earth-end-title" id="earthEndTitle" style="color:var(--green)">Well Done!</div>
      <div class="earth-end-sub" id="earthEndSub">You protected the planet from industrial collapse.</div>
    </div>
    <div class="earth-end-stats">
      <div class="earth-end-stat">
        <div class="ees-val" id="eesScore" style="color:var(--gold)">0</div>
        <div class="ees-lbl">Final Score</div>
      </div>
      <div class="earth-end-stat">
        <div class="ees-val" id="eesTrees" style="color:var(--green)">0</div>
        <div class="ees-lbl">Trees Saved</div>
      </div>
      <div class="earth-end-stat">
        <div class="ees-val" id="eesFacts" style="color:var(--red)">0</div>
        <div class="ees-lbl">Factories Hit</div>
      </div>
    </div>
    <div class="earth-end-actions">
      <button class="earth-end-btn primary" onclick="startEarth()">▶ Play Again</button>
      <button class="earth-end-btn" onclick="startGame()">🧥 Closet Game</button>
      <button class="earth-end-btn" onclick="goTycoonIntro()">🏭 Tycoon</button>
      <button class="earth-end-btn" onclick="goSplash()">Main Menu</button>
    </div>
  </div>
</div>

<script>
/* ══ PARTICLE BG ══════════════════════════════════ */
(()=>{
  const c=document.getElementById('bgCanvas'),ctx=c.getContext('2d');let pts=[];
  const rsz=()=>{c.width=innerWidth;c.height=innerHeight};
  const init=()=>{pts=[];for(let i=0;i<50;i++)pts.push({x:Math.random()*c.width,y:Math.random()*c.height,vx:(Math.random()-.5)*.22,vy:(Math.random()-.5)*.22,r:Math.random()*1.1+.3,a:Math.random()*.28+.04})};
  const draw=()=>{ctx.clearRect(0,0,c.width,c.height);pts.forEach(p=>{p.x+=p.vx;p.y+=p.vy;if(p.x<0)p.x=c.width;if(p.x>c.width)p.x=0;if(p.y<0)p.y=c.height;if(p.y>c.height)p.y=0;ctx.beginPath();ctx.arc(p.x,p.y,p.r,0,Math.PI*2);ctx.fillStyle=`rgba(201,169,110,${p.a})`;ctx.fill()});requestAnimationFrame(draw)};
  window.addEventListener('resize',()=>{rsz();init()});rsz();init();draw();
})();

/* ══ SHARED UTILS ══════════════════════════════════ */
function g(id){return document.getElementById(id);}
function clamp(v,mn=0,mx=100){return Math.max(mn,Math.min(mx,v));}
function fmtK(n){return n>=1000?(n/1000).toFixed(0)+'k':n;}
function shuffle(a){for(let i=a.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[a[i],a[j]]=[a[j],a[i]];}return a;}

/* ══ BUG FIX #3: corrected double-negative — earthStop now fires properly ══ */
function show(id){
  if(document.getElementById('s-earth').classList.contains('active') && id!=='s-earth'){
    earthStop();
  }
  document.querySelectorAll('.screen').forEach(s=>{
    s.classList.remove('active');
    if(['s-game','s-end','s-tycoon','s-tycoon-end','s-earth-end'].includes(s.id))s.style.display='';
  });
  const el=document.getElementById(id);
  el.classList.add('active');
  if(id==='s-earth'){el.style.display='block';}
}

function showToast(msg,type){
  document.querySelectorAll('.toast').forEach(t=>t.remove());
  const t=document.createElement('div');t.className='toast '+type;t.textContent=msg;
  document.body.appendChild(t);setTimeout(()=>t.remove(),2200);
}
function goSplash(){earthStop();show('s-splash');}
function goIntro(){show('s-intro');}
function goTycoonIntro(){show('s-tycoon-intro');}
function goEarthAsk(){earthStop();show('s-earth-ask');}

/* ══════════════════════════════════════════════════════
   CLOSET CONSUMERISM v1
══════════════════════════════════════════════════════ */
const SCENARIOS=[
  {head:"CROP TOP GOES VIRAL",price:6,ffE:"👕",ffN:"Polyester Crop Top",ffD:"Made in a sweatshop, will fall apart in 3 washes.",ecoE:"♻️",ecoN:"Thrift a Similar Top",ecoD:"Find it secondhand for $2 or style what you own."},
  {head:"PUFFER JACKET — 80% OFF",price:25,ffE:"🧥",ffN:"Synthetic Puffer",ffD:"Non-recyclable fill. Likely binned next season.",ecoE:"🤝",ecoN:"Borrow a Jacket",ecoD:"Ask a friend. Costs nothing, saves everything."},
  {head:"PARTY DRESS DROP",price:18,ffE:"👗",ffN:"One-Night Dress",ffD:"Worn once. Microplastics shed with every wash.",ecoE:"🏪",ecoN:"Rent or Thrift",ecoD:"Rent for a fraction of cost. Zero waste."},
  {head:"NEW DENIM TREND ALERT",price:12,ffE:"👖",ffN:"Trend Jeans",ffD:"10,000L of water per pair. Out of style in months.",ecoE:"🔧",ecoN:"Repair Your Jeans",ecoD:"Patch, distress, or hem what you already own."},
  {head:"SNEAKER COLLAB DROPS",price:30,ffE:"👟",ffN:"Hype Sneakers",ffD:"Rubber soles take 80 years to decompose.",ecoE:"🛠️",ecoN:"Restore Your Pair",ecoD:"Deep clean your current pair. Good as new."},
  {head:"FLASH SALE: 3 FOR $9",price:9,ffE:"👔",ffN:"3-Pack Shirts",ffD:"Low cost = low wages. Will fade fast.",ecoE:"🎁",ecoN:"Clothes Swap",ecoD:"Swap with friends. Free and social."},
  {head:"BUCKET HAT COMEBACK",price:5,ffE:"🪖",ffN:"Bucket Hat",ffD:"Last season beanies. Next season? Unknown.",ecoE:"🧵",ecoN:"DIY It",ecoD:"Sew one from old fabric. One-of-a-kind."},
  {head:"BLAZER MOMENT",price:22,ffE:"🥼",ffN:"Fast Fashion Blazer",ffD:"Synthetic lining, won't survive dry-cleaning.",ecoE:"🏪",ecoN:"Go Vintage",ecoD:"Quality vintage at thrift stores, same price."},
  {head:"LOUNGEWEAR OBSESSION",price:14,ffE:"🩳",ffN:"Loungewear Set",ffD:"You have pyjamas. This is the algorithm.",ecoE:"😴",ecoN:"Skip It",ecoD:"Wear the cozy clothes you already own."},
  {head:"GRAPHIC TEE COLLAB",price:35,ffE:"🎨",ffN:"Collab Tee",ffD:"'Limited' is marketing. Millions were printed.",ecoE:"🖌️",ecoN:"Customise Your Own",ecoD:"Paint a plain tee. Truly one-of-a-kind."},
  {head:"KNIT SWEATER SEASON",price:16,ffE:"🧶",ffN:"Acrylic Sweater",ffD:"Sheds microplastics into the ocean every wash.",ecoE:"📦",ecoN:"Shop Pre-Loved",ecoD:"Depop, Vinted — zero new waste."},
  {head:"LEGGINGS LAUNCH",price:20,ffE:"🩱",ffN:"Athleisure Leggings",ffD:"Synthetic fabric = microplastics every wash.",ecoE:"🌿",ecoN:"Buy Ethical",ecoD:"Save up, buy once from a certified label."},
  {head:"SILK BLOUSE DUPE",price:8,ffE:"👚",ffN:"Faux Silk Blouse",ffD:"It's polyester. Bought for $8, binned in 8 months.",ecoE:"📦",ecoN:"Rediscover Your Wardrobe",ecoD:"You likely have something similar. Look first."},
  {head:"THE IT JACKET",price:40,ffE:"🧣",ffN:"Statement Jacket",ffD:"'Must-have' until the next drop in 6 weeks.",ecoE:"📚",ecoN:"Capsule Wardrobe",ecoD:"Invest in timeless pieces. Quality over quantity."},
  {head:"IMPULSE AISLE FIND",price:4,ffE:"🧦",ffN:"Socks Multipack",ffD:"Even small purchases add up. Every time.",ecoE:"💚",ecoN:"Mend or Skip",ecoD:"Darn your socks or walk away. Small win, big impact."},
];
const ECO_TIPS=["The fashion industry produces 10% of global carbon emissions — more than aviation and shipping combined.","The average person buys 60% more clothing than 15 years ago, but keeps each item half as long.","It takes 2,700 litres of water to make one cotton T-shirt — enough for one person to drink for 2.5 years.","Only 1% of clothing is recycled into new garments. 73% ends up in landfill or incinerated.","Washing synthetic clothes releases 500,000 tonnes of microfibres into the ocean every year.","A 'capsule wardrobe' of 30-40 versatile pieces can eliminate impulse buying entirely.","Second-hand shopping extends a garment's life by 2 years, reducing its carbon footprint by 24%.",];
const EVENTS=[
  {tag:"📱 Influencer Alert",text:"Your fave influencer just dropped a haul. FF now costs the planet 5 extra health this round.",type:"negative",effect:"ffExtra",val:5},
  {tag:"🌱 Repair Café Opens",text:"A community repair café opened nearby. Sustainable choice gives an extra +5 planet health.",type:"positive",effect:"ecoBonus",val:5},
  {tag:"🌍 Climate News",text:"A major climate report dropped. Eco choices give double points this round.",type:"positive",effect:"ecoPtsX",val:2},
  {tag:"♻️ Swap Event",text:"A local clothes swap is happening! Sustainable choice this round costs the closet nothing.",type:"positive",effect:"ecoFree",val:0},
  {tag:"🧵 DIY Trend",text:"DIY fashion is trending. Sustainable choices earn +50 bonus points this round.",type:"positive",effect:"ecoPtsBonus",val:50},
  {tag:"🗑️ Landfill Report",text:"News reports a nearby landfill overflowing with fast fashion. FF penalty increased by 5.",type:"negative",effect:"ffExtra",val:5},
];
const ACHIEVEMENTS=[
  {id:"first_eco",icon:"🌱",name:"First Step",desc:"Make your first sustainable choice"},
  {id:"streak3",icon:"🔥",name:"On a Roll",desc:"3 eco choices in a row"},
  {id:"streak5",icon:"⚡",name:"Green Machine",desc:"5 eco choices in a row"},
  {id:"no_ff",icon:"🏆",name:"Pure Conscience",desc:"Complete a game without fast fashion"},
  {id:"full_closet",icon:"🧥",name:"Closet Full",desc:"Fill all 10 closet slots"},
  {id:"saved_planet",icon:"🌍",name:"Planet Saviour",desc:"Finish with 90+ planet health"},
  {id:"survivor",icon:"💀",name:"Survivor",desc:"Finish with planet health under 10"},
  {id:"high_score",icon:"⭐",name:"Fashion Economist",desc:"Score over 1500 points"},
  {id:"thrifter",icon:"♻️",name:"Thrift King",desc:"Make 10 sustainable choices in one game"},
  {id:"minimalist",icon:"✨",name:"Minimalist",desc:"End with 3 or fewer items in your closet"},
  {id:"big_spender",icon:"💸",name:"Big Spender",desc:"Spend over $150 on fast fashion"},
  {id:"comeback",icon:"🏅",name:"Comeback Kid",desc:"Recover planet from below 20 back to 60+"},
];
const LEVELS=[
  {pts:0,name:"Newcomer"},{pts:200,name:"Trend Follower"},{pts:500,name:"Conscious Shopper"},
  {pts:900,name:"Eco Advocate"},{pts:1400,name:"Sustainable Hero"},{pts:2000,name:"Fashion Revolutionary"},
];
const DIFF_SETTINGS={
  easy:  {startPlanet:100,ffDmg:8, ecoBuff:8, label:"Easy"},
  normal:{startPlanet:100,ffDmg:10,ecoBuff:5, label:"Normal"},
  hard:  {startPlanet:80, ffDmg:15,ecoBuff:3, label:"Hard"},
};
let selectedDiff='normal';
let G={};
let tipIdx=0;
function setDiff(d){selectedDiff=d;document.querySelectorAll('.diff-btn').forEach(b=>b.classList.remove('active'));g('d-'+d).classList.add('active');}
function newGame(){const diff=DIFF_SETTINGS[selectedDiff];G={round:1,planet:diff.startPlanet,score:0,closet:[],history:[],ff:0,eco:0,discard:0,spent:0,streak:0,maxStreak:0,achievements:new Set(),removeMode:false,pendingScenario:null,order:shuffle([...Array(SCENARIOS.length).keys()]),diff,currentEvent:null,hadBelow20:false};tipIdx=Math.floor(Math.random()*ECO_TIPS.length);}
function sc(){return SCENARIOS[G.order[(G.round-1)%SCENARIOS.length]];}
function getLevel(){let lv=0;for(let i=0;i<LEVELS.length;i++){if(G.score>=LEVELS[i].pts)lv=i;}return lv;}
function levelName(){return LEVELS[getLevel()].name;}
function xpPct(){const lv=getLevel();if(lv>=LEVELS.length-1)return 100;const cur=LEVELS[lv].pts,next=LEVELS[lv+1].pts;return Math.round(((G.score-cur)/(next-cur))*100);}
function addScore(pts){const oldLv=getLevel();G.score=Math.max(0,G.score+pts);if(getLevel()>oldLv){showToast('⬆️ Level Up! '+levelName(),'lvup');addLog('Level up → '+levelName(),'ach','ach',0);}}
function tryAchieve(id){if(G.achievements.has(id))return;const a=ACHIEVEMENTS.find(x=>x.id===id);if(!a)return;G.achievements.add(id);showToast('🏆 '+a.icon+' '+a.name,'ach');addLog('Achievement: '+a.name,'ach','ach',0);addScore(150);renderAchMini();}
function checkAchievements(){if(G.eco>=1)tryAchieve('first_eco');if(G.streak>=3)tryAchieve('streak3');if(G.streak>=5)tryAchieve('streak5');if(G.closet.length>=10)tryAchieve('full_closet');if(G.score>=1500)tryAchieve('high_score');if(G.eco>=10)tryAchieve('thrifter');if(G.spent>=150)tryAchieve('big_spender');if(G.planet<20)G.hadBelow20=true;if(G.hadBelow20&&G.planet>=60)tryAchieve('comeback');}
function renderAchMini(){const el=g('achMini');el.innerHTML='';ACHIEVEMENTS.slice(0,6).forEach(a=>{const div=document.createElement('div');div.className='ach-chip'+(G.achievements.has(a.id)?' unlocked':'');div.innerHTML=`<span class="ach-ico">${a.icon}</span><span class="ach-nm">${a.name}</span>`;div.title=a.desc;el.appendChild(div);});}
function rollEvent(){const eventRounds=[3,6,9,12];if(!eventRounds.includes(G.round)){G.currentEvent=null;return;}G.currentEvent=EVENTS[Math.floor(Math.random()*EVENTS.length)];const b=g('eventBanner');b.className='event-banner show '+G.currentEvent.type;g('eventTag').textContent=G.currentEvent.tag;g('eventText').textContent=G.currentEvent.text;addLog('Event: '+G.currentEvent.tag,'event','event',0);showToast(G.currentEvent.tag+' event!','event-t');}
function showTip(){const box=g('ecoTipBox');if(box.style.display==='none')box.style.display='block';g('ecoTipText').textContent=ECO_TIPS[tipIdx%ECO_TIPS.length];}
function nextTip(){tipIdx++;g('ecoTipText').textContent=ECO_TIPS[tipIdx%ECO_TIPS.length];}
function toggleTip(){const b=g('ecoTipBox');b.style.display=b.style.display==='none'?'block':'none';if(b.style.display==='block')showTip();}
function pColor(p){if(p>=75)return'#52b26a';if(p>=55)return'#8fcc6a';if(p>=35)return'#e8a020';if(p>=15)return'#e06030';return'#e63946';}
function pLabel(p){if(p>=75)return'🌳 Thriving';if(p>=55)return'🌱 Recovering';if(p>=35)return'⚠️ Stressed';if(p>=15)return'🔥 Critical';return'💀 Collapsing';}
function renderAll(){renderPlanet();renderCloset();renderStats();renderScenario();renderDots();renderScore();}
function renderPlanet(){const p=clamp(G.planet),col=pColor(p),lbl=pLabel(p);g('pBig').textContent=p;g('pBig').style.color=col;g('pLbl').textContent=lbl;g('pLbl').style.color=col;g('pBarFill').style.width=p+'%';g('pBarFill').style.background=col;g('hudFill').style.width=p+'%';g('hudFill').style.background=col;g('hudVal').textContent=p;const s=g('pgStop1'),s2=g('pgStop2'),circle=g('planetCircle');if(p>=55){s.setAttribute('stop-color','#52b26a');s2.setAttribute('stop-color','#1a4a28');}else if(p>=35){s.setAttribute('stop-color','#e8a020');s2.setAttribute('stop-color','#78350f');}else if(p>=15){s.setAttribute('stop-color','#e06030');s2.setAttribute('stop-color','#7a2010');}else{s.setAttribute('stop-color','#e63946');s2.setAttribute('stop-color','#7a1a20');}circle.style.animation=p<20?'planetPulse 1s infinite':p<40?'planetPulse 2s infinite':'';}
function renderCloset(){const grid=g('hooksGrid');grid.innerHTML='';g('capNum').textContent=G.closet.length;const pct=(G.closet.length/10)*100;g('capBarFill').style.width=pct+'%';g('capBarFill').style.background=G.closet.length>=8?'var(--red)':G.closet.length>=5?'var(--amber)':'var(--green)';for(let i=0;i<10;i++){const item=G.closet[i];const h=document.createElement('div');h.className='hanger'+(item?' is-'+item.type:'');const wire=document.createElement('div');wire.className='hanger-wire';const box=document.createElement('div');box.className='hanger-item'+(item?' is-'+item.type:' empty');box.textContent=item?item.emoji:'';const tag=document.createElement('div');tag.className='hanger-tag';tag.textContent=item?(item.type==='ff'?'FF':'ECO'):'';if(item&&G.removeMode){box.classList.add('removable');box.title='Discard '+item.name;const idx=i;box.onclick=()=>discardAndBuy(idx);}h.appendChild(wire);h.appendChild(box);h.appendChild(tag);grid.appendChild(h);}}
function renderStats(){g('sRound').textContent=G.round+' / 15';g('sStreak').textContent=G.streak+(G.streak>=3?' 🔥':'');g('sFf').textContent=G.ff;g('sEco').textContent=G.eco;g('sDiscard').textContent=G.discard;g('sSpent').textContent='$'+G.spent;renderMiniBars('bFf',G.history.map(h=>h==='ff'?1:0),'#e63946');renderMiniBars('bEco',G.history.map(h=>h==='eco'?1:0),'#52b26a');const sb=g('streakBadge');if(G.streak>=3){sb.classList.add('show');sb.textContent='🔥 ×'+G.streak+' Streak';}else sb.classList.remove('show');}
function renderScore(){g('scorePts').textContent=G.score;g('scoreLv').textContent='LV '+(getLevel()+1);g('sdPts').textContent=G.score;g('sdLv').textContent='Level '+(getLevel()+1)+' — '+levelName();g('xpFill').style.width=xpPct()+'%';}
function renderDots(){const el=g('gDots');el.innerHTML='';for(let i=0;i<15;i++){const d=document.createElement('div');d.className='dot';if(i<G.history.length)d.classList.add(G.history[i]==='ff'?'d-ff':'d-eco');else if(i===G.round-1)d.classList.add('d-cur');el.appendChild(d);}}
function renderMiniBars(id,data,color){const el=g(id);el.innerHTML='';const last=data.slice(-12);for(let i=0;i<12;i++){const b=document.createElement('div');b.className='m-bar';const v=i<last.length?last[i]:0;b.style.height=(v?20:2)+'px';b.style.background=v?color:'#2c2c2c';el.appendChild(b);}}
function renderScenario(){const s=sc();const ev=G.currentEvent;let pts=100*Math.max(1,Math.floor(G.streak/3)+1);if(ev&&ev.effect==='ecoPtsX')pts*=ev.val;if(ev&&ev.effect==='ecoPtsBonus')pts+=ev.val;g('scEye').textContent='Round '+G.round+' of 15 — '+G.diff.label;g('scHead').textContent=s.head;g('scAmt').textContent=s.price;g('cFfE').textContent=s.ffE;g('cFfN').textContent=s.ffN;g('cFfD').textContent=s.ffD;g('cEcoE').textContent=s.ecoE;g('cEcoN').textContent=s.ecoN;g('cEcoD').textContent=s.ecoD;const ffDmg=G.diff.ffDmg+(ev&&ev.effect==='ffExtra'?ev.val:0);g('cFfPts').textContent='Planet: −'+ffDmg;g('cEcoPts').textContent='Points: +'+pts+(G.streak>=2?' (×'+(Math.floor(G.streak/3)+1)+' combo!)':'');g('cEcoEff').textContent='🟢  +'+G.diff.ecoBuff+' Planet · +'+pts+'pts';setChoiceBtns(true);g('discardWarn').classList.remove('show');}
function setChoiceBtns(on){document.querySelectorAll('.choice').forEach(b=>b.disabled=!on);}
function choose(type){if(G.removeMode)return;const s=sc();if(type==='ff'){if(G.closet.length>=10){G.removeMode=true;G.pendingScenario=s;g('discardWarn').classList.add('show');setChoiceBtns(false);renderCloset();addLog('Closet full — discard a garment first','warn','warn',0);showToast('⚠️ Click a garment to discard','bad');return;}buyFF(s);}else{buyEco(s);}}
function buyFF(s){const ev=G.currentEvent;const dmg=G.diff.ffDmg+(ev&&ev.effect==='ffExtra'?ev.val:0);G.closet.push({emoji:s.ffE,name:s.ffN,type:'ff'});G.planet-=dmg;G.ff++;G.spent+=s.price;G.history.push('ff');G.streak=0;addScore(-50);addLog('Bought '+s.ffN+' $'+s.price,'ff','ff',-dmg);showToast('🛍️ −'+dmg+' Planet','bad');checkAchievements();g('eventBanner').classList.remove('show');finishRound();}
function buyEco(s){const ev=G.currentEvent;let buff=G.diff.ecoBuff+(ev&&ev.effect==='ecoBonus'?ev.val:0);G.planet+=buff;G.eco++;G.streak++;if(G.streak>G.maxStreak)G.maxStreak=G.streak;G.history.push('eco');let pts=100*Math.max(1,Math.floor(G.streak/3)+1);if(ev&&ev.effect==='ecoPtsX')pts*=ev.val;if(ev&&ev.effect==='ecoPtsBonus')pts+=ev.val;addScore(pts);const canAdd=(ev&&ev.effect==='ecoAlwaysAdd')||(G.closet.length<10&&Math.random()>.35);if(canAdd)G.closet.push({emoji:s.ecoE,name:s.ecoN,type:'eco'});addLog((canAdd?'Added: ':'Chose: ')+s.ecoN,'eco','eco',buff);showToast('🌱 +'+buff+' Planet · +'+pts+'pts','good');checkAchievements();g('eventBanner').classList.remove('show');finishRound();}
function discardAndBuy(idx){const gone=G.closet.splice(idx,1)[0];G.discard++;G.planet-=5;addLog('Discarded '+gone.name,'warn','warn',-5);G.removeMode=false;g('discardWarn').classList.remove('show');setChoiceBtns(true);const s=G.pendingScenario;G.pendingScenario=null;buyFF(s);}
function finishRound(){G.planet=clamp(G.planet);renderAll();if(G.planet<=0){addLog('Planet hit zero — game over!','ff','ff',0);setTimeout(endGame,800);return;}if(G.round>=15){setTimeout(endGame,800);return;}G.round++;rollEvent();renderAll();}
function addLog(msg,type,cls,delta){const el=g('logBody'),row=document.createElement('div');row.className='log-row';const now=new Date();const t=String(now.getHours()).padStart(2,'0')+':'+String(now.getMinutes()).padStart(2,'0')+':'+String(now.getSeconds()).padStart(2,'0');const dStr=delta===0?'—':(delta>0?'+'+delta:delta);const dCls=delta>0?'pos':delta<0?'neg':'gld';row.innerHTML=`<span class="log-time">${t}</span><span class="log-text ${cls}">${msg}</span><span class="log-delta ${dCls}">${dStr}</span>`;el.prepend(row);}
function startGame(){newGame();show('s-game');g('logBody').innerHTML='';g('ecoTipBox').style.display='none';renderAll();addLog('Game started ('+G.diff.label+' mode) — 15 rounds','','',0);renderAchMini();}
function endGame(){if(G.ff===0)tryAchieve('no_ff');if(G.planet>=90)tryAchieve('saved_planet');if(G.planet<=10&&G.planet>0)tryAchieve('survivor');if(G.closet.length<=3)tryAchieve('minimalist');const p=clamp(G.planet);const ratio=G.eco/Math.max(1,G.ff+G.eco);show('s-end');let grade,gradeColor,cls,title,desc,stripe;const total=G.eco+G.ff;const pct=total?Math.round((G.eco/total)*100):0;if(p>=80&&ratio>=.7){grade='A+';gradeColor='#52b26a';cls='good';}else if(p>=65&&ratio>=.55){grade='A';gradeColor='#52b26a';cls='good';}else if(p>=50&&ratio>=.4){grade='B';gradeColor='#8fcc6a';cls='good';}else if(p>=35&&ratio>=.3){grade='C';gradeColor='#e8a020';cls='mid';}else if(p>=20){grade='D';gradeColor='#e06030';cls='mid';}else{grade='F';gradeColor='#e63946';cls='bad';}
if(cls==='good'&&grade.startsWith('A')){title='Sustainable Wardrobe';stripe='linear-gradient(90deg,#52b26a,#8fcc6a)';desc="You built a conscious closet. Your choices protected the planet and proved that fashion doesn't have to cost the Earth.";}else if(cls==='good'){title='Eco Conscious';stripe='linear-gradient(90deg,#8fcc6a,#c8e86a)';desc="Mostly good choices with some slip-ups. The planet is recovering. Keep building those sustainable habits.";}else if(cls==='mid'){title='Mixed Signals';stripe='linear-gradient(90deg,#e8a020,#f5cc80)';desc="Half conscious, half consumer. The planet survived — barely. Awareness is step one.";}else{title='Fashion Waste Crisis';stripe='linear-gradient(90deg,#e63946,#c0392b)';desc="Your consumption habits left a trail of textile waste and environmental damage.";}
g('endStripe').style.background=stripe;g('gradeLetter').textContent=grade;g('gradeLetter').style.color=gradeColor;g('rcVerdict').className='rc-verdict '+cls;g('rcVerdict').textContent=cls==='good'?'✦ Great Outcome':cls==='mid'?'◈ Mixed Result':'✖ Bad Outcome';g('rcTitle').textContent=title;g('rcDesc').textContent=desc;const pCol=pColor(p);g('shScore').textContent=G.score;g('shScore').style.color='var(--gold)';g('shStatus').textContent='Level '+(getLevel()+1)+' — '+levelName();g('shBarFill').style.background=pCol;setTimeout(()=>{g('shBarFill').style.width=Math.min(100,(G.score/2000)*100)+'%';},120);
g('rcStats').innerHTML=[{k:'Planet Health',v:p+' / 100',c:p>=60?'grn':p>=30?'gld':'red'},{k:'Final Score',v:G.score,c:'gld'},{k:'Eco Rate',v:pct+'%',c:pct>=60?'grn':'red'},{k:'Best Streak',v:G.maxStreak+'x',c:'grn'},{k:'Fast Fashion',v:G.ff+' buys',c:'red'},{k:'Sustainable',v:G.eco+' times',c:'grn'},{k:'Items Discarded',v:G.discard,c:'red'},{k:'Money Wasted',v:'$'+G.spent,c:'gld'},].map(r=>`<div class="rc-stat"><div class="rc-sk">${r.k}</div><div class="rc-sv ${r.c||''}">${r.v}</div></div>`).join('');
g('achGrid').innerHTML=ACHIEVEMENTS.map(a=>{const ul=G.achievements.has(a.id);return`<div class="ach-end-chip ${ul?'unlocked':'locked'}"><div class="aec-icon">${a.icon}</div><div class="aec-name ${ul?'':'locked'}">${a.name}</div></div>`;}).join('');}
document.addEventListener('keydown',e=>{if(!g('s-game').classList.contains('active'))return;if(e.key==='a'||e.key==='A')choose('ff');if(e.key==='b'||e.key==='B')choose('eco');if(e.key==='t'||e.key==='T')toggleTip();});

/* ══════════════════════════════════════════════════════
   FASHION TYCOON
══════════════════════════════════════════════════════ */
const T_TOTAL=12,T_LIMIT=100;
const COMPANY_NAMES=['LUXE CO.','THREAD INC.','NOVA WEAR','APEX MODE','STITCH CORP','VOGUE INC.'];
const TAGLINES_GOOD=['Crafting responsibly.','Quality over quantity.','Fashion with a conscience.'];
const TAGLINES_BAD=['Growth at any cost.','Move fast, profit faster.','The market demands more.'];
const T_EVENTS=[
  {head:"Q1: SPRING COLLECTION",sub:"Fashion week is over. Your first production decision will define your company culture."},
  {head:"Q2: INFLUENCER PARTNERSHIP",sub:"A major influencer wants to collab. Production volume matters for exclusivity deals."},
  {head:"Q3: SUMMER SALE PREP",sub:"Retailers are placing orders early. How do you meet demand without burning out the planet?"},
  {head:"Q4: COMPETITOR COPIES YOUR DESIGN",sub:"A rival released a knockoff. Do you race to flood the market or take the sustainable high road?"},
  {head:"Q5: SUPPLY CHAIN DISRUPTION",sub:"Your main supplier raised prices. Corners can be cut — but at what cost?"},
  {head:"Q6: FASHION WEEK SPOTLIGHT",sub:"Press is watching. Your collection choice becomes a statement about your brand values."},
  {head:"Q7: CLIMATE REPORT RELEASED",sub:"A damning UN report on textile waste. Consumers are paying attention. Will you?"},
  {head:"Q8: NEW MARKET EXPANSION",sub:"Southeast Asian markets open up. Rapid scaling is possible. So is rapid pollution."},
  {head:"Q9: INVESTOR PRESSURE",sub:"Your backers want 20% growth this quarter. The easy path is cheap and dirty."},
  {head:"Q10: CELEBRITY ENDORSEMENT",sub:"A sustainable celebrity wants to front your brand. But only if you can prove your ethics."},
  {head:"Q11: END OF YEAR PUSH",sub:"Holiday season is here. Every company is in a production sprint. What's your play?"},
  {head:"Q12: THE FINAL QUARTER",sub:"Your legacy as a fashion leader is being written right now. How will history remember you?"},
];
const PRESSURE_MSGS=["Shareholders expect a 15% return. Fast fashion is the easy answer.","Gen-Z consumers rank sustainability higher than price. An opportunity.","A viral thread is calling out fast fashion brands. Tread carefully.","Your eco certification is up for renewal. Audit is coming.","Competitor went fully sustainable — and profit rose 12%.","UN report: fashion industry emits more CO2 than aviation + shipping combined.",];
let T={};
function startTycoon(){T={round:1,pollution:0,profit:0,ffCount:0,ecoCount:0,recCount:0,history:[],company:COMPANY_NAMES[Math.floor(Math.random()*COMPANY_NAMES.length)]};show('s-tycoon');g('tLogBody').innerHTML='';tRenderAll();tAddLog('sys','Company founded. Make your first production decision.','');}
function tRenderAll(){tRenderHud();tRenderLeft();tRenderCenter();tRenderRight();tRenderFactory();}
function pollutionColor(p){if(p<30)return'#52b26a';if(p<55)return'#8fcc6a';if(p<75)return'#e8a020';if(p<90)return'#e06030';return'#e63946';}
function pollutionLabel(p){if(p<30)return'🌤 Clear Skies';if(p<55)return'🌫 Hazy';if(p<75)return'⚠️ Smoggy';if(p<90)return'🔥 Toxic';return'☠️ Crisis Zone';}
function tRenderHud(){const pPct=Math.min(100,(T.pollution/T_LIMIT)*100);const pCol=pollutionColor(T.pollution);g('tHudPollute').style.width=pPct+'%';g('tHudPollute').style.background=pCol;g('tHudPolluteVal').textContent=T.pollution;const prPct=Math.min(100,(T.profit/(T_TOTAL*30000))*100);g('tHudProfit').style.width=prPct+'%';g('tHudProfitVal').textContent='$'+fmtK(T.profit);}
function tRenderLeft(){g('tCompanyName').textContent=T.company;
  /* ══ BUG FIX #1: include recycles in green ratio for tagline ══ */
  const ratio=(T.ecoCount+T.recCount)/Math.max(1,T.ffCount+T.ecoCount+T.recCount);
  g('tCompanyTagline').textContent=ratio>=0.5?TAGLINES_GOOD[T.round%TAGLINES_GOOD.length]:TAGLINES_BAD[T.round%TAGLINES_BAD.length];const col=pollutionColor(T.pollution);g('tPolluteBig').textContent=T.pollution;g('tPolluteBig').style.color=col;g('tPolluteLabel').textContent=pollutionLabel(T.pollution);g('tPolluteLabel').style.color=col;const pPct=Math.min(100,(T.pollution/T_LIMIT)*100);g('tPolluteFill').style.width=pPct+'%';g('tPolluteFill').style.background=col;g('tRound').textContent=T.round+' / '+T_TOTAL;g('tProfit').textContent='$'+fmtK(T.profit);g('tFFCount').textContent=T.ffCount;g('tEcoCount').textContent=T.ecoCount;g('tRecCount').textContent=T.recCount;}
function tRenderCenter(){const ev=T_EVENTS[Math.min(T.round-1,T_EVENTS.length-1)];g('tRoundEye').textContent='Quarter '+T.round+' of '+T_TOTAL;g('tHeadline').textContent=ev.head;g('tSubline').textContent=ev.sub;g('tCrisisWarn').classList.toggle('show',T.pollution>=75);document.querySelectorAll('.t-choice').forEach(b=>b.disabled=false);}
function tRenderRight(){const ffD=clamp(40+T.ffCount*3-T.round*1.5,0,100);const ecoD=clamp(20+T.ecoCount*4+T.round*2,0,100);const recD=clamp(15+T.recCount*5+T.round,0,100);const maxD=Math.max(ffD,ecoD,recD,1);g('tDemand').innerHTML=[{label:'Fast Fashion',val:ffD,color:'#e63946'},{label:'Eco',val:ecoD,color:'#52b26a'},{label:'Recycled',val:recD,color:'#2ec4b6'},].map(d=>`<div class="demand-row"><div class="demand-lbl">${d.label}</div><div class="demand-bar-wrap"><div class="demand-bar-fill" style="width:${(d.val/maxD)*100}%;background:${d.color}"></div></div><div class="demand-val">${Math.round(d.val)}%</div></div>`).join('');const chart=g('tHistChart');chart.innerHTML='';T.history.slice(-10).forEach(type=>{const colors={ff:'#e63946',eco:'#52b26a',rec:'#2ec4b6'};const labels={ff:'FF',eco:'ECO',rec:'REC'};const heights={ff:42,eco:26,rec:16};const div=document.createElement('div');div.className='h-bar-group';div.innerHTML=`<div class="h-bar" style="height:${heights[type]}px;background:${colors[type]};opacity:.8"></div><div class="h-bar-lbl" style="color:${colors[type]}">${labels[type]}</div>`;chart.appendChild(div);});g('tPressure').textContent=PRESSURE_MSGS[T.round%PRESSURE_MSGS.length];const remaining=T_TOTAL-T.round;const headroom=T_LIMIT-T.pollution;if(headroom<=0){g('tForecast').innerHTML='<span style="color:var(--red)">🚨 Pollution limit exceeded!</span>';}else if(remaining===0){g('tForecast').innerHTML='<span style="color:var(--teal)">Final quarter!</span>';}else{const safeFF=Math.floor(headroom/10);g('tForecast').innerHTML=`${remaining} quarters left. At most <strong style="color:var(--red)">${safeFF} more fast-fashion runs</strong>.`;}}
function tRenderFactory(){const slots=12;const html=T.history.slice(-slots).map(type=>{const cls={ff:'ff-u',eco:'eco-u',rec:'rec-u'};const emo={ff:'🏭',eco:'🌿',rec:'♻️'};return`<div class="factory-unit ${cls[type]}">${emo[type]}</div>`;}).join('');const empties=Array(Math.max(0,slots-T.history.length)).fill('<div class="factory-unit empty-u"></div>').join('');g('tFactory').innerHTML=html+empties;}
function tChoose(type){const effects={ff:{profit:30000,pollution:+10},eco:{profit:15000,pollution:+2},rec:{profit:5000,pollution:-8}};const e=effects[type];T.profit+=e.profit;T.pollution=Math.max(0,T.pollution+e.pollution);T.history.push(type);if(type==='ff')T.ffCount++;else if(type==='eco')T.ecoCount++;else T.recCount++;const labels={ff:'Mass Production Run',eco:'Ethical Collection',rec:'Upcycle Drive'};tAddLog(type,labels[type],e.profit);if(type==='ff')showToast('🏭 +$'+fmtK(e.profit)+' | +10 Pollution','bad');else if(type==='eco')showToast('🌿 +$'+fmtK(e.profit)+' | +2 Pollution','good');else showToast('♻️ +$'+fmtK(e.profit)+' | −8 Pollution','info');if(T.pollution>=T_LIMIT){tRenderAll();tAddLog('sys','☠️ Climate crisis triggered!','');setTimeout(()=>endTycoon(false,true),900);return;}if(T.round>=T_TOTAL){tRenderAll();setTimeout(()=>endTycoon(false,false),800);return;}T.round++;tRenderAll();}

function endTycoon(early=false,crisis=false){
  show('s-tycoon-end');
  const p=T.profit,pol=T.pollution;

  /* ══ BUG FIX #2: recycles count as green in ratio → recycle-only run scores A ══ */
  const ratio=(T.ecoCount+T.recCount)/Math.max(1,T.ffCount+T.ecoCount+T.recCount);

  let grade,gradeColor,cls,title,desc,stripe;
  if(crisis){
    grade='F';gradeColor='#e63946';cls='bad';
    title='Climate Crisis';stripe='linear-gradient(90deg,#e63946,#c0392b)';
    desc="Your pollution crossed the point of no return. The climate crisis wiped out consumer confidence.";
  } else if(early){
    grade='—';gradeColor='#888';cls='mid';
    title='Left Early';stripe='linear-gradient(90deg,#888,#555)';
    desc="You stepped away before the game was decided.";
  } else if(ratio>=0.7&&pol<40){
    /* Pure eco/recycle run, very low pollution → A+ */
    grade='A+';gradeColor='#2ec4b6';cls='good';
    title='Green Empire';stripe='linear-gradient(90deg,#2ec4b6,#52b26a)';
    desc="Exceptional. You built a thriving business while actively healing the environment.";
  } else if(ratio>=0.6&&pol<60){
    /* Strong green run → A */
    grade='A';gradeColor='#2ec4b6';cls='good';
    title='Ethical Empire';stripe='linear-gradient(90deg,#2ec4b6,#52b26a)';
    desc="You built a profitable business without sacrificing the environment.";
  } else if(ratio>=0.4||pol<80){
    /* Mixed or moderate → B (was missing — jumped straight to C) */
    grade='B';gradeColor='#8fcc6a';cls='good';
    title='Responsible Producer';stripe='linear-gradient(90deg,#8fcc6a,#c8e86a)';
    desc="More green than not. Your record shows a genuine effort to balance profit with responsibility.";
  } else if(ratio>=0.2||pol<95){
    /* Mostly fast fashion → C */
    grade='C';gradeColor='#e8a020';cls='mid';
    title='Calculated Compromise';stripe='linear-gradient(90deg,#e8a020,#f5cc80)';
    desc="A mixed record. Some green choices, some greedy ones.";
  } else {
    /* Almost all fast fashion, near-crisis pollution → D */
    grade='D';gradeColor='#e06030';cls='bad';
    title='Fast Fashion Baron';stripe='linear-gradient(90deg,#e63946,#e8a020)';
    desc="Rich in profit, bankrupt in conscience.";
  }

  g('tEndStripe').style.background=stripe;
  const pCol=cls==='good'?'#2ec4b6':cls==='mid'?'#e8a020':'#e63946';
  g('tEndProfit').textContent='$'+fmtK(p);
  g('tEndProfit').style.color=pCol;
  g('tEndStatus').textContent=crisis?'☠️ Climate Crisis':pollutionLabel(pol);
  g('tGradeLetter').textContent=grade;
  g('tGradeLetter').style.color=gradeColor;
  g('tRcVerdict').className='t-rc-verdict '+cls;
  g('tRcVerdict').textContent=cls==='good'?'✦ Green Ending':cls==='mid'?'◈ Mixed Verdict':'✖ Bad Ending';
  g('tRcTitle').textContent=title;
  g('tRcDesc').textContent=desc;
  g('tRcStats').innerHTML=[
    {k:'Total Profit',v:'$'+fmtK(p),c:p>200000?'grn':'gld'},
    {k:'Final Pollution',v:pol,c:pol<50?'grn':pol<80?'gld':'red'},
    {k:'Fast Fashion Runs',v:T.ffCount,c:'red'},
    {k:'Eco Runs',v:T.ecoCount,c:'grn'},
    {k:'Recycle Runs',v:T.recCount,c:T.recCount>0?'blue':'red'},
    {k:'Quarters Completed',v:T.history.length+' / '+T_TOTAL,c:'gld'},
  ].map(r=>`<div class="rc-stat"><div class="rc-sk">${r.k}</div><div class="rc-sv ${r.c||''}">${r.v}</div></div>`).join('');
}

function tAddLog(type,msg,profit){const el=g('tLogBody'),row=document.createElement('div');row.className='t-log-row';const types={ff:'ff',eco:'eco',rec:'rec',sys:'sys'};const labels={ff:'FF',eco:'ECO',rec:'REC',sys:'SYS'};const profStr=profit?'+$'+fmtK(profit):'';row.innerHTML=`<span class="t-log-type ${types[type]||'sys'}">${labels[type]||'SYS'}</span><span class="t-log-msg">${msg}</span><span class="t-log-profit">${profStr}</span>`;el.prepend(row);}

/* ══════════════════════════════════════════════════════
   SAVE THE EARTH
══════════════════════════════════════════════════════ */
let E = {};
let earthAnimId = null;
let earthKeys = {};

const SPRITE_SIZE = 52;
let _spriteTree = null, _spriteFactory = null, _spriteBasket = null;
let _basketW = 100, _basketH = 44;

function buildSprites(){
  _spriteTree = document.createElement('canvas');
  _spriteTree.width = _spriteTree.height = SPRITE_SIZE;
  const tc = _spriteTree.getContext('2d');
  tc.font = `${SPRITE_SIZE-4}px serif`;
  tc.textAlign = 'center'; tc.textBaseline = 'middle';
  tc.fillText('🌳', SPRITE_SIZE/2, SPRITE_SIZE/2);

  _spriteFactory = document.createElement('canvas');
  _spriteFactory.width = _spriteFactory.height = SPRITE_SIZE;
  const fc = _spriteFactory.getContext('2d');
  fc.font = `${SPRITE_SIZE-4}px serif`;
  fc.textAlign = 'center'; fc.textBaseline = 'middle';
  fc.fillText('🏭', SPRITE_SIZE/2, SPRITE_SIZE/2);

  _spriteBasket = document.createElement('canvas');
  _spriteBasket.width = _basketW + 20;
  _spriteBasket.height = _basketH + 20;
  const bc = _spriteBasket.getContext('2d');
  const bw = _basketW, bh = _basketH, ox = 10, oy = 10;

  bc.shadowColor = 'rgba(82,178,106,0.55)';
  bc.shadowBlur = 14;
  bc.beginPath();
  bc.moveTo(ox+8, oy);
  bc.lineTo(ox+bw-8, oy);
  bc.lineTo(ox+bw, oy+bh);
  bc.lineTo(ox, oy+bh);
  bc.closePath();
  bc.fillStyle = 'rgba(22,36,22,0.94)';
  bc.fill();
  bc.strokeStyle = '#52b26a';
  bc.lineWidth = 2.5;
  bc.stroke();
  bc.shadowBlur = 0;

  bc.strokeStyle = 'rgba(82,178,106,0.22)';
  bc.lineWidth = 1;
  for(let i=1;i<4;i++){
    const y=oy+bh*i/4;
    bc.beginPath();bc.moveTo(ox+i*2,y);bc.lineTo(ox+bw-i*2,y);bc.stroke();
  }
  for(let i=1;i<7;i++){
    const x=ox+bw*i/7;
    bc.beginPath();bc.moveTo(x,oy);bc.lineTo(x,oy+bh);bc.stroke();
  }
  bc.strokeStyle = 'rgba(160,240,180,0.35)';
  bc.lineWidth = 1.5;
  bc.beginPath();bc.moveTo(ox+8,oy+1);bc.lineTo(ox+bw-8,oy+1);bc.stroke();
}

let _bgCanvas = null, _bgLastPoll = -1;
function getCachedBg(w, h, pollPct){
  if(!_bgCanvas || _bgCanvas.width!==w || _bgCanvas.height!==h || Math.abs(pollPct-_bgLastPoll)>0.005){
    if(!_bgCanvas) _bgCanvas = document.createElement('canvas');
    _bgCanvas.width = w; _bgCanvas.height = h;
    _bgLastPoll = pollPct;
    const bc = _bgCanvas.getContext('2d');

    const r1=Math.floor(8+pollPct*65), g1=Math.floor(8+pollPct*10), b1=Math.floor(20-pollPct*18);
    const grad = bc.createLinearGradient(0,0,0,h);
    grad.addColorStop(0,`rgb(${r1},${g1},${b1})`);
    grad.addColorStop(1,`rgb(${Math.floor(r1*.45)},${Math.floor(g1*.4)},${Math.floor(b1*.5)})`);
    bc.fillStyle = grad; bc.fillRect(0,0,w,h);

    const starAlpha = Math.max(0,(1-pollPct*1.8)*0.55);
    if(E.stars && starAlpha>0.01){
      E.stars.forEach(s=>{
        bc.beginPath(); bc.arc(s.x,s.y,s.r,0,Math.PI*2);
        bc.fillStyle=`rgba(255,255,255,${(s.a*starAlpha).toFixed(3)})`; bc.fill();
      });
    }

    if(pollPct>0.25){
      const sa=(pollPct-0.25)/0.75*0.42;
      const smog=bc.createLinearGradient(0,0,0,h*0.45);
      smog.addColorStop(0,`rgba(210,130,30,${sa})`);
      smog.addColorStop(1,'rgba(0,0,0,0)');
      bc.fillStyle=smog; bc.fillRect(0,0,w,h*0.45);
    }

    const gc1=pollPct>0.55?'rgba(80,40,10,1)':'rgba(28,58,18,1)';
    const gc2=pollPct>0.55?'rgba(48,22,4,1)':'rgba(12,32,8,1)';
    const gg=bc.createLinearGradient(0,h-32,0,h);
    gg.addColorStop(0,gc1); gg.addColorStop(1,gc2);
    bc.fillStyle=gg; bc.fillRect(0,h-32,w,32);
  }
  return _bgCanvas;
}

function spawnLabel(x, y, text, color){
  E.labels.push({x, y, vy:-2.2, life:1, text, color});
}

function startEarth(){
  show('s-earth');
  buildSprites();
  _bgLastPoll = -1;
  _bgCanvas = null;

  const canvas = g('earthCanvas');
  const hud = document.querySelector('.earth-hud');
  const hudH = hud ? hud.offsetHeight : 50;
  canvas.width = window.innerWidth;
  canvas.height = window.innerHeight - hudH;

  E = {
    canvas,
    ctx: canvas.getContext('2d', {alpha:false}),
    w: canvas.width,
    h: canvas.height,
    bx: canvas.width/2,
    by: canvas.height - 76,
    bw: _basketW,
    bh: _basketH,
    bspeed: 14,
    targetBx: canvas.width/2,
    pollution: 0,
    score: 0,
    trees: 0,
    factories: 0,
    objects: [],
    particles: [],
    labels: [],
    spawnTimer: 0,
    frameCount: 0,
    baseSpeed: 4.5,
    speedLevel: 1,
    gameOver: false,
    paused: false,
    hudTimer: 0,
    stars: Array.from({length:70},()=>({
      x:Math.random()*canvas.width,
      y:Math.random()*canvas.height,
      r:Math.random()*1.4+.4,
      a:Math.random()*.9+.1
    })),
  };

  earthKeys = {};
  document.addEventListener('keydown', earthKeyDown);
  document.addEventListener('keyup', earthKeyUp);
  canvas.addEventListener('mousemove', earthMouse);
  canvas.addEventListener('touchmove', earthTouch, {passive:true});
  canvas.addEventListener('touchstart', earthTouch, {passive:true});
  window.addEventListener('resize', earthOnResize);

  if(earthAnimId) cancelAnimationFrame(earthAnimId);
  earthLoop();
}

function earthOnResize(){
  if(!E.canvas) return;
  const hud = document.querySelector('.earth-hud');
  const hudH = hud ? hud.offsetHeight : 50;
  E.canvas.width = E.w = window.innerWidth;
  E.canvas.height = E.h = window.innerHeight - hudH;
  E.by = E.h - 76;
  E.bx = clamp(E.bx, E.bw/2, E.w - E.bw/2);
  E.stars = Array.from({length:70},()=>({x:Math.random()*E.w,y:Math.random()*E.h,r:Math.random()*1.4+.4,a:Math.random()*.9+.1}));
  _bgCanvas = null;
}

function earthKeyDown(e){ earthKeys[e.key]=true; }
function earthKeyUp(e){   earthKeys[e.key]=false; }

function earthMouse(e){
  if(!E.canvas||E.gameOver||E.paused) return;
  E.targetBx = e.offsetX;
}
function earthTouch(e){
  if(!E.canvas||E.gameOver||E.paused) return;
  const rect = E.canvas.getBoundingClientRect();
  E.targetBx = e.touches[0].clientX - rect.left;
}

function earthTogglePause(){
  E.paused = !E.paused;
  g('ePauseBtn').textContent = E.paused ? 'Resume' : 'Pause';
  if(!E.paused) earthLoop();
}

function earthStop(){
  if(earthAnimId){ cancelAnimationFrame(earthAnimId); earthAnimId=null; }
  document.removeEventListener('keydown', earthKeyDown);
  document.removeEventListener('keyup', earthKeyUp);
  window.removeEventListener('resize', earthOnResize);
  if(E.canvas){
    E.canvas.removeEventListener('mousemove', earthMouse);
    E.canvas.removeEventListener('touchmove', earthTouch);
    E.canvas.removeEventListener('touchstart', earthTouch);
  }
  E = {};
}

function earthSpawnObject(){
  const isTree = Math.random() < 0.56;
  const sz = SPRITE_SIZE;
  E.objects.push({
    x:  sz/2 + Math.random() * (E.w - sz),
    y:  -sz,
    vy: E.baseSpeed * E.speedLevel * (0.75 + Math.random()*0.65),
    vx: (Math.random()-.5) * 1.4,
    type: isTree ? 'tree' : 'factory',
    rot: Math.random() * Math.PI * 2,
    rotV: (Math.random()-.5) * 0.07,
    wo: Math.random() * Math.PI * 2,
    woV: 0.045 + Math.random()*0.03,
  });
}

function earthSpawnParticles(x, y, type){
  const col = type==='tree' ? [82,178,106] : [230,57,70];
  const n = 18;
  for(let i=0;i<n;i++){
    const a = (i/n)*Math.PI*2 + Math.random()*.4;
    const sp = 2.5 + Math.random()*5;
    E.particles.push({
      x, y,
      vx: Math.cos(a)*sp,
      vy: Math.sin(a)*sp - 1,
      r: 3 + Math.random()*5,
      life: 1,
      decay: 0.038 + Math.random()*0.032,
      r0: col[0], g0: col[1], b0: col[2],
    });
  }
}

function earthLoop(){
  if(!E.ctx || E.gameOver) return;
  if(E.paused){
    const {ctx,w,h} = E;
    ctx.fillStyle = 'rgba(0,0,0,0.62)';
    ctx.fillRect(0,0,w,h);
    ctx.fillStyle = '#f0ebe3';
    ctx.font = '48px "Bebas Neue", sans-serif';
    ctx.textAlign = 'center'; ctx.textBaseline = 'middle';
    ctx.fillText('PAUSED', w/2, h/2-18);
    ctx.fillStyle = '#777';
    ctx.font = '13px "DM Mono", monospace';
    ctx.fillText('CLICK RESUME TO CONTINUE', w/2, h/2+22);
    return;
  }

  const {ctx, w, h} = E;
  E.frameCount++;

  E.speedLevel = 1 + Math.floor(E.frameCount / 480) * 0.3;

  if(earthKeys['ArrowLeft']  || earthKeys['a'] || earthKeys['A']) E.bx -= E.bspeed;
  if(earthKeys['ArrowRight'] || earthKeys['d'] || earthKeys['D']) E.bx += E.bspeed;
  if(E.targetBx !== undefined){
    E.bx += (E.targetBx - E.bx) * 0.28;
  }
  E.bx = clamp(E.bx, E.bw/2, w - E.bw/2);

  E.spawnTimer++;
  const spawnInterval = Math.max(10, 28 - Math.floor(E.frameCount/360)*2);
  if(E.spawnTimer >= spawnInterval){
    E.spawnTimer = 0;
    earthSpawnObject();
    if(Math.random() < 0.18) earthSpawnObject();
  }

  const bLeft = E.bx - E.bw/2, bRight = E.bx + E.bw/2;
  const bTop  = E.by - E.bh/2, bBot   = E.by + E.bh/2;
  const half  = SPRITE_SIZE * 0.42;

  let i = E.objects.length;
  while(i--){
    const obj = E.objects[i];
    obj.x  += obj.vx;
    obj.y  += obj.vy;
    obj.rot += obj.rotV;
    obj.wo  += obj.woV;

    if(obj.x < half)       { obj.x = half;    obj.vx =  Math.abs(obj.vx); }
    if(obj.x > w - half)   { obj.x = w-half;  obj.vx = -Math.abs(obj.vx); }

    if(obj.y + half > bTop && obj.y - half < bBot &&
       obj.x + half > bLeft && obj.x - half < bRight){
      E.objects.splice(i, 1);
      earthSpawnParticles(obj.x, obj.y, obj.type);
      if(obj.type === 'tree'){
        E.pollution = Math.max(0, E.pollution - 5);
        E.score += 10;
        E.trees++;
        spawnLabel(obj.x, bTop-10, '+10  −5☁', '#6ee896');
      } else {
        E.pollution = Math.min(100, E.pollution + 8);
        E.score = Math.max(0, E.score - 5);
        E.factories++;
        spawnLabel(obj.x, bTop-10, '−5  +8☁', '#f5a0a5');
      }
      continue;
    }

    if(obj.y > h + SPRITE_SIZE){
      E.objects.splice(i, 1);
      if(obj.type === 'tree'){
        E.pollution = Math.min(100, E.pollution + 2);
        spawnLabel(obj.x, h - 40, 'missed! +2☁', '#e8a020');
      }
    }
  }

  i = E.particles.length;
  while(i--){
    const p = E.particles[i];
    p.x += p.vx; p.y += p.vy; p.vy += 0.18;
    p.life -= p.decay;
    if(p.life <= 0) E.particles.splice(i,1);
  }

  i = E.labels.length;
  while(i--){
    const lb = E.labels[i];
    lb.y += lb.vy; lb.vy *= 0.94; lb.life -= 0.03;
    if(lb.life <= 0) E.labels.splice(i,1);
  }

  E.hudTimer++;
  if(E.hudTimer >= 4){
    E.hudTimer = 0;
    const pollRound = Math.round(E.pollution);
    const pollCol = E.pollution<50?'#52b26a':E.pollution<80?'#e8a020':'#e63946';
    const pf = g('ePollFill'), pv = g('ePollVal');
    pf.style.cssText = `width:${E.pollution}%;background:${pollCol};height:100%;border-radius:3px;transition:none`;
    pv.textContent = pollRound;
    pv.style.color = pollCol;
    g('eScoreDisp').textContent = E.score;
    g('eTreeDisp').textContent  = E.trees;
    g('eFactDisp').textContent  = E.factories;
  }

  const pollPct = E.pollution / 100;
  ctx.drawImage(getCachedBg(w, h, pollPct), 0, 0);

  ctx.save();
  for(let j=0; j<E.objects.length; j++){
    const obj = E.objects[j];
    const sprite = obj.type==='tree' ? _spriteTree : _spriteFactory;
    const wobX = Math.sin(obj.wo) * 4;
    ctx.setTransform(
      Math.cos(obj.rot), Math.sin(obj.rot),
      -Math.sin(obj.rot), Math.cos(obj.rot),
      obj.x + wobX, obj.y
    );
    ctx.drawImage(sprite, -SPRITE_SIZE/2, -SPRITE_SIZE/2);
  }
  ctx.setTransform(1,0,0,1,0,0);
  ctx.restore();

  if(E.particles.length){
    ctx.save();
    for(let j=0;j<E.particles.length;j++){
      const p = E.particles[j];
      ctx.globalAlpha = p.life * p.life;
      ctx.fillStyle = `rgb(${p.r0},${p.g0},${p.b0})`;
      ctx.beginPath();
      ctx.arc(p.x, p.y, p.r * p.life + 1, 0, Math.PI*2);
      ctx.fill();
    }
    ctx.globalAlpha = 1;
    ctx.restore();
  }

  ctx.drawImage(
    _spriteBasket,
    Math.round(E.bx - _basketW/2 - 10),
    Math.round(E.by - _basketH/2 - 10)
  );

  if(E.labels.length){
    ctx.save();
    ctx.font = 'bold 14px "DM Mono",monospace';
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    for(let j=0;j<E.labels.length;j++){
      const lb = E.labels[j];
      ctx.globalAlpha = lb.life;
      ctx.fillStyle = lb.color;
      ctx.shadowColor = 'rgba(0,0,0,0.7)';
      ctx.shadowBlur = 4;
      ctx.fillText(lb.text, lb.x, lb.y);
    }
    ctx.globalAlpha = 1; ctx.shadowBlur = 0;
    ctx.restore();
  }

  {
    const barW=w*0.38, barH=7, barX=(w-barW)/2, barY=h-16;
    ctx.fillStyle='rgba(0,0,0,0.55)';
    ctx.fillRect(barX-2, barY-2, barW+4, barH+4);
    const pCol=pollPct<0.5?'#52b26a':pollPct<0.8?'#e8a020':'#e63946';
    ctx.fillStyle=pCol;
    ctx.fillRect(barX, barY, barW*pollPct, barH);
    ctx.strokeStyle='rgba(255,255,255,0.15)';
    ctx.lineWidth=1;
    ctx.strokeRect(barX, barY, barW, barH);
  }

  if(E.pollution >= 100){
    E.gameOver = true;
    endEarth(false);
    return;
  }

  earthAnimId = requestAnimationFrame(earthLoop);
}

function endEarth(won){
  cancelAnimationFrame(earthAnimId); earthAnimId=null;
  document.removeEventListener('keydown', earthKeyDown);
  document.removeEventListener('keyup', earthKeyUp);
  window.removeEventListener('resize', earthOnResize);

  const score=E.score, trees=E.trees, facts=E.factories, poll=Math.round(E.pollution);
  show('s-earth-end');

  let icon,title,sub,titleColor;
  if(!won || poll>=100){
    icon='☠️'; title='Planet Lost'; titleColor='#e63946';
    sub="Pollution reached critical mass. The climate collapsed. "+facts+" factories caught vs "+trees+" trees saved.";
  } else if(trees > facts*2){
    icon='🌲'; title='Forest Guardian'; titleColor='#52b26a';
    sub="Remarkable! You caught "+trees+" trees and dodged most factories. The planet is healing.";
  } else if(score > 200){
    icon='🌍'; title='Earth Protector'; titleColor='#52b26a';
    sub="Great work protecting the planet. "+trees+" trees saved, "+facts+" factories unfortunately caught.";
  } else {
    icon='🌱'; title='Decent Effort'; titleColor='#8fcc6a';
    sub="You kept the planet alive. "+trees+" trees saved. Next time, dodge those factories!";
  }

  g('earthEndIcon').textContent = icon;
  g('earthEndTitle').textContent = title;
  g('earthEndTitle').style.color = titleColor;
  g('earthEndSub').textContent = sub;
  g('eesScore').textContent = score;
  g('eesTrees').textContent = trees;
  g('eesFacts').textContent = facts;
}
</script>
</body>
</html>"""

# Render at full viewport height
components.html(GAME_HTML, height=900, scrolling=False)