import streamlit as st
import random

# 1. 網頁基本設定
st.set_page_config(page_title="威力彩神算手 💰", page_icon="💵", layout="centered")

# 2. 核心美化與音樂路徑
# 檔名必須與 GitHub 完全一致：圖片是 gb.jpg，音樂是 music.mp3
bg_url = "https://raw.githubusercontent.com/dgfsrg423/my-lotto-app/main/gb.jpg"
music_url = "https://raw.githubusercontent.com/dgfsrg423/my-lotto-app/main/music.mp3"

st.markdown(f"""
    <style>
    .stApp {{
        background: url("{bg_url}");
        background-size: cover;
        background-attachment: fixed;
    }}
    
    .main {{
        background-color: rgba(0, 0, 0, 0.75);
        padding: 40px;
        border-radius: 25px;
        color: white;
        backdrop-filter: blur(5px);
    }}

    [data-testid="stSidebar"] {{
        background-color: rgba(0, 0, 0, 0.85);
    }}

    .stButton>button {{
        width: 100%;
        border-radius: 50px;
        height: 3.5em;
        background: linear-gradient(45deg, #ff4b4b, #ff8a8a);
        color: white;
        font-weight: bold;
        border: none;
    }}
    </style>
""", unsafe_allow_html=True)

# 3. 側邊欄控制
with st.sidebar:
    st.header("⚙️ 設定中心")
    count = st.slider("想要購買幾注？", 1, 10, 5)
    st.write("---")
    
    # 這裡顯示播放器，方便你檢查檔案是否抓取成功
    st.write("🎵 背景音樂控制")
    st.audio(music_url, format="audio/mp3")
    st.info("💡 如果播放器顯示載入中或無法播放，可能是檔案太大或網址失效。")

# 4. 主畫面內容
st.title("💰 威力彩幸運選號器")
st.write("聽著音樂，祝您好運連連！")

if st.button("🚀 啟動幸運召喚！"):
    st.balloons()
    for i in range(1, count + 1):
        a1 = sorted(random.sample(range(1, 39), 6))
        a2 = random.randint(1, 8)
        with st.container():
            st.markdown(f"### 第 {i} 注")
            col1, col2 = st.columns([3, 1])
            col1.info(f"**第一區：** {a1}")
            col2.error(f"**第二區：** [{a2}]")
            st.write("---")
