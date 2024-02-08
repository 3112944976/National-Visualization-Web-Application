#!/usr/bin/env python
# coding: utf-8
import json
import pandas as pd
import numpy as np
from pyecharts import options as opts 
from pyecharts.charts import Map,Bar,Line,Page,Pie,Timeline,Gauge,Bar3D,Tab,Grid,PictorialBar
from pyecharts.globals import ChartType, SymbolType,ThemeType
from pyecharts.commons.utils import JsCode

def ec1():
    tmp = './源数据/国家统计局年度数据/国民经济核算/国内生产总值.csv'
    obj1 = pd.read_csv(tmp)
    x = np.array(obj1['年份'])
    y1 = np.array(obj1['国民总收入'])
    y2 = np.array(obj1['国内生产总值'])
    y3 = np.array(obj1['人均国内生产总值'])
    x = [str(i)+'年' for i in x[::-1]]
    def set_y(x):
        tmp = [round(i) for i in x[::-1]]
        return tmp

    bar = (
        Bar(init_opts=opts.InitOpts(width="1280px", 
                                    height="610px", 
                                    #bg_color="dimgray", 
                                    theme=ThemeType.VINTAGE,
                                    animation_opts=opts.AnimationOpts(animation_delay=1000, animation_easing="elasticOut")
                                   )
           )

        .add_xaxis(xaxis_data=x)
        .add_yaxis(series_name="国民总收入",y_axis=set_y(y1),yaxis_index=0)#color=colors[1]
        .add_yaxis(series_name="国内生产总值", y_axis=set_y(y2), yaxis_index=1)#, color=colors[0]
        .add_yaxis(series_name="人均国内生产总值", y_axis=set_y(y3), yaxis_index=2)#, color=colors[0]

        .extend_axis(
            yaxis=opts.AxisOpts(
                name="",
                type_="value",
                min_=7000,
                max_=1000000,
                position="right",
                axisline_opts=opts.AxisLineOpts(linestyle_opts=opts.LineStyleOpts(color="#F75000")),
                axislabel_opts=opts.LabelOpts(formatter="{value}"),
            )
        )
        .extend_axis(
            yaxis=opts.AxisOpts(
                type_="value",
                name="",
                min_=7000,
                max_=1000000,
                position="center",
                axisline_opts=opts.AxisLineOpts(linestyle_opts=opts.LineStyleOpts(color="#F75000")),
                axislabel_opts=opts.LabelOpts(formatter="{value}"),
                splitline_opts=opts.SplitLineOpts(is_show=True, linestyle_opts=opts.LineStyleOpts(opacity=1)),
            )
        )
        .extend_axis(
            yaxis=opts.AxisOpts(
                type_="value",
                name="",
                min_=7000,
                max_=1000000,
                position="left",
                axisline_opts=opts.AxisLineOpts(linestyle_opts=opts.LineStyleOpts(color="#F75000")),
                axislabel_opts=opts.LabelOpts(formatter="{value}"),
                splitline_opts=opts.SplitLineOpts(is_show=True, linestyle_opts=opts.LineStyleOpts(opacity=2)),
            )
        )
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False),itemstyle_opts={"normal": {"barBorderRadius": [30, 30, 30, 30],}})
        .set_global_opts(
            title_opts=opts.TitleOpts(title="GNI And GDP Visualization"),#, subtitle="我是副标题"
            datazoom_opts=[opts.DataZoomOpts(), opts.DataZoomOpts(type_="inside")],
            toolbox_opts=opts.ToolboxOpts(is_show=True),
            xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=False),
            yaxis_opts=opts.AxisOpts(
                type_="value",
                name="",
                min_=7000,
                max_=1000000,
                position="right",
                #offset=80,
                axisline_opts=opts.AxisLineOpts(linestyle_opts=opts.LineStyleOpts(color="#0066CC")),
                axislabel_opts=opts.LabelOpts(formatter="{value}"),
            ),
            tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
        )
    )
    return bar

def ec2():
    tmp = './源数据/国家统计局分省年度数据/国民经济核算/地区生产总值指数.csv'
    obj1 = pd.read_csv(tmp)
    obj2 = obj1[obj1['年份'].isin([2019])]
    x = [i[:2] for i in obj2['省份']]
    x[x.index('内蒙')] = '内蒙古'
    x[x.index('黑龙')] = '黑龙江'

    y = [round((i-87)*10) for i in obj1['地区生产总值指数(上年=100)']]
    y_2 = []
    for i in range(0,31):
        y_2.append(list(y[0:20]))
        y = y[20:]
    y_3 = np.array(y_2).T.tolist()

    tl = Timeline()
    count = 0
    for i in range(2019,1999,-1):
        map0 = (
            Map(init_opts=opts.InitOpts())
            .add("China", [list(z) for z in zip(x, y_3[count])], "china")
            .set_global_opts(
                title_opts=opts.TitleOpts(title="Visualization of regional GDP in {}".format(i)),
                visualmap_opts=opts.VisualMapOpts(min_=160, max_=280, is_piecewise=True, )
            )
        )
        count += 1
        tl.add(map0, "{}年".format(i))
        tl.add_schema(is_auto_play=True,is_rewind_play=True)
    return tl

def ec3():
    obj1 = pd.read_csv('./源数据/国家统计局年度数据/国民经济核算/支出法国内生产总值.csv')
    obj2 = obj1.set_index(obj1['年份'])
    obj3 = pd.DataFrame(obj2,columns=obj2.columns[1:7])

    data = []
    for i in obj3.index:
        for j in obj3.columns:
            data.append((i,j,round(obj3[j][i]/1000,1)))

    c = (
        Bar3D(init_opts=opts.InitOpts(width="1280px", height="610px"))
        .add(
            "项目分年GDP指数",
            data,
            xaxis3d_opts=opts.Axis3DOpts(obj3.index, type_="category"),
            yaxis3d_opts=opts.Axis3DOpts(obj3.columns, type_="category"),
            zaxis3d_opts=opts.Axis3DOpts(type_="value"),
        )
        .set_global_opts(visualmap_opts=opts.VisualMapOpts(max_=1000),title_opts=opts.TitleOpts(title="支出计量法GDP指数可视化"))
    )
    return c

def ec4():
    symbols = {
    "消费":"path://M633.250909 302.545455H390.749091A46.545455 46.545455 0 0 0 349.090909 328.145455C302.545455 423.796364 186.181818 571.112727 186.181818 674.909091c0 179.898182 145.92 279.272727 325.818182 279.272727s325.818182-99.374545 325.818182-279.272727c0-103.796364-116.363636-251.112727-162.909091-346.763636a46.545455 46.545455 0 0 0-41.658182-25.6z m-3.258182 302.545454h-73.076363a21.643636 21.643636 0 0 0-21.643637 21.643636v26.53091a21.643636 21.643636 0 0 0 21.643637 21.643636h73.076363a21.643636 21.643636 0 0 1 21.643637 21.643636v3.258182a21.643636 21.643636 0 0 1-21.643637 21.643636h-73.076363a21.643636 21.643636 0 0 0-21.643637 21.643637v49.803636a21.643636 21.643636 0 0 1-21.643636 21.643637h-3.258182a21.643636 21.643636 0 0 1-21.643636-21.643637v-49.803636a21.643636 21.643636 0 0 0-21.643637-21.643637h-73.076363a21.643636 21.643636 0 0 1-21.643637-21.643636v-3.258182a21.643636 21.643636 0 0 1 21.643637-21.643636h73.076363a21.643636 21.643636 0 0 0 21.643637-21.643636v-26.53091a21.643636 21.643636 0 0 0-21.643637-21.643636h-73.076363a21.643636 21.643636 0 0 1-21.643637-21.643636v-3.258182a21.643636 21.643636 0 0 1 21.643637-21.643636h16.290909a21.643636 21.643636 0 0 0 20.014545-29.556364l-23.272727-57.250909a21.643636 21.643636 0 0 1 20.48-29.556364 21.410909 21.410909 0 0 1 20.014545 13.498182l35.84 89.367273a21.410909 21.410909 0 0 0 20.014546 13.498182h17.221818a21.410909 21.410909 0 0 0 20.014546-13.498182l35.84-89.367273a21.410909 21.410909 0 0 1 20.014545-13.498182 21.643636 21.643636 0 0 1 20.014545 29.556364l-23.272727 57.250909a21.643636 21.643636 0 0 0 20.48 29.556364h16.290909a21.643636 21.643636 0 0 1 21.643637 21.643636v3.258182a21.643636 21.643636 0 0 1-21.643637 21.643636zM299.985455 178.269091A46.545455 46.545455 0 0 1 279.272727 139.636364a46.545455 46.545455 0 0 1 91.694546-10.938182l43.752727-43.752727a46.545455 46.545455 0 0 1 65.861818 0L512 116.363636l31.418182-31.418181a46.545455 46.545455 0 0 1 65.861818 0l43.752727 43.752727A46.545455 46.545455 0 0 1 744.727273 139.636364a46.545455 46.545455 0 0 1-20.712728 38.632727l-40.261818 57.716364a46.545455 46.545455 0 0 1-38.167272 20.014545H374.690909a46.545455 46.545455 0 0 1-39.330909-21.643636z"
    }
    
    tmp = './源数据/国家统计局分省年度数据/国民经济核算/居民消费水平.csv'
    obj1 = pd.read_csv(tmp)
    obj2 = obj1[~obj1['年份'].isin([2018,2019])]#选取含有指定值的行从表中删除：~
    obj3 = obj2.reset_index(drop=True)
    
    tmp1 = 0
    tmp2 = []
    for i in range(0,31):
        tmp2.append(obj2['省份'].tolist()[tmp1])
        tmp1 += 18
    
    z = np.array(obj3['居民消费水平(元)'])
    z_1 = []
    for i in range(0, len(z), 18):#18
        z_1.append(z[i : i+18])#18
    z_1 = np.array(z_1).T
    z_2 = list(z_1)

    tl = Timeline()
    count = 0
    for i in range(2017, 1999, -1):
        bar = (
                PictorialBar()
                .add_xaxis(tmp2)
                .add_yaxis(
                            "分省居民消费水平值数",
                            [int(i) for i in list(z_2[count])],
                            label_opts=opts.LabelOpts(is_show=False),
                            symbol_size=9,
                            symbol_repeat="fixed",
                            symbol_offset=[0, 0],
                            is_symbol_clip=True,
                            symbol=symbols["消费"],
                )                
                .reversal_axis()
                .set_global_opts(
                    title_opts=opts.TitleOpts("Visualization of CPI index by Region in {}".format(i),pos_left = '0%',
                                             title_textstyle_opts=opts.TextStyleOpts( font_size=12)),
                    xaxis_opts=opts.AxisOpts(is_show=False),
                    yaxis_opts=opts.AxisOpts(
                        axislabel_opts=opts.LabelOpts(font_size=9),
                        axistick_opts=opts.AxisTickOpts(is_show=False),
                        axisline_opts=opts.AxisLineOpts(
                            linestyle_opts=opts.LineStyleOpts(opacity=0)
                        ),
                    ),
                )
                )
        count += 1
        tl.add(bar, "{}年".format(i))
    tl.add_schema(is_auto_play=True,is_rewind_play=True,play_interval = 900)
    return tl

def ec5():
    url = './源数据/国家统计局年度数据/国民经济核算/分行业增加值.csv'
    obj1 = pd.read_csv(url)
    obj2 = obj1.set_index('年份')
    obj2.columns=['年份','农林牧渔业','工业','建筑业','批发和零售业','交通运输、仓储和邮政业','住宿和餐饮业','金融业','房地产业','其他行业']
    obj3 = pd.DataFrame(obj2,columns=['农林牧渔业','工业','建筑业','批发和零售业','交通运输、仓储和邮政业','住宿和餐饮业','金融业','房地产业','其他行业'])
    tl = Timeline()
    count = 0
    for i in range(2019, 1999, -1):
        tmp = []
        x = obj3.columns.tolist()
        y = [y for y in dict(obj3.iloc[count,]).values()]
        for a,b in zip(x,y):
            tmp.append((a,b))
        pie = (
            Pie(init_opts=opts.InitOpts(width="1280px", height="610px"))
            .add(
                "",
                tmp,
                rosetype="radius",
                radius=["30%", "55%"],
            )
            .set_global_opts(title_opts=opts.TitleOpts(title="Visualization of GDP contribution by industry in {}".format(i),
                                                       pos_left="center",
                                                       pos_top="50",
                                                       title_textstyle_opts=opts.TextStyleOpts(color="#272727"),
                                                      ),
                            )
        )
        count += 1
        tl.add(pie, "{}年".format(i))
        tl.add_schema(is_auto_play=True,is_rewind_play=True)
    return tl

def ec6():
    tmp = './源数据/国家统计局年度数据/国民经济核算/国内生产总值.csv'
    obj1 = pd.read_csv(tmp)
    x = np.array(obj1['年份'])
    # y1 = np.array(obj1['国民总收入'])
    y2 = np.array(obj1['第一产业增加值'])
    y3 = np.array(obj1['第二产业增加值'])
    y4 = np.array(obj1['第三产业增加值'])
    y5 = np.array(obj1['国内生产总值'])
    # y6 = np.array(obj1['人均国内生产总值'])
    x = [str(i)+'年' for i in x[::-1]]
    def set_y(x):
        tmp = [round(i) for i in x[::-1]]
        return tmp
    c = (
        Bar(init_opts=opts.InitOpts(width="1280px", height="610px"))
        .add_xaxis(x)
    #     .add_yaxis("国民总收入", set_y(y1), stack="stack1")
        .add_yaxis("第一产业增加值",set_y(y2), stack="stack1")
        .add_yaxis("第二产业增加值", set_y(y3), stack="stack1")
        .add_yaxis("第三产业增加值", set_y(y4), stack="stack1")
        .add_yaxis("国内生产总值", set_y(y5), stack="stack1")
    #     .add_yaxis("人均国内生产总值", set_y(y6), stack="stack1")

        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(title_opts=opts.TitleOpts(title="三大产业GDP贡献指数"),
                        datazoom_opts=opts.DataZoomOpts(),
                        toolbox_opts=opts.ToolboxOpts(),
                        legend_opts=opts.LegendOpts(is_show=True)
                        )
    )
    return c

def ec7():
    url = './源数据/国家统计局年度数据/国民经济核算/三次产业构成.csv'
    obj1 = pd.read_csv(url)
    obj2 = obj1.set_index('年份')
    obj2.columns=['年份','第一产业增加值','第二产业增加值','第三产业增加值']
    obj3 = pd.DataFrame(obj2,columns=['第一产业增加值','第二产业增加值','第三产业增加值'])

    tl = Timeline()
    count = 0
    x = obj3.columns.tolist()
    for i in range(2019, 1999, -1):
        tmp = []
        y = [y for y in dict(obj3.iloc[count,]).values()]
        for a,b in zip(x,y):
            tmp.append((a,b))
        pie = (
            Pie(init_opts=opts.InitOpts(width="1280px", height="610px"))
            .add(
                "",
                tmp,
                rosetype="radius",
                radius=["30%", "55%"],
            )
            .set_global_opts(title_opts=opts.TitleOpts(title="Visualization of GDP contribution proportion of three major industries in {}".format(i),
                                                       pos_left="center",
                                                       pos_top="50",
                                                       title_textstyle_opts=opts.TextStyleOpts(color="#272727"),
                                                      ),
                            )
        )
        count += 1
        tl.add(pie, "{}年".format(i))
        tl.add_schema(is_auto_play=True,is_rewind_play=True)
    return tl






