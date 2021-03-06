import time
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable

# mathtext.FontConstantsBase = mathtext.ComputerModernFontConstants  # 上つき文字の補正

# Latex文字に対応
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams["mathtext.fontset"] = "stix"
plt.rcParams['font.size'] = 18


class Setplot(object):
    """
    プロットエリアを設定
    """

    def __init__(self, ax, fig):
        self.ax = ax
        self.fig = fig

    @classmethod
    def set_ax(cls, figsize=(8, 6), inner_facecolor='white', outer_facecolor='white', right=0.7):
        """
        fig,axを設定
        figsize=(横,縦)
        プロットエリアの大きさ、線の幅、色を決める。
        out_facecolorを'white'にしておくことでmonokaiで見にくくなる問題を回避
        """
        fig = plt.figure(figsize=figsize, facecolor=outer_facecolor, linewidth=10)
        fig.subplots_adjust(right=right)
        ax = fig.add_subplot(111)
        ax.set_facecolor(inner_facecolor)
        return cls(ax, fig)

    def set_aspect(self):
        """
        xy軸に合わせてアスペクト比を調整
        この時，figsizeも軸アスペクト比率に近い値にしておくとよい．
        """
        self.ax.set_aspect('equal')
        return self

    def set_plot_layout(self, grid_axis='both', grid_color='gray', fontsize=18, is_bottom_tick=True):
        """
        プロットエリアのグリット線と軸の数字の大きさを設定
        ax.grid線は、
        水平+垂直：'both'
        水平のみ：'y'
        垂直のみ：'x'
        なし:'none
        を引数にとる
        """
        self.ax.set_axisbelow(True)
        if grid_axis != 'none':
            self.ax.grid(axis=grid_axis, color=grid_color, linestyle='dashed', linewidth=0.8)
        self.ax.tick_params(labelsize=fontsize, direction='out',
                            length=5, colors='black', bottom=is_bottom_tick)
        self.ax.spines["top"].set_linewidth(1.0)
        self.ax.spines["left"].set_linewidth(1.0)
        self.ax.spines["bottom"].set_linewidth(1.0)
        self.ax.spines["right"].set_linewidth(1.0)
        self.ax.spines["top"].set_linewidth(1.0)
        self.ax.spines['top'].set_color('black')
        self.ax.spines['bottom'].set_color('black')
        self.ax.spines['left'].set_color('black')
        self.ax.spines['right'].set_color('black')
        return self

    def set_axis_range(self, x_min='null', x_max='null', y_min='null', y_max='null'):
        """
        軸の範囲を設定。
        'null'にしておくことで、autoにできる
        """
        if x_min == 'null' or x_max == 'null':
            self.ax.set_xlim(auto=True)
        else:
            self.ax.set_xlim([x_min, x_max])
        if y_min == 'null' or y_max == 'null':
            self.ax.set_ylim(auto=True)
        else:
            self.ax.set_ylim([y_min, y_max])
        return self

    def set_log(self, is_set_x=True, is_set_y=True):
        """
        軸をlogスケールにする
        """
        if is_set_x:
            self.ax.set_xscale('log')
        if is_set_y:
            self.ax.set_yscale('log')
        return self

    def set_axis_label(self, xlabel, ylabel, fontsize=18, font_name='MS Gothic'):
        """
        軸ラベルを設定。
        なしにしたい場合は''を入力
        """
        if xlabel != '':
            self.ax.set_xlabel(xlabel, fontsize=fontsize, fontname=font_name)
        if ylabel != '':
            self.ax.set_ylabel(ylabel, fontsize=fontsize, fontname=font_name)
        return self

    def set_legend(self, fontsize=14, loc='upper left'):
        """
        凡例を設定。
        """
        self.ax.legend(fontsize=fontsize, loc=loc, bbox_to_anchor=(1.05, 1),
                       fancybox=False, edgecolor="black", framealpha=1)
        return self

    def set_title(self, title, fontsize=14):
        self.ax.set_title(title, fontsize=fontsize)

    def replace_xticks(self, xticks_array, xticks_label, rad=0):
        """
        x軸の目盛りを置換
        axes.set_xticks()で
        文字列に置き換えたい座標に限定してから置き換える。
        """
        self.ax.set_xticks(xticks_array)
        self.ax.set_xticklabels(xticks_label, rotation=rad)
        return self

    def plt_show(self, is_plot=True):
        """
        グラフを表示する。
        notebook使用する場合は、
        インラインでグラフが表示されるので、
        させたくない場合は、'is_plot'を'False'にする
        """
        if is_plot:
            plt.show()
        # メモリ解放
        plt.clf()
        plt.close()
        return self

    def savefig(self, figname, dpi=300, is_append_datetime=True, save_dir_name='.'):
        """
        グラフを保存。
        日付を付けたければ、'is_append_datetime'を'True'にする
        """
        now = datetime.now()
        if is_append_datetime:
            save_file_name = '{0}_{1:%Y%m%d%H%M%S}'.format(figname, now)
        else:
            save_file_name = '{0}'.format(figname)
        plt.savefig('{0}/{1}.jpeg'.format(save_dir_name, save_file_name),
                    dpi=dpi, bbox_inches="tight")
        time.sleep(3)
        return self

    def return_ax(self):
        """
        axを返す
        """
        return self.ax

    def return_fig(self):
        """
        figを返す
        """
        return self.fig


class PlotScatter(Setplot):
    """
    散布図
    Setplotを継承
    """

    def plot_scatter(self, x_data, y_data, label='data',
                     edgecolors='black', facecolor='None', **kwargs):
        """
        散布図を作成
        'ax.scatter'関係の細かい引数は'**kwargs'で投げる
        """
        self.ax.scatter(x_data, y_data, label=label,
                        edgecolors=edgecolors, facecolor=facecolor, s=80, **kwargs)
        return self


class PlotLine(Setplot):
    """
    折れ線グラグ
    """

    def plot_line(self, x_data, y_data, label='data', **kwargs):
        """
        折れ線グラフを作成
        """
        self.ax.plot(x_data, y_data, label=label, **kwargs)
        return self


class PlotBar(Setplot):
    """
    棒グラフ
    """

    def plot_bar(self, x_data, y_data, label='data', width=0.3, **kwargs):
        """
        棒グラフを作成
        """
        self.ax.bar(x_data, y_data, label=label, width=width, edgecolor='black',
                    linewidth=0.8, align="center", **kwargs)
        return self

    def mlt_plot_bar(self, x_data, y_data_list, label_list,
                     bar_color_list=('b', 'r', 'g', 'y', 'gray'), width=0.3, **kwargs):
        """
        横に複数並べた棒グラフを作成。
        幾つかの項目を比較するのに使用。
        棒グラフの位置は'if..else..'の部分で処理。
        :param x_data: 各棒グラフのx軸位置情報
        :param y_data_list: 棒グラフの高さ
        :param label_list: 凡例。グラフに表示させるときは、'set_legend'
        :param bar_color_list: 棒グラフの色。デフォルトで、青、赤、緑、黄色の順
        :param width: 棒一本幅
        :param kwargs: 'ax.plotbar'関係の詳細な引数を投げる
        :return: self
        """
        len_data = len(y_data_list)
        if len_data % 2 == 0:
            st_bar_loc = x_data + 0.5 * width * (1 - len_data)
        else:
            st_bar_loc = x_data - width * (len_data - 1) * 0.5

        for i, (y_data, label) in enumerate(zip(y_data_list, label_list)):
            try:
                self.plot_bar(st_bar_loc, y_data, label=label, width=width, color=bar_color_list[i], **kwargs)
                st_bar_loc += width
            except IndexError:
                print('ERROE : `bar_color_list`に色のリストを追加してください')
                break
        return self


class Plot3d(Setplot):

    def plot_color_map(self, xx_array, yy_array, zz_array, cmap="jet",
                       set_zmin='null', set_zmax='null', fontsize=18):
        """
        3次元カラーマップを作成
        カラーバーの数字のサイズは当スクリプトの一番上の`plt.rcParams['font.size'] = 18`
        で規定．それ以外の方法については，今のところわからない．
        [20220118]
        x,y軸の目盛りサイズは`set_plot_layout`で規定する．
        plt.tick_params(label=18)で規定できる．->機能追加
        参考:https://qiita.com/aisha/items/6c84a734b6bd1605b5c9
        :param xx_array: meshgridで生成した2次元ndarray
        :param yy_array: meshgridで生成した2次元ndarray
        :param zz_array: meshgridで生成した2次元ndarray
        :param cmap: デフォルトはjet
        :param set_zmin: カラーバーの最小値．デフォルトはzz_arrayの最小値
        :param set_zmax: カラーバーの最大値．デフォルトはzz_arrayの最大値
        :return:
        """
        if set_zmin == 'null':
            vmin = np.min(zz_array)
        else:
            vmin = set_zmin
        if set_zmax == 'null':
            vmax = np.max(zz_array)
        else:
            vmax = set_zmax
        cnt = plt.pcolormesh(xx_array, yy_array, zz_array, cmap=cmap,
                             vmin=vmin, vmax=vmax, shading='auto')
        divider = make_axes_locatable(self.ax)
        cax = divider.append_axes("right", size="5%", pad=0.2)
        plt.colorbar(cnt, ax=self.ax, cax=cax)
        plt.tick_params(labelsize=fontsize)
        return self


if __name__ == '__main__':
    pass
