# -*- coding:utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import A_Node
import Pre_Order_Solution
import Post_Order_Solution

#程式的起始點


In_Order = ['C','B','E','D','F','N','J','X','A','G','I','H','Y','L','K','M','Z']

Pre_Order = ['A','B','C','D','E','F','J','N','X','G','H','I','K','L','Y','M','Z']


B_tree_Z = A_Node.Node()

B_tree_A = Post_Order_Solution.Post_Solution()
B_tree_Z = B_tree_A.buildTree(Pre_Order, In_Order)

print(B_tree_Z.right.data)
