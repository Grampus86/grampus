import os
import re
from datetime import datetime


class OsProc(object):
    def __init__(self):
        pass

    @staticmethod
    def creat_dir(path, basename, is_append_datetime=True, is_return_dirname=True):
        """
        ディレクトリを作成.pathは絶対パス推奨.
        ファイル名をreturnするときは
        `is_return_dirname=True`
        """
        now = datetime.now()
        if is_append_datetime:
            save_dir_name = '{0}/{1}_{2:%Y%m%d%H%M%S}'.format(path, basename, now)
        else:
            save_dir_name = '{0}/{1}'.format(path, basename)
        os.makedirs(save_dir_name, exist_ok=True)
        if is_return_dirname:
            return save_dir_name
        else:
            return None

    @staticmethod
    def get_file_name(path, pattern='.*.'):
        """
        指定したディレクトリのファイル名を取得
        正規表現使用可能
        ex)
        [aaa.py bbb.py xxx.txt sample_xxx.txt]
        ・ファイル名にpyが含まれる
        pattern='.*py*.'もしくはpattern='py'
        [aaa.py, bbb.py]

        ・ファイル名の先頭がxxx
        pattern='^xxx'
        [xxx.txt]

        ・ファイル名の末尾がtxt
        pattern='txt$'
        [sample_xxx.txt, xxx.txt]

        ・ファイル名の3文字がm
        pattern='^..m'
        [sample_xxx.txt]
        """
        file_dir_list = os.listdir(path)
        only_file_list = [file for file in file_dir_list if os.path.isfile(os.path.join(path, file))]
        file_list = [file for file in only_file_list if re.search(pattern, file)]
        file_name_list_sorted = sorted(file_list, key=lambda x: int((re.search(r"[0-9]+", x)).group(0)))
        return file_name_list_sorted

    @staticmethod
    def get_dir_name(path, pattern='.*.'):
        """
        指定したディレクトリのディレクトリ名を取得
        正規表現使用可能
        """
        file_dir_list = os.listdir(path)
        only_dir_list = [dir for dir in file_dir_list if os.path.isdir(os.path.join(path, dir))]
        dir_list = [dir for dir in only_dir_list if re.search(pattern, dir)]
        dir_name_list_sorted = sorted(dir_list, key=lambda x: int((re.search(r"[0-9]+", x)).group(0)))
        return dir_name_list_sorted


if __name__ == '__main__':
    pass
