# -*- coding: utf-8 -*-

import os
import filecmp
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

file_list = []


class DuplicateFileFinding:
    def __init__(self):
        pass

    def fetch_files(self, path):  # 遍历主目录下所有文件（包括自目录），并返回至列表
        global file_list
        dir_list = os.listdir(path)
        dir_list_with_full_path = [os.path.join(path, x) for x in dir_list]
        temp_list = dir_list_with_full_path[:]
        for i in temp_list:
            if os.path.isdir(i):
                dir_list_with_full_path.remove(i)
                self.fetch_files(i)
            else:
                file_list.append(i)

    @staticmethod
    def same_image():
        global file_list
        temp_list = file_list[:]
        for i in temp_list:
            index = temp_list.index(i) + 1
            while index < len(temp_list):
                if filecmp.cmp(i, temp_list[index]):
                    # os.remove(i)
                    print(i)
                    print(temp_list[index])
                    print('***********************************')
                    file_list.remove(i)
                    break
                else:
                    index += 1


if __name__ == '__main__':
    test = DuplicateFileFinding()
    test.fetch_files(r'E:' + u'\照片')
    test.same_image()




