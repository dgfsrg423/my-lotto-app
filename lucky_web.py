import streamlit as st
import random

# 1. 網頁基本設定
st.set_page_config(page_title="威力彩神算手 💰", page_icon="💵", layout="centered")

# 2. 核心美化：注入 CSS 魔法
# 這裡同時處理了背景圖與介面的透明質感
st.markdown("""
    <style>
    /* 背景圖片設定 */
    .stApp {
        background: url("https://raw.githubusercontent.com/dgfsrg423/my-lotto-app/main/bg.jpg");
        background-size: cover;
        background-attachment: fixed;
    }
    
    /* 主畫面磨砂玻璃效果 */
    .main {
        background-color: rgba(0, 0, 0, 0.7);
        padding: 40px;
        border-radius: 25px;
        color: white;
        backdrop-filter: blur(5px); /* 增加一點模糊美感 */
    }

    /* 側邊欄深色透明處理 */
    [data-testid="stSidebar"] {
        background-color: rgba(0, 0, 0, 0.85);
    }

    /* 美化按鈕 */
    .stButton>button {
        width: 100%;
        border-radius: 50px;
        height: 3.5em;
        background: linear-gradient(45deg, #ff4b4b, #ff8a8a);
        color: white;
        font-weight: bold;
        border: none;
        transition: 0.3s;
    }
    .stButton>button:hover {
        transform: scale(1.02);
        box-shadow: 0px 5px 15px rgba(255, 75, 75, 0.4);
    }
    </style>
""", unsafe_allow_html=True)

# 3. 側邊欄設定 (選項 + 音樂播放器)
with st.sidebar:
    st.header("⚙️ 設定與音樂")
    count = st.slider("想要購買幾注？", 1, 10, 5)
    
    st.write("---")
    st.write("🎵 背景音樂控制")
    # 音樂路徑指向你的 GitHub 檔案
    music_url = "https://raw.githubusercontent.com/dgfsrg423/my-lotto-app/main/music.mp3"
    st.audio(music_url, format="audio/mp3")
    st.caption("點擊上方播放按鈕開啟氛圍模式")

# 4. 主網頁內容
st.title("💰 威力彩幸運選號器")
st.write("在雨中尋找財富的靈感...")

if st.button("🚀 啟動幸運召喚！"):
    st.balloons()
    
    for i in range(1, count + 1):
        # 第一區 1~38 取 6 個
        a1 = sorted(random.sample(range(1, 39), 6))
        # 第二區 1~8 取 1 個
        a2 = random.randint(1, 8)
        
        with st.container():
            st.markdown(f"### 第 {i} 注")
            col1, col2 = st.columns([3, 1])
            col1.info(f"**第一區：** {a1}")
            col2.error(f"**第二區：** [{a2}]")
            st.write("---")

    st.success("選號完成！祝您順利中大獎！")
