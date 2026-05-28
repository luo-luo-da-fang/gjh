import streamlit as st

# 设置页面标题
st.set_page_config(page_title="数字人民币分析报告", layout="wide")

# 读取你的HTML文件并嵌入
with open("digital_concusmy.html", "r", encoding="utf-8") as f:
    html_code = f.read()

# 嵌入HTML内容
st.components.v1.html(html_code, height=1000, scrolling=True)