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
        # 使用 replace 繞過 f-string 的大括號陷阱
        style_code = """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Fira+Code:wght@300;500&family=Syncopate:wght@400;700&display=swap');

        .stApp {
            background: linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.7)), 
                        url("data:image/gif;base64,DATA_PLACEHOLDER");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            font-family: 'Fira Code', monospace;
            color: #00ff9f;
        }

        @keyframes glitch {
            0% { transform: translate(0); text-shadow: -2px 0 #ff003c, 2px 0 #00f0ff; }
            40% { transform: translate(-3px, -3px); text-shadow: 2px 0 #ff003c, -2px 0 #00f0ff; }
            100% { transform: translate(0); }
        }

        .glitch-header {
            font-family: 'Syncopate', sans-serif;
            font-size: 3.5rem;
            text-align: center;
            color: white;
            letter-spacing: 12px;
            animation: glitch 2s infinite linear;
            padding-top: 5vh;
        }

        .stTextInput>div>div>input {
            background: rgba(0, 30, 30, 0.8) !important;
            border: 1px solid #00ff9f !important;
            color: #ff003c !important;
            border-radius: 0;
        }

        .stButton>button {
            background: transparent;
            color: #00ff9f;
            border: 2px solid #00ff9f;
            clip-path: polygon(10% 0, 100% 0, 100% 70%, 90% 100%, 0 100%, 0% 30%);
            width: 100%;
            height: 3rem;
