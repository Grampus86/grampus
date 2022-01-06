"""
エクセルのデータからカラーマップを作成．
各シートのデータ分だけ図が作成される．
ただし，シート名が'_'から始まるものは無視される．
'sample_data.xlsx'の場合
'sample_1','sample_2'のみ読み込まれ，図が作成される．
'_sample_3'はシート名が'_'から始まるため無視される.
"""

import pandas as pd
from grampus.sci_toolkits import get_interpo_data
from grampus.pd_toolkits import Process_data_flame
from grampus.plt_toolkits import Plot3d

"""
必ず設定
"""
file_name = 'sample_data.xlsx'  # エクセルファイル名
figsize = (10, 10)  # 図サイズ，アスペクト比とおよそ同じ比率にする
xlabel = 'x axis $\mathrm{(J \cdot K^{-1})}$'  # X軸ラベル
ylabel = 'y axis $\mathrm{(cm^2)}$'  # Y軸ラベル
y_axis_min = 0  # Y軸最小値
y_axis_max = 100  # Y軸最大値
x_axis_min = 0  # X軸最小値
x_axis_max = 100  # X軸最大値
z_axis_min = 0  # Z軸最小値(カラーバー最小値)
z_axis_max = 3000  # Z軸最小値(つまりカラーバー最大値)

"""
任意設定
"""
x_mesh = 100  # X方向メッシュ数
y_mesh = 100  # X方向メッシュ数
dpi = 300  # 図の解像度
font_name = 'Times New Roman'

"""
処理内容
"""

pdf = Process_data_flame()
# エクセルシート名取得
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
    plc.set_axis_label(xlabel=xlabel, ylabel=ylabel,font_name=font_name)
    plc.savefig(sheetname, dpi=dpi, is_append_datetime=True)
print('Done')
