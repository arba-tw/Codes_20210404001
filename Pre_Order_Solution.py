# -*- coding:utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding("utf-8")


import A_Node

class Pre_Solution(): #中文
    def buildTree(self, postorder, inorder):
        if len(postorder) == 0:
            return None
        root = A_Node.Node(postorder[-1])
        #print(root.data)
        index = inorder.index(root.data)
        #print("point = ",index)
        root.right = self.buildTree(postorder[index : -1], inorder[index + 1 :])
        root.left = self.buildTree(postorder[0 : index ], inorder[0 : index])


        #print(root.data)
        return root
