import streamlit as st
import random

# 1. 網頁基本設定
st.set_page_config(page_title="威力彩神算手 💰", page_icon="💵", layout="centered")

# 2. 檔案路徑設定 (嚴格對齊你截圖中的檔名)
# 圖片是 gb.jpg，音樂目前是 music.mp3.mp3
bg_url = "https://raw.githubusercontent.com/dgfsrg423/my-lotto-app/main/gb.jpg"
music_url = "https://raw.githubusercontent.com/dgfsrg423/my-lotto-app/main/music.mp3.mp3"

# 3. 視覺美化與自動播放腳本
st.markdown(f"""
    <style>
    /* 背景圖與毛玻璃效果 */
    .stApp {{
        background: url("{bg_url}");
        background-size: cover;
        background-attachment: fixed;
    }}
    
    .main {{
        background-color: rgba(0, 0, 0, 0.7);
        padding: 40px;
        border-radius: 25px;
        color: white;
        backdrop-filter: blur(8px);
    }}

    /* 側邊欄風格 */
    [data-testid="stSidebar"] {{
        background-color: rgba(0, 0, 0, 0.85);
    }}

    /* 按鈕美化 */
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

    <audio id="bgm" loop>
        <source src="{music_url}" type="audio/mp3">
    </audio>
    
    <script>
    var playBgm = function() {{
        var audio = document.getElementById('bgm');
        audio.play();
        document.removeEventListener('click', playBgm);
    }};
    document.addEventListener('click', playBgm);
    </script>
""", unsafe_allow_html=True)

# 4. 側邊欄控制
with st.sidebar:
    st.header("⚙️ 設定與音樂")
    count = st.slider("想要購買幾注？", 1, 10, 5)
    st.write("---")
    st.write("🎵 **背景音樂控制**")
    st.audio(music_url, format="audio/mp3")
    st.info("💡 提示：若沒聲音，點擊畫面任何地方或手動按播放。")

# 5. 主網頁內容
st.title("💰 威力彩幸運選號器")
st.write("檔名已全面對齊，準備迎接頭獎吧！")

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
    st.success("選號完成！")
