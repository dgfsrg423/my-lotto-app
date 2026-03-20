import streamlit as st
import time
import random

# --- 1. 頁面基礎設置 ---
st.set_page_config(page_title="ARASAKA-RELIQUE-TERMINAL", layout="wide")

# --- 2. CSS 修正 (背景圖路徑對準 gb.jpg.jpg) ---
def apply_cyber_theme():
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Share+Tech+Mono&display=swap');

        /* 背景與濾鏡 */
        .stApp {
            background: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)), 
                        url("app/static/gb.jpg.jpg"); /* 修正路徑 */
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            color: #00ff9f;
            font-family: 'Share+Tech+Mono', monospace;
        }

        /* 掃描線動畫 */
        .stApp::after {
            content: " ";
            display: block;
            position: fixed;
            top: 0; left: 0; bottom: 0; right: 0;
            background: linear-gradient(rgba(18, 16, 16, 0) 50%, rgba(0, 0, 0, 0.1) 50%);
            background-size: 100% 4px;
            z-index: 100;
            pointer-events: none;
            opacity: 0.3;
        }

        /* 霓虹標題 */
        .glitch-title {
            text-align: center;
            color: #fcee0a;
            text-shadow: 3px 3px #ff003c;
            font-family: 'Orbitron', sans-serif;
            font-size: 3rem;
            margin-bottom: 30px;
        }

        /* 賽博切角按鈕 */
        .stButton>button {
            background: #fcee0a;
            color: #000;
            font-family: 'Orbitron', sans-serif;
            font-weight: bold;
            border: none;
            clip-path: polygon(15% 0, 100% 0, 100% 70%, 85% 100%, 0 100%, 0% 30%);
            padding: 12px 30px;
            transition: 0.3s;
            width: 100%;
        }
        .stButton>button:hover {
            background: #00f0ff;
            box-shadow: 0 0 20px #00f0ff;
            color: #000;
            transform: scale(1.02);
        }

        /* 隱藏預設元件 */
        #MainMenu, footer, header {visibility: hidden;}
        </style>
        """,
        unsafe_allow_html=True
    )

apply_cyber_theme()

# --- 3. 打字機效果函數 ---
def slow_type(text, speed=0.03):
    placeholder = st.empty()
    full_text = ""
    for char in text:
        full_text += char
        placeholder.markdown(f"#### `> {full_text}_`")
        time.sleep(speed)

# --- 4. 側邊欄：音樂播放 (修正為 music.mp3.mp3) ---
with st.sidebar:
    st.markdown("### 💿 NEURAL LINK")
    st.write("🎵 **OST:** *Been Good to Know Ya*")
    # 對準你的檔案名稱
    st.audio("music.mp3.mp3") 
    st.divider()
    st.markdown("##### [SYSTEM: CRITICAL]")
    st.progress(15)

# --- 5. 主介面 ---
st.markdown('<div class="glitch-title">[ RELIC BACKUP TERMINAL ]</div>', unsafe_allow_html=True)

col1, col2 = st.columns([2, 1])

with col1:
    user_input = st.text_input("輸入要備份到神經雲端的訊息:", placeholder="Wake up, Samurai...")
    
    if st.button("啟動遺言封裝 (INITIATE ARCHIVE)"):
        if user_input:
            slow_type("正在連結神經元網絡...")
            time.sleep(0.5)
            slow_type(f"警告：正在將資料串流至 Mikoshi...")
            time.sleep(1)
            slow_type(f"加密完成：'{user_input}' 已寫入 Relic 2.0。")
            st.success("存檔成功。夜之城不會忘記你。")
        else:
            st.error("偵測不到訊息輸入，請重新嘗試。")

with col2:
    # 這裡可以放個賽博感的 GIF 或是直接留白看背景
    st.info("Status: Waiting for Neural Link...")
