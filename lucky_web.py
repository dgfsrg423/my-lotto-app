import streamlit as st
import random

def pick_numbers():
    a1 = random.sample(range(1, 39), 6)
    a1.sort()
    a2 = random.randint(1, 8)
    return a1, a2

st.title("🎰 威力彩幸運選號器")
st.write("這是我的第一個 Python 網頁作品！")

count = st.slider("想要幾注？", 1, 10, 5)

if st.button("點我產生號碼"):
    for i in range(1, count + 1):
        a1, a2 = pick_numbers()
        st.success(f"第 {i} 注 - 第一區：{a1}，第二區：[{a2}]")