from scipy.interpolate import RegularGridInterpolator
import numpy as np


class ProcessArray(object):
    def __init__(self):
        pass

    @staticmethod
    def get_xy_grid(x_array, y_array, x_mesh=100, y_mesh=100):
        """
        x,yメッシュを作成
        """
        meshed_x_array = np.linspace(x_array[0], x_array[-1], x_mesh)
        meshed_y_array = np.linspace(y_array[0], y_array[-1], y_mesh)
        xx_array, yy_array = np.meshgrid(meshed_x_array, meshed_y_array)
        return xx_array, yy_array


class Interpolation(object):
    """
    データの補完
    """

    def __init__(self):
        pass

    @staticmethod
    def exec_interpo(x_array, y_array, z_array):
        """
        n次元線型補間
        """
        ff = RegularGridInterpolator((y_array, x_array), z_array)
        return ff

    @staticmethod
    def get_xi(xx_array, yy_array):
        """
        x，y座標のペアの行列を作成
        get_obj_varで用いる
        """
        xi_array = np.array([yy_array, xx_array]).transpose()
        return xi_array

    @staticmethod
    def get_obj_var(ff, xi_array):
        """
        補間を利用して目的変数を取得
        """
        zz_array = ff(xi_array).transpose()
        return zz_array
