#!/usr/bin/env python
# coding: utf-8
import pandas as pd
import numpy as np
from pyecharts import options as opts 
from pyecharts.charts import Map,Bar,Line,Page,Pie,Timeline,Gauge,Map3D,Tab,Grid,PictorialBar
from pyecharts.globals import ChartType, SymbolType,ThemeType
from pyecharts.commons.utils import JsCode
import json

def po1():
    obj1 = pd.read_csv('./源数据/国家统计局年度数据/人口/人口出生率、死亡率和自然增长率.csv')
    obj1 = obj1.sort_values('年份',ascending=True)
    x = [str(i)+'年' for i in obj1['年份'].tolist()]
    y1 = obj1['人口出生率'].tolist()
    y2 = obj1['人口死亡率'].tolist()
    y3 = obj1['人口自然增长率'].tolist()

    c = (
        Line(init_opts=opts.InitOpts(theme=ThemeType.VINTAGE))
        .add_xaxis(x)
        .add_yaxis("人口出生率", y1, is_smooth=True,
                   markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(type_="average", name="平均值")])
                  )
        .add_yaxis("人口死亡率", y2, is_smooth=True,
                   markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(type_="average", name="平均值")])
                  )
        .add_yaxis("人口自然增长率", y3, is_smooth=True,
                   markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(type_="average", name="平均值")])
                  )
        .set_global_opts(title_opts=opts.TitleOpts(title="人口出生/死亡及自然增长率"),
                         yaxis_opts=opts.AxisOpts(
                             axislabel_opts=opts.LabelOpts(formatter="{value} %"),interval=10,name="",min_=0,max_=15),
                             tooltip_opts=opts.TooltipOpts(trigger="axis"),
                            toolbox_opts=opts.ToolboxOpts(is_show=True),
                            xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=False),
                        )
    )
    return c

def po2():
    url = "./源数据/国家统计局年度数据/人口/人口年龄结构和抚养比.csv"
    obj1 = pd.read_csv(url)
    obj2 = obj1.set_index('年份')
    obj3 = pd.DataFrame(obj2,columns=['0-14岁人口','15-64岁人口','65岁及以上人口'])

    tl = Timeline()
    count = 0
    for i in range(2019, 1999, -1):
        tmp = []
        x = obj3.columns.tolist()
        y = [y for y in dict(obj3.iloc[count,]).values()]
        for a,b in zip(x,y):
            tmp.append((a,b))
        pie = (
            Pie(init_opts=opts.InitOpts(theme=ThemeType.VINTAGE))
            .add(
                "",
                tmp,
                rosetype="radius",
                radius=["30%", "55%"],
            )
            .set_global_opts(title_opts=opts.TitleOpts(title="{0}年人口年龄结构动态饼状图".format(i),
                                                       pos_left="center",
                                                       pos_top="50",
                                                       title_textstyle_opts=opts.TextStyleOpts(color="#FF8040"),
                                                      ),
                            )
        )
        count += 1
        tl.add(pie, "{}年".format(i))
        tl.add_schema(is_auto_play=True,is_rewind_play=True)
    return tl

def po3():
    url = "./源数据/国家统计局年度数据/人口/总人口.csv"
    obj1 = pd.read_csv(url)
    x = np.array(obj1['年份'])
    y1 = np.array(obj1['年末总人口'])
    y2 = np.array(obj1['男性人口'])
    y3 = np.array(obj1['女性人口'])
    x = [str(i)+'年' for i in x[::-1]]
    def set_y(x):
        tmp = [round(i) for i in x[::-1]]
        return tmp

    bar = (
        Bar(init_opts=opts.InitOpts(width="1680px", 
                                    height="800px", 
                                    #bg_color="dimgray", 
                                    theme=ThemeType.VINTAGE,
                                    animation_opts=opts.AnimationOpts(animation_delay=1000, animation_easing="elasticOut")
                                   )
           )
        .add_xaxis(xaxis_data=x)
        .add_yaxis(series_name="男性人口",y_axis=set_y(y2),yaxis_index=0)
        .add_yaxis(series_name="女性人口", y_axis=set_y(y3), yaxis_index=1)


        .extend_axis(
            yaxis=opts.AxisOpts(
                name="",
                #type_="value",
                min_=0,
                max_=200000,
                position="right",
                axisline_opts=opts.AxisLineOpts(linestyle_opts=opts.LineStyleOpts(color="#F75000")),
                axislabel_opts=opts.LabelOpts(formatter="{value}"),
            )
        )
        .extend_axis(
            yaxis=opts.AxisOpts(
                #type_="value",
                name="",
                min_=0,
                max_=200000,
                position="center",
                axisline_opts=opts.AxisLineOpts(linestyle_opts=opts.LineStyleOpts(color="#F75000")),
                axislabel_opts=opts.LabelOpts(formatter="{value}"),
                splitline_opts=opts.SplitLineOpts(is_show=True, linestyle_opts=opts.LineStyleOpts(opacity=1)),
            )
        )

        .set_series_opts(itemstyle_opts={"normal": {"barBorderRadius": [30, 30, 30, 30],}})
        .set_global_opts(
            title_opts=opts.TitleOpts(title=""),#, subtitle="我是副标题"
            datazoom_opts=[opts.DataZoomOpts(), opts.DataZoomOpts(type_="inside")],


            toolbox_opts=opts.ToolboxOpts(is_show=True),
            xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=False),

            yaxis_opts=opts.AxisOpts(
                #type_="value",
                name="",
                min_=0,
                max_=200000,
                position="right",
                #offset=80,
                axisline_opts=opts.AxisLineOpts(linestyle_opts=opts.LineStyleOpts(color="#0066CC")),
                axislabel_opts=opts.LabelOpts(formatter="{value}"),
            ),
            tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
        )
    )

    line = (
        Line()
        .add_xaxis(xaxis_data=x)
        .add_yaxis(series_name="年末总人口", y_axis=set_y(y1), yaxis_index=2)
    )
    return bar.overlap(line)

def po4():
    symbols = {
    "人": 'path://M408 350c0-9.941-8.059-18-18-18s-18 8.059-18 18v246h-0.098c-1.274 16.229-14.847 29-31.402 29h-3c-17.397 0-31.5-14.103-31.5-31.5V254c0-28.167 22.833-51 51-51h310c28.167 0 51 22.833 51 51v339.5c0 17.397-14.103 31.5-31.5 31.5-16.555 0-30.128-12.771-31.402-29H655V350c0-9.83-7.88-17.82-17.67-17.997L637 332c-9.941 0-18 8.059-18 18v601.5c0 26.234-21.266 47.5-47.5 47.5S524 977.734 524 951.5V596h-21v355.5c0 26.234-21.266 47.5-47.5 47.5S408 977.734 408 951.5zM512.5 25c44.459 0 80.5 36.041 80.5 80.5S556.959 186 512.5 186 432 149.959 432 105.5 468.041 25 512.5 25z'
    }
    tmp = "./源数据/国家统计局分省年度数据/人口/人口抽样调查样本数据/按婚姻状况分人口数(人口抽样调查).csv"
    obj1 = pd.read_csv(tmp)
    obj2 = obj1[~obj1['年份'].isin([2000,2001,2010])]#选取含有指定值的行从表中删除：~
    obj3 = obj2.reset_index(drop=True)
    obj4 = pd.DataFrame(obj3,columns=['省份','年份','15岁及以上男性未婚人口数(人口抽样调查)(人)','15岁及以上女性未婚人口数(人口抽样调查)(人)'])
    obj5 = obj4[obj4['年份'] == 2019]
    obj6 = obj5.reset_index(drop=True)

    name_list = [i for i in obj4[obj4['年份'] == 2019]['省份'].tolist()]
    time_list = [i for i in obj4[obj4['省份'] == '北京市']['年份'].tolist()]

    def men(x):
        tmp1 = obj4[obj4['年份'] == int(x)]
        tmp2 = tmp1.reset_index(drop=True)
        return tmp2['15岁及以上男性未婚人口数(人口抽样调查)(人)'].tolist()
    def women(x):
        tmp1 = obj4[obj4['年份'] == int(x)]
        tmp2 = tmp1.reset_index(drop=True)
        return tmp2['15岁及以上女性未婚人口数(人口抽样调查)(人)'].tolist()

    tl = Timeline()
    for i in time_list:
        bar = (
                PictorialBar()
                .add_xaxis(name_list)
                .add_yaxis(
                            "男性未婚人口数",
                            men(i),
                            label_opts=opts.LabelOpts(is_show=False),
                            symbol_size=9,
                            symbol_repeat="fixed",
                            symbol_offset=[0, 0],
                            is_symbol_clip=True,
                            symbol=symbols["人"],
                )


                .add_yaxis(
                            "女性未婚人口数",
                            women(i),
                            label_opts=opts.LabelOpts(is_show=False),
                            symbol_size=9,
                            symbol_repeat="fixed",
                            symbol_offset=[0, 0],
                            is_symbol_clip=True,
                            symbol=symbols["人"],
                )                
                .reversal_axis()
                .set_global_opts(
                    title_opts=opts.TitleOpts(title="分地区分性别未婚人数抽样调查可视化"),
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
        tl.add(bar, "{}年".format(i))
    tl.add_schema(is_auto_play=True,is_rewind_play=True,play_interval = 900)
    return tl