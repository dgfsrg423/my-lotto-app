import streamlit as st
import time
import base64

# --- 系統初始化 ---
st.set_page_config(page_title="RELIC_OS", layout="wide", initial_sidebar_state="collapsed")

def get_base64(bin_file):
    try:
        with open(bin_file, 'rb') as f:
            return base64.b64encode(f.read()).decode()
    except:
        return ""

# --- 注入 CSS 樣式 ---
def inject_ui():
    bg_data = get_base64('bg_motion.gif')
    
    # 使用最基礎的字串拼接，確保編譯器不會誤讀
    css = '<style>'
    css += 'font-family: "Fira Code", monospace;'
    css += '.stApp {'
    css += f'background: linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.7)), url("data:image/gif;base64,{bg_data}");'
    css += 'background-size: cover; background-position: center; color: #00ff9f; }'
    css += '.glitch { font-size: 3rem; text-align: center; color: white; letter-spacing: 10px; padding: 20px; }'
    css += '.stTextInput>div>div>input { background: #001a1a !important; color: #ff003c !important; }'
    css += '.stButton>button { background: transparent; color: #00ff9f; border: 1px solid #00ff9f; width: 100%; }'
    css += 'header, footer { visibility: hidden; }'
    css += '</style>'
    
    st.markdown(css, unsafe_allow_html=True)

inject_ui()

# --- 終端機打字效果 ---
def terminal_print(text, type="info"):
    colors = {"info": "#00ff9f", "error": "#ff003c", "warn": "#fcee0a"}
    placeholder = st.empty()
    display_text = ""
    for char in text:
        display_text += char
        placeholder.markdown(f'<p style="color:{colors[type]};"><b>[SYS_LOG]:</b> {display_text}_</p>', unsafe_allow_html=True)
        time.sleep(0.02)

# --- 主介面佈局 ---
st.markdown('<div class="glitch">RELIC_OS</div>', unsafe_allow_html=True)

st.write("---")
col1, col2, col3 = st.columns(3)
col1.metric("連結狀態", "SYNCED")
col2.metric("完整度", "42%", "-1%")
col3.metric("區域", "Night City")
st.write("---")

left, right = st.columns([2,
