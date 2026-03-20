import streamlit as st
import time
import base64

# --- 1. 頁面基礎設置 ---
st.set_page_config(page_title="ARASAKA-RELIQUE-TERMINAL", layout="wide")

# --- 2. 核心 CSS 注入 (含音樂播放器隱藏樣式) ---
def apply_cyber_theme(bin_file):
    try:
        with open(bin_file, 'rb') as f:
            data = f.read()
        bin_str = base64.b64encode(data).decode()
        
        st.markdown(
            f"""
            <style>
            @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Share+Tech+Mono&display=swap');

            /* 背景圖與濾鏡 */
            .stApp {{
                background-image: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)), url("data:image/jpg;base64,{bin_str}");
                background-size: cover;
                background-position: center;
                background-attachment: fixed;
                color: #00ff9f;
                font-family: 'Share+Tech+Mono', monospace;
            }}

            /* 隱藏主界面不必要的元件 */
            header, footer, [data-testid="stToolbar"] {{ visibility: hidden; }}

            /* 標題與文字樣式 */
            .glitch-title {{
                text-align: center;
                color: #fcee0a;
                text-shadow: 3px 3px #ff003c;
                font-family: 'Orbitron', sans-serif;
                font-size: 3rem;
                margin-top: 50px;
            }}

            /* 改造按鈕 */
            .stButton>button {{
                background: #fcee0a;
                color: #000;
                font-family: 'Orbitron', sans-serif;
                font-weight: bold;
                border: none;
                clip-path: polygon(15% 0, 100% 0, 100% 70%, 85% 100%, 0 100%, 0% 30%);
                width: 100%;
                transition: 0.3s;
            }}
            .stButton>button:hover {{
                background: #00f0ff;
                box-shadow: 0 0 20px #00f0ff;
            }}

            /* 強制讓音樂播放器保持運作但看起來不突兀 */
            [data-testid="stAudio"] {{
                position: fixed;
                bottom: 10px;
                right: 10px;
                width: 300px;
                opacity: 0.5; /* 半透明，避免擋住畫面 */
                z-index: 999;
                transition: 0.5s;
            }}
            [data-testid="stAudio"]:hover {{ opacity: 1.0; }}

            </style>
            """,
            unsafe_allow_html=True
        )
    except:
        st.error("背景載入失敗，請確認 gb.jpg.jpg 在根目錄。")

apply_cyber_theme('gb.jpg.jpg')

# --- 3. 功能函數 ---
def slow_type(text, speed=0.03):
    placeholder = st.empty()
    full_text = ""
    for char in text:
        full_text += char
        placeholder.markdown(f"#### `> {full_text}_`")
        time.sleep(speed)

# --- 4. 主介面 ---
st.markdown('<div class="glitch-title">[ RELIC BACKUP TERMINAL ]</div>', unsafe_allow_html=True)

col1, col2 = st.columns([2, 1])
with col1:
    user_input = st.text_input("輸入要備份到神經雲端的訊息:", placeholder="Wake up, Samurai...")
    if st.button("啟動遺言封裝 (INITIATE ARCHIVE)"):
        if user_input:
            slow_type("正在連結神經元網絡...")
            slow_type(f"加密完成：'{user_input}' 已寫入 Relic 2.0。")
            st.success("存檔成功。夜之城不會忘記你。")
        else:
            st.error("偵測不到訊息輸入。")

with col2:
    st.markdown("### [ SYSTEM STATUS ]")
    st.write("🟢 Neural Link: **Stable**")
    st.write("🟡 Audio Stream: **Active**")
    st.progress(24)

# --- 5. 音樂播放器 (移出側邊欄，置於頁面底部) ---
# 這樣就算側邊欄關閉，音樂也不會中斷
st.audio("music.mp3.mp3")
