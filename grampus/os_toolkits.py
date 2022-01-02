import os
from datetime import datetime


class OsProc(object):
    def __init__(self):
        pass

    @staticmethod
    def creat_dir(basename, path, is_append_datetime=True, is_return_dirname=True):
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


if __name__ == '__main__':
    pass
