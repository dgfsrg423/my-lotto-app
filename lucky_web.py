import streamlit as st
import random

# 設定網頁標題與圖示
st.set_page_config(page_title="威力彩神算手", page_icon="💰")

# 加入一些 CSS 讓按鈕變大變漂亮
st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        height: 3em;
        background-color: #ff4b4b;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

st.title("💰 威力彩幸運選號器")
st.info("祝您中大獎！記得存檔後推送到 GitHub 才會更新喔！")

# 側邊欄設定
with st.sidebar:
    st.header("設定選項")
    count = st.number_input("購買注數", min_value=1, max_value=20, value=5)
    show_lucky = st.checkbox("顯示今日運勢")

if st.button("🚀 立即產生幸運號碼"):
    if show_lucky:
        st.write(f"🔮 今日幸運方位：{random.choice(['東方', '南方', '西方', '北方'])}")
    
    for i in range(1, count + 1):
        a1 = sorted(random.sample(range(1, 39), 6))
        a2 = random.randint(1, 8)
        
        with st.expander(f"第 {i} 注號碼"):
            col1, col2 = st.columns([3, 1])
            col1.write(f"**第一區：** `{a1}`")
            col2.error(f"**第二區：** `{a2}`")

st.balloons() # 成功後的慶祝氣球！
