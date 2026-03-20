import streamlit as st
import time
import base64

# --- 1. [SYSTEM INITIALIZATION] ---
st.set_page_config(page_title="RELIC_OS_TERMINAL", layout="wide", initial_sidebar_state="collapsed")

def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        return base64.b64encode(f.read()).decode()

# --- 2. [ULTRA-CUSTOM CYBER_CSS] ---
def inject_god_mode_ui(bg_file):
    bg_base64 = get_base64(bg_file)
    st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Fira+Code:wght@300;500&family=Syncopate:wght@400;700&display=swap');

    /* 全域背景：動態背景 + 掃描線 + 色散濾鏡 */
    .stApp {{
        background: linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.7)), 
                    url("data:image/gif;base64,{bg_base64}");
        background-size: cover;
        font-family: 'Fira Code', monospace;
        color: #00ff9f;
        cursor: crosshair;
    }}

    /* 故障藝術效果 (Glitch Animation) */
    @keyframes glitch {{
        0% {{ transform: translate(0); text-shadow: -2px 0 red, 2px 0 blue; }}
        20% {{ transform: translate(-2px, 2px); }}
        100% {{ transform: translate(0); }}
    }}

    .glitch-header {{
        font-family: 'Syncopate', sans-serif;
        font-size: 4rem;
        text-align: center;
        color: white;
        letter-spacing: 15px;
        animation: glitch 1s infinite linear alternate-reverse;
        margin-top: 10vh;
    }}

    /* 輸入框與組件透明化 */
    .stTextInput>div>div>input {{
        background: rgba(0, 20, 20, 0.6) !important;
        border: 1px solid #00ff9f !important;
        color: #ff003c !important;
        font-size: 1.2rem;
        border-radius: 0;
    }}

    /* 偽裝成「義體按鈕」的 CSS */
    .stButton>button {{
        background: transparent;
        color: #00ff9f;
        border: 1px solid #00ff9f;
        padding: 20px;
        font-weight: bold;
        text-transform: uppercase;
        letter-spacing: 5px;
        position: relative;
        overflow: hidden;
        transition: 0.5s;
    }}
    .stButton>button:hover {{
        background: #00ff9f;
        color: black;
        box-shadow: 0 0 50px #00ff9f;
    }}

    /* 隱藏所有垃圾介面 */
    header, footer, [data-testid="stSidebarNav"] {{ visibility: hidden; }}
    
    /* 右下角浮動音樂監控器 */
    [data-testid="stAudio"] {{
        position: fixed;
        bottom: 20px;
        right: 20px;
        opacity: 0.2;
        filter: invert(1);
    }}
    </style>
    """, unsafe_allow_html=True)

# 助理，確認檔案在那裡
try:
    inject_god_mode_ui('bg_motion.gif')
except:
    st.warning("⚠️ 系統偵測到遺失動態背景路徑，請助理儘速補齊。")

# --- 3. [SYSTEM LOGIC: NEURAL SYNC] ---
def terminal_print(text, type="info"):
    colors = {{"info": "#00ff9f", "error": "#ff003c", "warning": "#fcee0a"}}
    placeholder = st.empty()
    full_text = ""
    for char in text:
        full_text += char
        placeholder.markdown(f'<p style="color:{colors[type]}; margin:0;"><b>[SYS_LOG]:</b> {full_text}_</p>', unsafe_allow_html=True)
        time.sleep(0.02)

# --- 4. [MAIN INTERFACE] ---
st.markdown('<h1 class="glitch-header">RELIC_OS</h1>', unsafe_allow_html=True)
st.write(f"<p style='text-align:center; letter-spacing:10px;'>PROTOCOL: {time.strftime('%Y-%m-%d %H:%M:%S')}</p>", unsafe_allow_html=True)

# 系統狀態欄
cols = st.columns(4)
with cols[0]: st.metric("Neural Sync", "98.4%", "0.2%")
with cols[1]: st.metric("Buffer", "1024GB", "-12MB")
with cols[2]: st.metric("User ID", "V_077")
with cols[3]: st.metric("Status", "DYING")

st.divider()

# 交互區
c1, c2 = st.columns([2, 1])
with c1:
    message = st.text_input("ENTER FRAGMENT TO ENCRYPT:", placeholder="Type your last words...")
    if st.button("EXECUTE SOULKILLER"):
        if message:
            terminal_print("正在存取核心神經記憶體...")
            time.sleep(0.5)
            terminal_print(f"寫入中: {message}", type="warning")
            time.sleep(1)
            terminal_print("備份成功。強尼銀手向你致意。", type="info")
            st.toast("Data Saved to Mikoshi.")
        else:
            terminal_print("錯誤: 無法上傳空白數據。", type="error")

with c2:
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJ4eG14eG14eG14eG14eG14eG14eG14eG14eG14eG14JnB2PTEmZXA9djFfaW50ZXJuYWxfZ2lmX2J5X2lkJmN0PWc/vVzH2XY3m0EJG/giphy.gif")

# 音樂注入
st.audio("main_theme.mp3")
