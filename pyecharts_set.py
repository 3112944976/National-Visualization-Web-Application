#!/usr/bin/env python
# coding: utf-8
from pyecharts import options as opts 
from pyecharts.charts import Map,Bar,Line,Page,Pie,Timeline,Gauge,Bar3D,Tab,Grid,PictorialBar
from pyecharts.globals import ChartType, SymbolType,ThemeType
from pyecharts.commons.utils import JsCode

def Bar_with_brush(df):
    y_1 = df[df.columns.tolist()[0]].tolist()
    c = (
    Bar()
    .add_xaxis(df.index.tolist())
    .add_yaxis(y_1)
#     .set_global_opts(title_opts=opts.TitleOpts(title="", subtitle=""))
    )
    return c


