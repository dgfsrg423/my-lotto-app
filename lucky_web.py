import streamlit as st
import random

# 1. 網頁基本設定
st.set_page_config(page_title="威力彩神算手 💰", page_icon="💵", layout="centered")

# 2. 核心美化：注入 CSS 魔法
# 修正：檔名改為你 GitHub 上的 gb.jpg
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

    <audio id="bgm" loop>
        <source src="{music_url}" type="audio/mp3">
    </audio>
    
    <script>
    // 監聽第一次點擊來啟動音樂
    var playBgm = function() {{
        var audio = document.getElementById('bgm');
        audio.play();
        document.removeEventListener('click', playBgm);
    }};
    document.addEventListener('click', playBgm);
    </script>
""", unsafe_allow_html=True)

# 3. 側邊欄
with st.sidebar:
    st.header("⚙️ 設定中心")
    count = st.slider("想要購買幾注？", 1, 10, 5)
    st.write("---")
    st.info("🎵 進入網頁後，請【點擊畫面任何地方】即可啟動背景音樂！")

# 4. 主畫面內容
st.title("💰 威力彩幸運選號器")
st.write("背景與音樂已同步，祝您好運連連！")

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

