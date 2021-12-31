from scipy.interpolate import RegularGridInterpolator
from scipy import integrate
import numpy as np


def get_interpo_data(x_array, y_array, z_array, x_mesh=1000, y_mesh=1000):
    """
    補間したデータを作成
    """
    itp = Interpolation()
    ff = itp.exec_interpo(x_array, y_array, z_array)
    xx_array, yy_array = ProcessArray.get_xy_grid(x_array, y_array, x_mesh=x_mesh, y_mesh=y_mesh)
    xi = itp.get_xi(xx_array, yy_array)
    zz_array = itp.get_obj_var(ff, xi)
    return xx_array, yy_array, zz_array


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
        n次元線型補間．データは必ず昇順の必要あり．
        z_arrayは,x軸方向はx_array,y軸方向はy_array
        を元に昇順にソートする．
        """
        y_array_sorted = np.sort(y_array)
        x_array_sorted = np.sort(x_array)
        z_array_sorted = z_array[np.argsort(y_array), :][:, np.argsort(x_array)]
        ff = RegularGridInterpolator((y_array_sorted, x_array_sorted), z_array_sorted)
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


class NumericalCalc(object):
    def __init__(self):
        pass

    @staticmethod
    def calc_integrate_2d(x_array, y_array, z_array):
        """
        離散データから2次元の数値積分を行う
        example
        # ∬x^2+x^2dxdy=8/3を計算
        x_array = np.linspace(1, 2, 1000)
        y_array = np.linspace(0, 1, 1000)
        X, Y = np.meshgrid(x_array, y_array)
        Z = X ** 2 + Y ** 2
        calc_int_x = integrate.cumtrapz(Z, x_array, axis=1)
        calc_int_xy = integrate.cumtrapz(calc_int_x, y_array, axis=0)
        print(np.max(calc_int_xy))
        # 2.6666670006676663 = 8/3

        :param x_array: 1d_ndarray
        :param y_array: 1d_ndarray
        :param z_array: 2d_ndarray
        :return: integrated_2d_ndarray
        """
        # x軸方向(axis=1)に数値積分
        calc_int_x = integrate.cumtrapz(z_array, x_array, axis=1)
        # y軸方向(axis=0)に数値積分
        calc_int_xy = integrate.cumtrapz(calc_int_x, y_array, axis=0)
        return calc_int_xy
