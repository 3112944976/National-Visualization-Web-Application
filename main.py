#!/usr/bin/env python
# coding: utf-8
import pandas as pd
import streamlit as st
from PIL import Image
import tools
import tools_cygf as t2
# 设置网页名称
st.set_page_config(page_title='中国国情数据可视化网')
# ==========左边栏==========
with st.sidebar:
    st.subheader('欢迎访问,中国国情数据可视化网!')
    # 展示图片
    image = Image.open('./图片/头像.jpg')
    st.image(image, caption='Hi,My name is Pandas!',width=150,use_column_width=False)
    # 下拉栏1
    add_selectbox1 = st.selectbox("选择您想了解的主题：",("待选择","经济", "人口", "教育","关于我们"))
    # 下拉栏2
    add_selectbox2 = st.selectbox("创意工坊",("待选择","图表生成"))

if add_selectbox1 == "经济":
    tools.set_ec()
if add_selectbox1 == "人口":
    tools.set_po()
if add_selectbox1 == "教育":
    tools.set_ed()
if add_selectbox1 == "关于我们":
    tools.set_our()
    
if add_selectbox2 == "图表生成":
    t2.set_chart()
    





