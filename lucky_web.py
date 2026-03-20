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
        # 這裡不使用 f-string，避免 CSS 大括號衝突
        style_code = """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Fira+Code:wght@300;500&family=Syncopate:wght@400;700&display=swap');

        .stApp {
            background: linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.7)), 
                        url("data:image/gif;base64,REPLACE_BG");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            font-family: 'Fira Code', monospace;
            color: #00ff9f;
        }

        @keyframes glitch {
            0% { transform: translate(0); text-shadow: -2px 0 #ff003c, 2px 0 #00f0ff; }
            20% { transform: translate(-3px, 3px); opacity: 0.8; }
            40% { transform: translate(-3px, -3px); text-shadow: 2px 0 #ff003c, -2px 0 #00f0ff; }
            60% { transform: translate(3px, 3px); }
            80% { transform: translate(3px, -3px); opacity: 0.9; }
            100% { transform: translate(0); }
        }

        .glitch-header {
            font-family: 'Syncopate', sans-serif;
            font-size: 4rem;
            text-align: center;
            color: white;
            letter-spacing: 15px;
            animation: glitch 1.5s infinite linear alternate-reverse;
            padding-top: 5vh;
        }

        .stTextInput>div>div>input {
            background: rgba(0, 30, 30, 0.7) !important;
            border: 1px solid #00ff9f !important;
            color: #ff003c !important;
            font-size: 1.2rem;
            border-radius: 0;
            padding: 10px;
        }

        .stButton>button {
            background: transparent;
            color: #00ff9f;
            border: 2px solid #00ff9f;
            padding: 20px;
            font-weight: bold;
            text-transform: uppercase;
            letter-spacing: 5px;
            clip-path: polygon(10% 0, 100% 0, 100% 70%, 90% 100%, 0 100%, 0% 30%);
            transition: 0.4s;
            width: 100%;
        }
        .stButton>button:hover {
            background: #00ff9f;
            color: black;
            box-shadow: 0 0 30px #00ff9f;
        }

        header, footer, [data-testid="stToolbar"] { visibility: hidden; }
        
        [data-testid="stAudio"] {
            position: fixed;
            bottom: 20px;
            right: 20px;
            width: 300px;
            opacity: 0.2;
            filter: invert(1) hue-rotate(90deg);
            z-index: 9999;
        }
        [data-testid="stAudio"]:hover { opacity: 1.0; }
        </style>
        """.replace("REPLACE_BG", bg_base64)
        
        st.markdown(style_code, unsafe_allow_html=True)
    except Exception as e:
        st.error(f"SYSTEM_FAILURE: {e}")

inject_god_mode_ui('bg_motion.gif')

# --- 3. [SYSTEM LOGIC: NEURAL SYNC] ---
def terminal_print(text, msg_type="info"):
    colors = {"info": "#00ff9f", "error": "#ff003
