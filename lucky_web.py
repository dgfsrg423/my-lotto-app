import streamlit as st
import time
import base64

# --- 1. 頁面基礎設置 (隱藏所有 Streamlit 預設元件) ---
st.set_page_config(page_title="ARASAKA-RELIQUE-TERMINAL", layout="wide")

# --- 2. CSS 終極封裝：包含背景、發光、掃描線與故障效果 ---
def apply_cyber_theme():
    st.markdown(
        f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Share+Tech+Mono&display=swap');

        /* 全螢幕背景與濾鏡 */
        .stApp {{
            background: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), 
                        url("你的4K背景連結");
            background-size: cover;
            background-position: center;
            color: #00ff9f;
            font-family: 'Share+Tech+Mono', monospace;
        }}

        /* 掃描線動畫 (Scanline Effect) */
        .stApp::after {{
            content: " ";
            display: block;
            position: absolute;
            top: 0; left: 0; bottom: 0; right: 0;
            background: linear-gradient(rgba(18, 16, 16, 0) 50%, rgba(0, 0, 0, 0.1) 50%);
            background-size: 100% 4px;
            z-index: 100;
            pointer-events: none;
            opacity: 0.3;
        }}

        /* 自定義按鈕：賽博黃與切角設計 */
        .stButton>button {{
            background: #fcee0a;
            color: #000;
            font-family: 'Orbitron', sans-serif;
            font-weight: bold;
            border: none;
            border-radius: 0px;
            clip-path: polygon(15% 0, 100% 0, 100% 70%, 85% 100%, 0 100%, 0% 30%);
            padding: 10px 30px;
            transition: 0.2s;
            width: 100%;
        }}
        .stButton>button:hover {{
            background: #00f0ff; /* 霓虹藍 */
            box-shadow: 0 0 15px #00f0ff;
            color: #000;
        }}

        /* 輸入框樣式 */
        .stTextInput>div>div>input {{
            background-color: rgba(0, 255, 159, 0.1);
            color: #00ff9f;
            border: 1px solid #00ff9f;
        }}

        /* 隱藏標記 */
        #MainMenu, footer, header {{visibility: hidden;}}
        </style>
        """,
        unsafe_allow_html=True
    )

apply_cyber_theme()

# --- 3. 核心功能邏輯 ---
def slow_type(text, speed=0.04):
    placeholder = st.empty()
    full_text = ""
    for char in text:
        full_text += char
        placeholder.markdown(f"#### `> {full_text}_`")
        time.sleep(speed)

# --- 4. 側邊欄：音樂控制器 ---
with st.sidebar:
    st.markdown("### 💿 NEURAL LINK ACTIVE")
    st.write("🎵 **Now Playing:** *Been Good to Know Ya*")
    # 這裡放你的音樂
    st.audio("你的音樂連結.mp3") 
    st.divider()
    st.markdown("##### [SYSTEM STATUS: CRITICAL]")
    st.progress(24) # 模擬系統快要崩潰的進度條

# --- 5. 主畫面：最後遺言備份 ---
st.markdown("<h1 style='text-align: center; color: #fcee0a; text-shadow: 3px 3px #ff003c;'>[ RELIC STORAGE UNIT ]</h1>", unsafe_allow_html=True)
st.write("---")

col1, col2 = st.columns([2, 1])

with col1:
    user_input = st.text_input("輸入你想留下的最後訊息 (Input Message to Arasaka Cloud):", placeholder="Goodbye, Night City...")
    
    if st.button("啟動資料備份 (UPLOAD TO RELIC)"):
        if user_input:
            slow_type("正在初始化神經連結...")
            time.sleep(0.5)
            slow_type("加密封裝中: SHA-256 [賽博編碼]...")
            time.sleep(0.5)
            slow_type(f"警告：正在將訊息 '{user_input}' 寫入靈魂殺手 (Soulkiller)...")
            time.sleep(1)
            st.success("備份完成。你在這個世界上留下了印記。")
            st.warning("ERROR: System Integrity 0% - Connecting to Mikoshi...")
        else:
            st.error("請輸入訊息以啟動備份。")

with col2:
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJ4eG14eG14eG14eG14eG14eG14eG14eG14eG14eG14JnB2PTEmZXA9djFfaW50ZXJuYWxfZ2lmX2J5X2lkJmN0PWc/vVzH2XY3m0EJG/giphy.gif", caption="Neural Link Processing...")
