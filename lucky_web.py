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
    try:
        bg_base64 = get_base64(bg_file)
        st.markdown(f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Fira+Code:wght@300;500&family=Syncopate:wght@400;700&display=swap');

        /* 全域背景：動態背景 + 深色遮罩 */
        .stApp {{
            background: linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.7)), 
                        url("data:image/gif;base64,{bg_base64}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            font-family: 'Fira Code', monospace;
            color: #00ff9f;
        }}

        /* 標題故障藝術 (Glitch Animation) */
        @keyframes glitch {{
            0% {{ transform: translate(0); text-shadow: -2px 0 #ff003c, 2px 0 #00f0ff; }}
            20% {{ transform: translate(-3px, 3px); opacity: 0.8; }}
            40% {{ transform: translate(-3px, -3px); text-shadow: 2px 0 #ff003c, -2px 0 #00f0ff; }}
            60% {{ transform: translate(3px, 3px); }}
            80% {{ transform: translate(3px, -3px); opacity: 0.9; }}
            100% {{ transform: translate(0); }}
        }}

        .glitch-header {{
            font-family: 'Syncopate', sans-serif;
            font-size: clamp(2rem, 8vw, 4rem);
            text-align: center;
            color: white;
            letter-spacing: 15px;
            animation: glitch 1.5s infinite linear alternate-reverse;
            padding-top: 5vh;
        }}

        /* 輸入框美化 */
        .stTextInput>div>div>input {{
            background: rgba(0, 30, 30, 0.7) !important;
            border: 1px solid #00ff9f !important;
            color: #ff003c !important;
            font-size: 1.2rem;
            border-radius: 0;
            padding: 10px;
        }}

        /* 賽
