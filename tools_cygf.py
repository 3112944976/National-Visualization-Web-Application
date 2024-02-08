#!/usr/bin/env python
# coding: utf-8
import pandas as pd
import streamlit as st
from PIL import Image
from streamlit_echarts import st_pyecharts
from pyecharts.charts import Bar
from pyecharts import options as opts 

import population as po
import economics as ec
import education as ed
import pyecharts_set as pye_set

def set_chart():
    st.balloons()
    # 设置网页标题
    st.header('创意工坊 | 图表生成')
    st.markdown('1、`上传表格文件：`')
    # 文件类型选择
    file_info = st.selectbox("文件类型选择", options=['csv','xls'])
    # 1、单文件载入
    t2_uploaded_file = st.file_uploader("选择上传文件")
    if t2_uploaded_file is not None:
        if file_info == 'csv':
            st.write(t2_uploaded_file)
            t2_dataframe = pd.read_csv(t2_uploaded_file)
            st.write(t2_dataframe)
        if file_info == 'xls':
            st.write(t2_uploaded_file)
            t2_dataframe = pd.read_excel(t2_uploaded_file)
            st.write(t2_dataframe)
        
        # 2、数据集选择
        st.markdown('2、`数据集选择：`')
        # 初始化
        x = t2_dataframe.columns.tolist()
        y = []
        for i in range(0,len(t2_dataframe.index)):
            y.append(t2_dataframe.iloc[i].tolist())
        chart_data1 = pd.DataFrame(y,columns=x)
        # 索引选择
        file_info = st.selectbox("索引选择", options=chart_data1.columns.tolist())
        chart_data2 = chart_data1.set_index(file_info)
        # 选择数据列
        chart_x1 = st.multiselect('选择数据列：',chart_data2.columns.tolist())
        chart_data3 = pd.DataFrame(chart_data2,columns=chart_x1)
        st.write(chart_data3)
#         st.write(chart_data3.index.tolist())
#         st.write(chart_data3[chart_data3.columns.tolist()[0]].tolist())

        
        # 3、图表样式选项卡
        st.markdown('3、`图表样式选项卡：`')
        t2_options = st.multiselect('',['直线图','单Y柱状图','面积图'])
        if '直线图' in t2_options:
            st.write('`直线图`')
            st.line_chart(chart_data3)
            
        if '单Y柱状图' in t2_options:
            st.write('`单Y柱状图`')
            st.bar_chart(chart_data3)
            st_pyecharts(pye_set.Bar_with_brush(chart_data3))
        if '面积图' in t2_options:
            st.write('`面积图`')
            st.area_chart(chart_data3)
#         if '饼状图' in t2_options:
#             st.write('`饼状图`')