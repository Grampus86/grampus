import matplotlib.pyplot as plt
import pandas as pd

from grampus.sci_toolkit import get_interpo_data
from grampus.pd_toolkits import Process_data_flame
from grampus.plt_toolkits import Plot3d, PlotScatter

pdf = Process_data_flame()
file_name_list = pdf.get_excel_sheet_name('data.xlsx')
sheetname = file_name_list[0]

df = pd.read_excel('data.xlsx', sheet_name=sheetname, index_col=0)
x_array, y_array, z_array = pdf.to_xyz_array(df)
xx_array, yy_array, zz_array = get_interpo_data(x_array, y_array, z_array, x_mesh=100, y_mesh=100)
fig, ax = plt.subplots(figsize=(6, 4), dpi=300)
pls1 = Plot3d.set_ax(figsize=(10, 10))
pls1.set_plot_layout(grid_axis='none')
pls1.set_aspect()
pls1.set_axis_range(x_min=-70, x_max=70, y_min=-70, y_max=70)
pls1.plot_color_map(xx_array, yy_array, zz_array, set_zmin=200, set_zmax=2000)
# pls1.set_axis_label(xlabel='X軸', ylabel='Y軸')
pls1.plt_show()
print('Done')
