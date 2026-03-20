import streamlit as st
import time
import base64

# --- 1. 初始化 ---
st.set_page_config(page_title="RELIC_OS", layout="wide", initial_sidebar_state="collapsed")

def get_base64(bin_file):
    try:
        with open(bin_file, 'rb') as f:
            return base64.b64encode(f.read()).decode()
    except:
        return ""

# --- 2. 簡約版賽博 UI 注入 ---
def inject_ui():
    bg_data = get_base64('bg_motion.gif')
    css = f'''
    <style>
    .stApp {{
        background: linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.7)), url("data:image/gif;base64,{bg_data}");
        background-size: cover;
        background-position: center;
        color: #00ff9f;
        font-family: monospace;
    }}
    .glitch-text {{
        font-size: 4rem;
        text-align: center;
        color: white;
        text-shadow: 2px 2px #ff003c;
        margin: 20px;
    }}
    header, footer {{ visibility: hidden; }}
    </style>
    '''
    st.markdown(css, unsafe_allow_html=True)

inject_ui()

# --- 3. 核心邏輯 ---
def slow_type(text, tag="INFO"):
    placeholder = st.empty()
    full_str = ""
    for char in text:
        full_str += char
        placeholder.write(f"**[{tag}]:** {full_str}_")
        time.sleep(0.03)

# --- 4. 介面佈局 ---
st.markdown('<div class="glitch-text">RELIC_OS</div>', unsafe_allow_html=True)

# 狀態儀錶板
col1, col2 = st.columns(2)
col1.metric("連線狀態", "已同步 (SYNCED)")
col2.metric("晶片完整度", "42%", "-1%")

st.divider()

# 主要功能區
left_col, right_col = st.columns([2, 1]) # 確保這裡的中括號有閉合

with left_col:
    st.write("### < 數據封裝模組 >")
    user_msg = st.text_input("輸入要寫入晶片的內容", placeholder="Wake up, Samurai...", label_visibility="collapsed")
    
    if st.button("執行靈魂寫入 (EXECUTE)"):
        if user_msg:
            slow_type("正在開啟神經連結...")
            time.sleep(0.5)
            slow_type(f"數據備份中：{user_msg}", tag="WARNING")
            time.sleep(0.8)
            slow_type("寫入完成。夜之城不會忘記你。", tag="SYSTEM")
            st.success("存檔成功 (ARCHIVE SUCCESS)")
        else:
            slow_type("錯誤：未偵測到輸入流。", tag="ERROR")

with right_col:
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJ4eG14eG14eG14eG14eG14eG14eG14eG14eG14eG14JnB2PTEmZXA9djFfaW50ZXJuYWxfZ2lmX2J5X2lkJmN0PWc/vVzH2XY3m0EJG/giphy.gif")

# 音樂播放
st.audio("main_theme.mp3")
