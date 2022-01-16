import os
import sys

from grampus.plt_toolkits import PlotScatter, PlotLine, PlotBar
import numpy as np
import pandas as pd

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

x = np.linspace(0, 10, 10)
y1 = np.linspace(0, 1, 10)
y2 = np.linspace(0.2, 0.4, 10)
y3 = np.linspace(0.9, 0.1, 10)
y4 = np.linspace(0.5, 0.5, 10)
y5 = np.linspace(0.8, 0.8, 10)

"""
散布図
"""
pls1 = PlotScatter.set_ax(figsize=(10, 2))
pls1.set_plot_layout(grid_axis='none')
pls1.set_axis_range(x_min=0, x_max=10, y_min=0, y_max=4)
pls1.set_axis_label(xlabel='$\mathrm{cm^2}$', ylabel='xy', font_name='Times New Roman')
pls1.plot_scatter(x, y1, label='data1$\mu$', facecolor='r', marker='o')
pls1.plot_scatter(x, y2, label='data2', facecolor='b', marker='v')
pls1.set_aspect()
pls1.set_legend()
pls1.plt_show()
#
pls2 = PlotScatter.set_ax()
pls2.set_plot_layout()
pls2.set_axis_range(x_min=0, x_max=10, y_min=0, y_max=10)
pls2.plot_scatter(x, y3, label='d', facecolor='g', marker='D')
pls2.plot_scatter(x, y4, label='data4\n($\Delta d$)', facecolor='y', marker='s')
pls2.plot_scatter(x, y5, label='data5', facecolor='None', marker='o')
pls2.set_legend(fontsize=10)
pls2.plt_show()
#

"""
ライン
"""
pll = PlotLine.set_ax()
pll.set_plot_layout()
pll.set_axis_range(x_min=0, x_max=10, y_min=0, y_max=10)
pll.plot_line(x, y1, linewidth=1, color="red", linestyle="dashed", marker="o", markersize=4)
pll.plot_line(x, y2, linewidth=1, color="b", linestyle="dashed", marker="v", markersize=4)
pll.plt_show()

"""
棒グラフ
"""
"""
'test_data.xlsx'の中身
     col1 col2 col3	col4 col5
row1 0.4 0.2 0.2 0.3 0.1
row2 0.1 0.2 0.3 0.4 0.1
row3 0.9 0.3 0.0 0.1 0.2
"""

df = pd.read_excel('test_data.xlsx', index_col=0)
by1 = df['col1'].to_numpy()
by2 = df['col2'].to_numpy()
by3 = df['col3'].to_numpy()
by4 = df['col4'].to_numpy()
by5 = df['col5'].to_numpy()
y_list = [by1, by2, by3, by4, by5]
xb = np.array([2, 5, 8])
label_list = df.columns.tolist()
xticks_label = df.index.tolist()
plb = PlotBar.set_ax()
plb.set_plot_layout(grid_axis='y')
plb.set_axis_range(x_min=0, x_max=10, y_min=0, y_max=1)
plb.mlt_plot_bar(x_data=xb, y_data_list=y_list, width=.4, label_list=label_list)
plb.set_legend()
plb.replace_xticks(xb, xticks_label)
plb.plt_show()

"""
棒グラフ & ライン
"""
df = pd.read_excel('test_data.xlsx', index_col=0)
by1 = df['col1'].to_numpy()
by2 = df['col2'].to_numpy()
by3 = df['col3'].to_numpy()
y_list = [by1, by2, by3]
xb = np.array([2, 5, 8])
label_list = df.columns.tolist()
xticks_label = df.index.tolist()
plb = PlotBar.set_ax()
plb.set_plot_layout(grid_axis='y')
plb.set_axis_range(x_min=0, x_max=10, y_min=0, y_max=1)
plb.mlt_plot_bar(x_data=xb, y_data_list=y_list, width=.4, label_list=label_list)
plb.set_legend()
plb.replace_xticks(xb, xticks_label)
ax = plb.return_ax()
fig = plb.return_fig()
pll = PlotLine(ax, fig)
pll.plot_line(x, y1, linewidth=1, color="red", linestyle="dashed", marker="o", markersize=4)
pll.plot_line(x, y2, linewidth=1, color="b", linestyle="dashed", marker="v", markersize=4)
pll.set_legend()
pll.plt_show()
