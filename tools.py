#!/usr/bin/env python
# coding: utf-8
import pandas as pd
import streamlit as st
from PIL import Image
from streamlit_echarts import st_pyecharts

import population as po
import economics as ec
import education as ed

def set_our():
    st.balloons()
    # 设置网页标题
    st.markdown('# 关于我们')
    # 打开音频
    our_music1 = open('./music/背景音乐-成为事实.mp3', 'rb')
    our_audio_bytes = our_music1.read()
    st.markdown('背景音乐：`Divenire(演变).mp3`')
    st.audio(our_audio_bytes, format='audio/mp3')
    our_1, our_2 = st.beta_columns([1, 3])
    with our_1:
        our_image = Image.open('./图片/our_1.jpg')
        st.image(our_image, caption='',use_column_width=True)
    with our_2:
        st.markdown('''####
            大家好，我是Pandas！我们生活在数据时代，
            每一个行为都在产生着记录或者未被记录的数据。
            这些数据的背后，都刻画着许多基于行为的真相。
            所以我们通过收集、组织、处理、挖掘分析及输出设计等步骤，
            来最终直观的呈现出它们背后的意味。
            而这也是我们建设这个可视化网站的意义所在！
                    ''')
        st.markdown('青春寄语：`矢志不渝，沉静致远!`')
    
    with st.beta_expander("查看源数据"):
        pw = st.text_input('请输入权限密码：')
        if pw != 'hello':
            st.warning('Please enter the correct password！')
            st.stop()
        else:
            st.write("欢迎，您的访问！")
            st.write("数据来源：[国家统计局官网](http://www.stats.gov.cn/)")
            our_options = ('不看了','对，我想看爬虫代码','不，我想直接看源数据')
            our_radio = st.radio("您想了解获取数据的爬虫代码吗？", our_options)
            if our_radio == '对，我想看爬虫代码':
                st.markdown("我有，但我就是不给，就是`玩`！！！")
            if our_radio == '不，我想直接看源数据':
                our_selection = st.selectbox('请先选择主题：',options=("经济", "人口", "教育","null"))
                if our_selection == "人口":
                    obj1 = pd.read_csv('./源数据/国家统计局年度数据/人口/人口出生率、死亡率和自然增长率.csv')
                    obj2 = pd.read_csv("./源数据/国家统计局年度数据/人口/人口年龄结构和抚养比.csv")
                    obj3 = pd.read_csv("./源数据/国家统计局年度数据/人口/总人口.csv")
                    obj4 = pd.read_csv("./源数据/国家统计局分省年度数据/人口/人口抽样调查样本数据/按婚姻状况分人口数(人口抽样调查).csv")
                    our_po_tmp = ('人口出生率、死亡率和自然增长率.csv'
                                  ,'人口年龄结构和抚养比.csv'
                                  ,'总人口.csv'
                                  ,'按婚姻状况分人口数(人口抽样调查).csv','')
                    our_selection_po = st.multiselect('选择指定的表：',our_po_tmp,default='')
                    if '人口出生率、死亡率和自然增长率.csv' in our_selection_po:
                        st.markdown('`人口出生率、死亡率和自然增长率.csv`')
                        st.dataframe(obj1)
                    if '人口年龄结构和抚养比.csv' in our_selection_po:
                        st.markdown('`人口年龄结构和抚养比.csv`')
                        st.dataframe(obj2)
                    if '总人口.csv' in our_selection_po:
                        st.markdown('`总人口.csv`')
                        st.dataframe(obj3)
                    if '按婚姻状况分人口数(人口抽样调查).csv' in our_selection_po:
                        st.markdown('`按婚姻状况分人口数(人口抽样调查).csv`')
                        st.dataframe(obj4)
                
def set_ed():
    # 设置网页标题
    st.header('教育')
    # 设置网页子标题
    st.subheader('数据来源：国家统计局官网')
    # 子主题导航栏
    ed_options = st.selectbox('导航栏',['可视化组件展示','test'])
    # 主题下拉栏
    if ed_options == '可视化组件展示':
        ed_tmp = ('高等教育','高中','初中','小学','教育经费')
        ed_selectbox = st.multiselect('选择您想看到的素材：',ed_tmp,default='教育经费')
    
    if ed_options == '可视化组件展示':
        if '教育经费' in ed_selectbox:
            st.subheader('分省教育经费排名')
            video_file1 = open('./video/教育经费.mp4', 'rb')
            video_bytes1 = video_file1.read()
            st.video(video_bytes1)
        if '高等教育' in ed_selectbox:
            '''- '''
            st_pyecharts(ed.ed1(),width="864px",height="520px")
            '''- '''
            st_pyecharts(ed.ed2(),width="864px",height="520px")
            '''- '''
            st_pyecharts(ed.ed3(),width="864px",height="520px")
            '''- '''
            st_pyecharts(ed.ed11(),width="864px",height="520px")
        if '高中' in ed_selectbox:
            '''- '''
            #地图不显示，脚本导入失败
            #st_pyecharts(ed.ed4(),width="864px",height="520px")
            '''- '''
            st_pyecharts(ed.ed5(),width="864px",height="520px")
            '''- '''
            st_pyecharts(ed.ed6(),width="864px",height="520px")
        if '初中' in ed_selectbox:
            '''- '''
            #地图不显示，脚本导入失败
            #st_pyecharts(ed.ed7(),width="864px",height="520px")
            '''- '''
            st_pyecharts(ed.ed8(),width="864px",height="520px")
        if '小学' in ed_selectbox:
            '''- '''
            #地图不显示，脚本导入失败
            #st_pyecharts(ed.ed9(),width="864px",height="520px")
            '''- '''
            st_pyecharts(ed.ed10(),width="864px",height="520px")
    else:
        '''### Please waiting,We don't finish that work!  '''
        
def set_ec():
    # 设置网页标题
    st.header('经济')
    # 设置网页子标题
    st.subheader('数据来源：国家统计局官网')
    # 子主题导航栏
    ec_options = st.selectbox('导航栏',['可视化组件展示','test'])
    # 主题下拉栏
    if ec_options == '可视化组件展示':
        ec_tmp = ('GNI/GDP','居民消费水平','三大产业','NULL')
        ec_selectbox = st.multiselect('选择您想看到的素材：',ec_tmp,default='NULL')
    
    if ec_options == '可视化组件展示':
        if 'GNI/GDP' in ec_selectbox:
            '''- '''
            st_pyecharts(ec.ec1(),width="864px",height="520px")
            '''- '''
            #地图不显示，脚本导入失败
            #st_pyecharts(ec.ec2(),width="864px",height="520px")
            '''- '''
            st_pyecharts(ec.ec3(),width="864px",height="520px")
        if '居民消费水平' in ec_selectbox:
            st.subheader('中国居民消费水平')
            video_file1 = open('./video/中国居民消费水平.mp4', 'rb')
            video_bytes1 = video_file1.read()
            st.video(video_bytes1)
            '''- '''
            st_pyecharts(ec.ec4(),width="864px",height="520px")
        if '三大产业' in ec_selectbox:
            '''- '''
            st_pyecharts(ec.ec5(),width="864px",height="520px")
            '''- '''
            st_pyecharts(ec.ec6(),width="864px",height="520px")
            '''- '''
            st_pyecharts(ec.ec7(),width="864px",height="520px")
    else:
        '''### Please waiting,We don't finish that work!  '''
            
def set_po():
    # 设置网页标题
    st.header('人口')
    # 设置网页子标题
    st.subheader('数据来源：国家统计局官网')
    # 子主题导航栏
    po_options = st.selectbox('导航栏',['可视化组件展示','test'])
    # 下拉栏
    if po_options == '可视化组件展示':
        po_tmp = ('人口出生/死亡及自然增长率','人口年龄结构','人口性别结构','分地区/性别未婚人数抽样','年末常住人口')
        po_selectbox = st.multiselect('选择您想看到的素材：',po_tmp,default='年末常住人口')
    # 素材_可视化组件展示
    if po_options == '可视化组件展示':
        if '年末常住人口' in po_selectbox:
            st.subheader('年末常住人口')
            video_file1 = open('./video/年末常住人口.mp4', 'rb')
            video_bytes1 = video_file1.read()
            st.video(video_bytes1)
        if '人口出生/死亡及自然增长率' in po_selectbox:
            st.subheader('人口自然增长率')
            video_file2 = open('./video/人口自然增长率.mp4', 'rb')
            video_bytes2 = video_file2.read()
            st.video(video_bytes2)
            
            '''- 2000--2019年间，人口增长率从7.58%降到3.34%，同比下降了44.00%'''
            st_pyecharts(po.po1(),width="864px",height="520px")
        if '人口年龄结构' in po_selectbox:
            '''- 人口年龄结构的总体趋势是中、高龄人口占比逐渐升高，低龄人口占比在下降。'''
            st_pyecharts(po.po2(),width="864px",height="520px")
        if '人口性别结构' in po_selectbox:
            '''- 人口性别结构'''
            st_pyecharts(po.po3(),width="864px",height="520px")
        if '分地区/性别未婚人数抽样' in po_selectbox:
            '''- 总体而言，男性未婚人数在大多数省份里都比女性未婚人数多。'''
            st_pyecharts(po.po4(),width="864px",height="520px")
    else:
        '''### Please waiting,We don't finish that work!  '''

