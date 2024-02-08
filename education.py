#!/usr/bin/env python
# coding: utf-8
import json
import pandas as pd
import numpy as np
from pyecharts import options as opts 
from pyecharts.charts import Map,Bar,Line,Page,Pie,Timeline,Gauge,Bar3D,Tab,Grid,PictorialBar
from pyecharts.globals import ChartType, SymbolType,ThemeType
from pyecharts.commons.utils import JsCode

# 分地区高校数（动态象型图）
def ed1():
    symbols = {
    "a":"path://M488.6 651.5c4.3 2 9.3 2 13.7 0l234.1-111v159c0 6.1-3.4 11.7-8.9 14.5L502.6 827.4c-4.5 2.3-9.8 2.3-14.4 0L203.5 714.1c-5.5-2.7-8.9-8.3-8.9-14.5V540.5l294 111zM836 359v440.1c0 16.5-13.4 29.9-29.9 29.9s-29.9-13.4-29.9-29.9V371.4l-39.7 9.3v110.4l-241 114.2-300.9-114.2V377l-78-25.2c-6.2-2.4-10.3-8.4-10.3-15s4.1-12.6 10.3-15l372.9-149c3.8-1.5 8-1.5 11.8 0l373 149c6.1 2.5 10.2 8.4 10.2 15s-4 12.6-10.2 15L836 359z"
    }
    obj1 = pd.read_csv('./源数据/国家统计局分省年度数据/教育/高等学校普通本、专科学校和学生情况.csv')
    name_list = [i for i in obj1[obj1['年份'] == 2019]['省份'].tolist()]
    time_list = [i for i in obj1[obj1['省份'] == '北京市']['年份'].tolist()]

    def demo(x):
        tmp1 = obj1[obj1['年份'] == int(x)]
        tmp2 = tmp1.reset_index(drop=True)
        return tmp2['普通高等学校数(所)'].tolist()

    tl = Timeline()
    for i in time_list:
        bar = (
                PictorialBar()
                .add_xaxis(name_list)
                .add_yaxis(
                            "普通高等学校数(所)",
                            demo(i),
                            label_opts=opts.LabelOpts(is_show=False),
                            symbol_size=9,
                            symbol_repeat="fixed",
                            symbol_offset=[0, 0],
                            is_symbol_clip=True,
                            symbol=symbols["a"],
                )               
                .reversal_axis()
                .set_global_opts(
                    title_opts=opts.TitleOpts(title="分地区高校数量"),
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

# 分地区高等学校在校学生数 $ 分地区高等学校本专科在校学生数（静态折线图）
def ed2():
    obj1 = pd.read_csv('./源数据/国家统计局年度数据/教育/高等学校普通本、专科学校和学生情况.csv')
    obj1 = obj1.sort_values('年份',ascending=True)
    x = [str(i)+'年' for i in obj1['年份'].tolist()]
    y1 = obj1['普通高等学校在校学生数'].tolist()
    y2 = obj1['普通高等学校本科在校学生数'].tolist()
    y3 = obj1['普通高等学校专科在校学生数'].tolist()

    c = (
        Line(init_opts=opts.InitOpts(width="1100px", height="520px",theme=ThemeType.VINTAGE))
        .add_xaxis(x)
        .add_yaxis("高校在校生数", y1, is_smooth=True,
                   markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(type_="average", name="平均值")])
                  )
        .add_yaxis("高校本科在校生数", y2, is_smooth=True,
                   markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(type_="average", name="平均值")])
                  )
        .add_yaxis("高校专科在校生数", y3, is_smooth=True,
                   markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(type_="average", name="平均值")])
                  )
        .set_global_opts(title_opts=opts.TitleOpts(title="高校本专科在校生数(万人)"),
                         yaxis_opts=opts.AxisOpts(
                             axislabel_opts=opts.LabelOpts(formatter="{value}"),interval=320,name="",min_=0,max_=3200),
                             tooltip_opts=opts.TooltipOpts(trigger="axis"),
                            toolbox_opts=opts.ToolboxOpts(is_show=True),
                            xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=False),
                        )
    )
    return c

# 高等学校毕业学生数 $ 高等学校本专科毕业学生数（静态折线图）
def ed3():
    obj1 = pd.read_csv('./源数据/国家统计局年度数据/教育/高等学校普通本、专科学校和学生情况.csv')
    obj1 = obj1.sort_values('年份',ascending=True)
    x = [str(i)+'年' for i in obj1['年份'].tolist()]
    y1 = obj1['普通高等学校毕(结)业生数'].tolist()
    y2 = obj1['普通高等学校本科毕(结)业生数'].tolist()
    y3 = obj1['普通高等学校专科毕(结)业生数'].tolist()

    c = (
        Line(init_opts=opts.InitOpts(width="1100px", height="520px",theme=ThemeType.VINTAGE))
        .add_xaxis(x)
        .add_yaxis("高校在校生数", y1, is_smooth=True,
                   markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(type_="average", name="平均值")])
                  )
        .add_yaxis("高校本科在校生数", y2, is_smooth=True,
                   markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(type_="average", name="平均值")])
                  )
        .add_yaxis("高校专科在校生数", y3, is_smooth=True,
                   markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(type_="average", name="平均值")])
                  )
        .set_global_opts(title_opts=opts.TitleOpts(title="高校本专科毕(结)业生数(万人)"),
                         yaxis_opts=opts.AxisOpts(
                             axislabel_opts=opts.LabelOpts(formatter="{value}"),interval=80,name="",min_=0,max_=800),
                             tooltip_opts=opts.TooltipOpts(trigger="axis"),
                            toolbox_opts=opts.ToolboxOpts(is_show=True),
                            xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=False),
                        )
    )
    return c

#  分地区普高学校数（动态2D地图）
def ed4():
    obj1 = pd.read_csv('./源数据/国家统计局分省年度数据/教育/普通高中基本情况.csv')
    obj2 = obj1[obj1['年份'].isin([2019])]
    x = [i[:2] for i in obj2['省份']]
    x[x.index('内蒙')] = '内蒙古'
    x[x.index('黑龙')] = '黑龙江'

    y = [i for i in obj1['普通高中学校数(所)']]
    y_2 = []
    for i in range(0,31):
        y_2.append(list(y[0:20]))
        y = y[20:]
    y_3 = np.array(y_2).T.tolist()

    tl = Timeline()
    count = 0
    for i in range(2019,1999,-1):
        map0 = (
            Map(init_opts=opts.InitOpts(bg_color="dimgray", theme=ThemeType.DARK))
            .add("", [list(z) for z in zip(x, y_3[count])], "china")
            .set_global_opts(
                title_opts=opts.TitleOpts(title="{}年分地区普高学校数量".format(i)),
                visualmap_opts=opts.VisualMapOpts(min_=10, 
                                                          max_=1200, 
                                                          is_piecewise=True, )
            )
        )
        count += 1
        tl.add(map0, "{}年".format(i))
        tl.add_schema(is_auto_play=True,is_rewind_play=True)
    return tl
# 分地区普高学校招生数、专任教师数（动态象型图）
def ed5():
    symbols = {
    "a":"path://M488.6 651.5c4.3 2 9.3 2 13.7 0l234.1-111v159c0 6.1-3.4 11.7-8.9 14.5L502.6 827.4c-4.5 2.3-9.8 2.3-14.4 0L203.5 714.1c-5.5-2.7-8.9-8.3-8.9-14.5V540.5l294 111zM836 359v440.1c0 16.5-13.4 29.9-29.9 29.9s-29.9-13.4-29.9-29.9V371.4l-39.7 9.3v110.4l-241 114.2-300.9-114.2V377l-78-25.2c-6.2-2.4-10.3-8.4-10.3-15s4.1-12.6 10.3-15l372.9-149c3.8-1.5 8-1.5 11.8 0l373 149c6.1 2.5 10.2 8.4 10.2 15s-4 12.6-10.2 15L836 359z"
    }
    obj1 = pd.read_csv('./源数据/国家统计局分省年度数据/教育/普通高中基本情况.csv')
    obj2 = obj1[~obj1['年份'].isin([2000,2001,2002,2003])]
    obj3 = obj2.reset_index(drop=True)
    
    name_list = [i for i in obj3[obj3['年份'] == 2019]['省份'].tolist()]
    time_list = [i for i in obj3[obj3['省份'] == '北京市']['年份'].tolist()]

    def demo(x):
        tmp1 = obj3[obj3['年份'] == int(x)]
        tmp2 = tmp1.reset_index(drop=True)
        return tmp2['普通高中招生数(万人)'].tolist()
    
    def demo2(x):
        tmp1 = obj3[obj3['年份'] == int(x)]
        tmp2 = tmp1.reset_index(drop=True)
        return tmp2['普通高中专任教师数(万人)'].tolist()

    tl = Timeline()
    for i in time_list:
        bar = (
                PictorialBar()
                .add_xaxis(name_list)
                .add_yaxis(
                            "",
                            demo(i),
                            label_opts=opts.LabelOpts(is_show=False),
                            symbol_size=9,
                            symbol_repeat="fixed",
                            symbol_offset=[0, 0],
                            is_symbol_clip=True,
                            symbol=symbols["a"],
                )
                .add_yaxis(
                            "",
                            demo2(i),
                            label_opts=opts.LabelOpts(is_show=False),
                            symbol_size=9,
                            symbol_repeat="fixed",
                            symbol_offset=[0, 0],
                            is_symbol_clip=True,
                            symbol=symbols["a"],
                )       
                .reversal_axis()
                .set_global_opts(
                    title_opts=opts.TitleOpts(title="分地区普通高中在校生与专任教师数量(万人)"),
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
# 分地区高等学校在校学生数、毕业生数（条形及折线复合图）
def ed6():
   
    obj1 = pd.read_csv( './源数据/国家统计局年度数据/教育/普通高中学校和学生情况/普通高中在校学生数.csv')
    obj2 = pd.read_csv( './源数据/国家统计局年度数据/教育/普通高中学校和学生情况/普通高中毕业生数.csv')

    x = [str(round(i))+'年' for i in list(np.array(obj1['年份']))]
    y1 = list(np.array(obj1['普通高中在校学生数']))
    y2 = list(np.array(obj2['普通高中毕业生数']))

    def round_set(x):
        x = [round(i, 0) for i in x]
        return x
    round_set(y1)
    round_set(y2)

    bar = (
        Bar(init_opts=opts.InitOpts(width="1680px", 
                                    height="800px", 
                                    theme=ThemeType.VINTAGE,
                                    animation_opts=opts.AnimationOpts(animation_delay=1000, animation_easing="elasticOut")
                                   )
           )
        .add_xaxis(xaxis_data=x[::-1])
        .add_yaxis(
            series_name="普通高中在校学生数",
            y_axis=y1[::-1],
            yaxis_index=0,
        )
        .add_yaxis(series_name="普通高中毕业生数", y_axis=y2[::-1], yaxis_index=1)
        .extend_axis(
            yaxis=opts.AxisOpts(
                name="",
                type_="value",
                min_=0,
                max_=4000,
                position="right",
                axisline_opts=opts.AxisLineOpts(linestyle_opts=opts.LineStyleOpts(color="#F75000")),
                axislabel_opts=opts.LabelOpts(formatter="{value}"),
            )
        )
        .extend_axis(
            yaxis=opts.AxisOpts(
                type_="value",
                name="",
                min_=0,
                max_=4000,
                position="left",
                axisline_opts=opts.AxisLineOpts(linestyle_opts=opts.LineStyleOpts(color="#F75000")),
                axislabel_opts=opts.LabelOpts(formatter="{value}"),
                splitline_opts=opts.SplitLineOpts(is_show=True, linestyle_opts=opts.LineStyleOpts(opacity=1)),
            )
        )
        .set_series_opts(itemstyle_opts={"normal": {"barBorderRadius": [30, 30, 30, 30],}})
        .set_global_opts(
            title_opts=opts.TitleOpts(title="普通高中在校生及毕业生数量（万人）"),#, subtitle="我是副标题"
            datazoom_opts=[opts.DataZoomOpts(), opts.DataZoomOpts(type_="inside")],


            toolbox_opts=opts.ToolboxOpts(is_show=True),
            xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=False),

            yaxis_opts=opts.AxisOpts(
                type_="value",
                name="",
                min_=0,
                max_=4000,
                position="right",
                axisline_opts=opts.AxisLineOpts(linestyle_opts=opts.LineStyleOpts(color="#0066CC")),
                axislabel_opts=opts.LabelOpts(formatter="{value}"),
            ),
            tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
        )
    )
    return bar

def ed7():
    
    obj1 = pd.read_csv( './源数据/国家统计局分省年度数据/教育/初中基本情况.csv')
    obj1 = obj1[~obj1['年份'].isin([_ for _ in range(2000,2011)])]
    obj1 = obj1.reset_index(drop=True)
    obj2 = obj1[obj1['年份'].isin([2019])]
    
    x = [i[:2] for i in obj2['省份']]
    x[x.index('内蒙')] = '内蒙古'
    x[x.index('黑龙')] = '黑龙江'

    y = [i for i in obj1['初中学校数(所)']]
    y_2 = []
    for i in range(0,31):
        y_2.append(list(y[0:9]))
        y = y[9:]
    y_3 = np.array(y_2).T.tolist()

    tl = Timeline()
    count = 0
    for i in range(2019,2010,-1):
        map0 = (
            Map(init_opts=opts.InitOpts(bg_color="dimgray", theme=ThemeType.DARK))
            .add("", [list(z) for z in zip(x, y_3[count])], "china")
            .set_global_opts(
                title_opts=opts.TitleOpts(title="{}年分地区初中学校数量".format(i)),
                visualmap_opts=opts.VisualMapOpts(min_=0, 
                                                          max_=5000, 
                                                          is_piecewise=True, )
            )
        )
        count += 1
        tl.add(map0, "{}年".format(i))
        tl.add_schema(is_auto_play=True,is_rewind_play=True)
    return tl

def ed8():
    symbols = {
    "a":"path://M488.6 651.5c4.3 2 9.3 2 13.7 0l234.1-111v159c0 6.1-3.4 11.7-8.9 14.5L502.6 827.4c-4.5 2.3-9.8 2.3-14.4 0L203.5 714.1c-5.5-2.7-8.9-8.3-8.9-14.5V540.5l294 111zM836 359v440.1c0 16.5-13.4 29.9-29.9 29.9s-29.9-13.4-29.9-29.9V371.4l-39.7 9.3v110.4l-241 114.2-300.9-114.2V377l-78-25.2c-6.2-2.4-10.3-8.4-10.3-15s4.1-12.6 10.3-15l372.9-149c3.8-1.5 8-1.5 11.8 0l373 149c6.1 2.5 10.2 8.4 10.2 15s-4 12.6-10.2 15L836 359z"
    }

    obj1 = pd.read_csv( './源数据/国家统计局分省年度数据/教育/初中基本情况.csv')
    obj2 = obj1[~obj1['年份'].isin([_ for _ in range(2000,2011)])]
    obj3 = obj2.reset_index(drop=True)
    
    name_list = [i for i in obj3[obj3['年份'] == 2019]['省份'].tolist()]
    time_list = [i for i in obj3[obj3['省份'] == '北京市']['年份'].tolist()]

    def demo(x):
        tmp1 = obj3[obj3['年份'] == int(x)]
        tmp2 = tmp1.reset_index(drop=True)
        return tmp2['初中在校学生数(万人)'].tolist()
    
    def demo2(x):
        tmp1 = obj3[obj3['年份'] == int(x)]
        tmp2 = tmp1.reset_index(drop=True)
        return tmp2['初中专任教师数(万人)'].tolist()

    tl = Timeline()
    for i in time_list:
        bar = (
                PictorialBar()
                .add_xaxis(name_list)
                .add_yaxis(
                            "",
                            demo(i),
                            label_opts=opts.LabelOpts(is_show=False),
                            symbol_size=9,
                            symbol_repeat="fixed",
                            symbol_offset=[0, 0],
                            is_symbol_clip=True,
                            symbol=symbols["a"],
                )
                .add_yaxis(
                            "",
                            demo2(i),
                            label_opts=opts.LabelOpts(is_show=False),
                            symbol_size=9,
                            symbol_repeat="fixed",
                            symbol_offset=[0, 0],
                            is_symbol_clip=True,
                            symbol=symbols["a"],
                )       
                .reversal_axis()
                .set_global_opts(
                    title_opts=opts.TitleOpts(title="分地区普通初中在校生与专任教师数量(万人)"),
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

def ed9():
    obj1 = pd.read_csv( './源数据/国家统计局分省年度数据/教育/普通小学基本情况.csv')
    obj2 = obj1[obj1['年份'].isin([2019])]
    
    x = [i[:2] for i in obj2['省份']]
    x[x.index('内蒙')] = '内蒙古'
    x[x.index('黑龙')] = '黑龙江'

    y = [i for i in obj1['普通小学学校数(所)']]
    y_2 = []
    for i in range(0,31):
        y_2.append(list(y[0:20]))
        y = y[20:]
    y_3 = np.array(y_2).T.tolist()

    tl = Timeline()
    count = 0
    for i in range(2019,1999,-1):
        map0 = (
            Map(init_opts=opts.InitOpts(bg_color="dimgray", theme=ThemeType.DARK))
            .add("", [list(z) for z in zip(x, y_3[count])], "china")
            .set_global_opts(
                title_opts=opts.TitleOpts(title="{}年分地区小学学校数量".format(i)),
                visualmap_opts=opts.VisualMapOpts(min_=500, 
                                                          max_=50000, 
                                                          is_piecewise=True, )
            )
        )
        count += 1
        tl.add(map0, "{}年".format(i))
        tl.add_schema(is_auto_play=True,is_rewind_play=True)
    return tl

def ed10():
    symbols = {
    "a":"path://M488.6 651.5c4.3 2 9.3 2 13.7 0l234.1-111v159c0 6.1-3.4 11.7-8.9 14.5L502.6 827.4c-4.5 2.3-9.8 2.3-14.4 0L203.5 714.1c-5.5-2.7-8.9-8.3-8.9-14.5V540.5l294 111zM836 359v440.1c0 16.5-13.4 29.9-29.9 29.9s-29.9-13.4-29.9-29.9V371.4l-39.7 9.3v110.4l-241 114.2-300.9-114.2V377l-78-25.2c-6.2-2.4-10.3-8.4-10.3-15s4.1-12.6 10.3-15l372.9-149c3.8-1.5 8-1.5 11.8 0l373 149c6.1 2.5 10.2 8.4 10.2 15s-4 12.6-10.2 15L836 359z"
    }
    obj1 = pd.read_csv( './源数据/国家统计局分省年度数据/教育/普通小学基本情况.csv')
    
    name_list = [i for i in obj1[obj1['年份'] == 2019]['省份'].tolist()]
    time_list = [i for i in obj1[obj1['省份'] == '北京市']['年份'].tolist()]

    def demo(x):
        tmp1 = obj1[obj1['年份'] == int(x)]
        tmp2 = tmp1.reset_index(drop=True)
        return tmp2['普通小学在校学生数(万人)'].tolist()
    
    def demo2(x):
        tmp1 = obj1[obj1['年份'] == int(x)]
        tmp2 = tmp1.reset_index(drop=True)
        return tmp2['普通小学专任教师数(万人)'].tolist()

    tl = Timeline()
    for i in time_list:
        bar = (
                PictorialBar()
                .add_xaxis(name_list)
                .add_yaxis(
                            "",
                            demo(i),
                            label_opts=opts.LabelOpts(is_show=False),
                            symbol_size=9,
                            symbol_repeat="fixed",
                            symbol_offset=[0, 0],
                            is_symbol_clip=True,
                            symbol=symbols["a"],
                )
                .add_yaxis(
                            "",
                            demo2(i),
                            label_opts=opts.LabelOpts(is_show=False),
                            symbol_size=9,
                            symbol_repeat="fixed",
                            symbol_offset=[0, 0],
                            is_symbol_clip=True,
                            symbol=symbols["a"],
                )       
                .reversal_axis()
                .set_global_opts(
                    title_opts=opts.TitleOpts(title="分地区小学在校生与专任教师数量(万人)"),
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

def ed11():
    obj1 = pd.read_csv( './源数据/国家统计局年度数据/教育/研究生和留学生数.csv')
    obj2 = obj1.set_index(obj1['年份'])
    obj3 = pd.DataFrame(obj2,columns=obj2.columns[1:6])
    obj3 = obj3.fillna(value=0)

    data = []
    for i in obj3.index:
        for j in obj3.columns:
            data.append((i,j,round(obj3[j][i],2)))

    c = (
        Bar3D()
        .add(
            "研究生及留学生(万人)",
            data,
            xaxis3d_opts=opts.Axis3DOpts(obj3.index, type_="category"),
            yaxis3d_opts=opts.Axis3DOpts(obj3.columns, type_="category"),
            zaxis3d_opts=opts.Axis3DOpts(type_="value"),
            #grid3d_opts=opts.Grid3DOpts(width=100, depth=100, rotate_speed=150, is_rotate=True)
        )
        .set_global_opts(visualmap_opts=opts.VisualMapOpts(max_=300),title_opts=opts.TitleOpts(title="研究生及留学生情况(万人)"))

    )
    return c