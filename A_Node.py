# -*- coding:utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class Node():
    def __init__(self,data=None):
        self.data = data
        self.left = None
        self.right = None   #中文
