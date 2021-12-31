import matplotlib.pyplot as plt
import pandas as pd

from grampus.sci_toolkit import get_interpo_data
from grampus.pd_toolkits import Process_data_flame
from grampus.plt_toolkits import Plot3d

file_name = 'data.xlsx'
figsize = (10, 10)
# xlabel = 'X軸'
# ylabel = 'Y軸'
xlabel = 'X'
ylabel = 'Y'
y_axis_min = 0
y_axis_max = 100
x_axis_min = 0
x_axis_max = 100
z_axis_min = 0
z_axis_max = 3000
x_mesh = 100
y_mesh = 100
dpi = 300

pdf = Process_data_flame()
file_name_list = pdf.get_excel_sheet_name(file_name)
for sheetname in file_name_list:
    df = pd.read_excel(file_name, sheet_name=sheetname, index_col=0)
    x_array, y_array, z_array = pdf.to_xyz_array(df)
    xx_array, yy_array, zz_array = get_interpo_data(x_array, y_array, z_array, x_mesh=x_mesh, y_mesh=y_mesh)
    plc = Plot3d.set_ax(figsize=figsize)
    plc.set_plot_layout(grid_axis='none')
    plc.set_aspect()
    plc.set_axis_range(x_min=x_axis_min, x_max=x_axis_max, y_min=y_axis_min, y_max=y_axis_max)
    plc.plot_color_map(xx_array, yy_array, zz_array, set_zmin=z_axis_min, set_zmax=z_axis_max)
    # plc.set_axis_label(xlabel=xlabel, ylabel=ylabel)
    plc.savefig(sheetname, dpi=dpi)
print('Done')
