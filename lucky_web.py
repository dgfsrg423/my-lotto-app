import streamlit as st
import random

# 1. 網頁基本設定 (分頁標題與圖示)
st.set_page_config(page_title="威力彩神算手 💰", page_icon="💵", layout="centered")

# 2. 核心美化：注入 CSS 魔法
st.markdown("""
    <style>
    /* 設定背景圖片：使用錢堆背景 */
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1518458028434-518f2333d60d?q=80&w=2070");
        background-size: cover;
        background-attachment: fixed;
    }
    
    /* 讓主畫面區塊變透明黑，讓文字浮現出來 */
    .main {
        background-color: rgba(0, 0, 0, 0.75);
        padding: 40px;
        border-radius: 25px;
        color: white;
    }

    /* 美化按鈕：變大、變亮紅、滑鼠移上去會動 */
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

# 3. 網頁標題
st.title("💰 威力彩幸運選號器")
st.write("這不僅僅是程式，這是通往財富自由的門票（誤）！")

# 4. 側邊欄設定
with st.sidebar:
    st.header("⚙️ 選項設定")
    count = st.slider("想要購買幾注？", 1, 10, 5)
    st.divider()
    st.write("💡 提示：按鈕點下去會噴氣球喔！")

# 5. 選號邏輯與顯示
if st.button("🚀 啟動幸運召喚！"):
    st.balloons() # 噴發慶祝氣球
    
    for i in range(1, count + 1):
        # 第一區 1~38 取 6 個
        a1 = sorted(random.sample(range(1, 39), 6))
        # 第二區 1~8 取 1 個
        a2 = random.randint(1, 8)
        
        # 使用漂亮的小卡片顯示號碼
        with st.container():
            st.markdown(f"### 第 {i} 注")
            col1, col2 = st.columns([3, 1])
            col1.info(f"**第一區：** {a1}")
            col2.error(f"**第二區：** [{a2}]")
            st.write("---")

    st.success("選號完成！祝您順利中大獎！")
