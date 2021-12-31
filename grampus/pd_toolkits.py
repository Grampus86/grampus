import pandas as pd


class Process_data_flame(object):
    """
    pandasのデータフレームを加工
    """

    def __init__(self):
        pass

    @staticmethod
    def create_date_col(df, year_col, month_col, day_col,
                        date_col_name='date', fill_zero_num=2):
        """
        yyyymmddの日付列を作成
        ゼロ埋めの為にはastypeで一度strに変換する必要がある。
        結合後、再度intに戻す。
        ゼロ埋めが必要ない場合は、fill_zero_numを0にすること
        """
        year = df[year_col].astype(str)
        month = df[month_col].astype(str).str.zfill(fill_zero_num)
        day = df[day_col].astype(str).str.zfill(fill_zero_num)
        df[date_col_name] = (year + month + day).astype(int)
        return df

    @staticmethod
    def create_cat_col(df, cat_col_list, cat_col_name, cat_sep='_'):
        """
        複数列を結合して新たな列を作成
        デフォルトでは'_'でつなぐ
        指定したがnanなどで結合できなかった場合はnanとなる
        """
        df[cat_col_name] = df[cat_col_list[0]].astype(str)
        for cat_col in cat_col_list[1:]:
            df[cat_col_name] = df[cat_col_name].str.cat(df[cat_col].astype(str), sep=cat_sep)
        return df

    @staticmethod
    def create_merged_df(df_base, df_link, key_col_1, how='left'):
        """
        マージの仕方は、集合で考える。
        df_baseがleft、df_linkがrightとなる。
        ①df_baseを基準に考えて、df_linkを参照する場合
        つまり、df_linkの中で、df_baseのデータに該当しない物を排除するすればいいので、
        how='left'となる。
        ②積集合ならhow='inner'
        leftとrightでキーにする列以外の列名が重複している場合、
        デフォルトでは_x, _yというサフィックス（接尾辞）がつけられる。
        """
        df_merged = pd.merge(df_base, df_link, on=key_col_1, how=how)
        return df_merged

    @staticmethod
    def get_excel_sheet_name(data_file_name):
        """
        エクセルのシート名の一覧を取得
        """
        df_for_get_sheet_name = pd.read_excel(data_file_name, sheet_name=None)
        sheet_name_list = list(df_for_get_sheet_name.keys())
        return sheet_name_list

    @staticmethod
    def sort_df_by_column(df, col_name, ascending=True):
        """
        dfをある列にしたがってソート
        昇順(1,2,3,...)なら`ascending`を`True`
        降順(5,4,3,...)なら`ascending`を`False`
        :param df: DataFlame
        :param col_name: str
        :param ascending: bool
        :return df_sorted: DataFlame
        """
        df_sorted = df.sort_values(col_name, ascending=ascending)
        return df_sorted

    @staticmethod
    def to_xyz_array(df):
        """
        columnsをx_array
        indexをy_array
        dataをz_arrayに変換
        """
        x_array = df.columns.to_numpy()
        y_array = df.index.to_numpy()
        z_array = df.to_numpy()
        return x_array, y_array, z_array


if __name__ == '__main__':
    pass
