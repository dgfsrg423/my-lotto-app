import streamlit as st
import time
import base64

# --- 1. 頁面基礎設置 ---
st.set_page_config(page_title="ARASAKA-RELIQUE-TERMINAL", layout="wide")

# --- 2. 圖片轉碼函數 (解決路徑找不到的終極方案) ---
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_png_as_page_bg(bin_file):
    bin_str = get_base64_of_bin_file(bin_file)
    page_bg_img = f'''
    <style>
    .stApp {{
        background-image: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)), url("data:image/jpg;base64,{bin_str}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    
    /* 賽博掃描線 */
    .stApp::after {{
        content: " ";
        display: block;
        position: fixed;
        top: 0; left: 0; bottom: 0; right: 0;
        background: linear-gradient(rgba(18, 16, 16, 0) 50%, rgba(0, 0, 0, 0.1) 50%);
        background-size: 100% 4px;
        z-index: 100;
        pointer-events: none;
        opacity: 0.3;
    }}

    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Share+Tech+Mono&display=swap');
    
    .stApp {{
        color: #00ff9f;
        font-family: 'Share+Tech+Mono', monospace;
    }}

    .glitch-title {{
        text-align: center;
        color: #fcee0a;
        text-shadow: 3px 3px #ff003c;
        font-family: 'Orbitron', sans-serif;
        font-size: clamp(1.5rem, 5vw, 3rem);
        margin-bottom: 30px;
    }}

    .stButton>button {{
        background: #fcee0a;
        color: #000;
        font-family: 'Orbitron', sans-serif;
        font-weight: bold;
        border: none;
        clip-path: polygon(15% 0, 100% 0, 100% 70%, 85% 100%, 0 100%, 0% 30%);
        padding: 12px 30px;
        transition: 0.3s;
        width: 100%;
    }}
    .stButton>button:hover {{
        background: #00f0ff;
        box-shadow: 0 0 20px #00f0ff;
        color: #000;
    }}
    #MainMenu, footer, header {{visibility: hidden;}}
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)

# 嘗試加載背景 (對準你的檔案名稱)
try:
    set_png_as_page_bg('gb.jpg.jpg')
except:
    st.error("系統錯誤：找不到 gb.jpg.jpg 檔案。請確認檔案已上傳至 GitHub 根目錄。")

# --- 3. 打字機與主介面 ---
def slow_type(text, speed=0.03):
    placeholder = st.empty()
    full_text = ""
    for char in text:
        full_text += char
        placeholder.markdown(f"#### `> {full_text}_`")
        time.sleep(speed)

with st.sidebar:
    st.markdown("### 💿 NEURAL LINK")
    st.write("🎵 **OST:** *Been Good to Know Ya*")
    st.audio("music.mp3.mp3") 
    st.divider()
    st.markdown("##### [SYSTEM: CRITICAL]")
    st.progress(15)

st.markdown('<div class="glitch-title">[ RELIC BACKUP TERMINAL ]</div>', unsafe_allow_html=True)

col1, col2 = st.columns([2, 1])
with col1:
    user_input = st.text_input("輸入要備份到神經雲端的訊息:", placeholder="Wake up, Samurai...")
    if st.button("啟動遺言封裝 (INITIATE ARCHIVE)"):
        if user_input:
            slow_type("正在連結神經元網絡...")
            time.sleep(0.5)
            slow_type(f"加密完成：'{
