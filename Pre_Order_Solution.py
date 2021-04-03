# -*- coding:utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding("utf-8")


import A_Node

class Per_Solution(): #中文
    def buildTree(self, preorder, inorder):
        if len(preorder) == 0:
            return None
        root = A_Node.Node(preorder[0])
        #print(root.data)
        index = inorder.index(root.data)
        root.left = self.buildTree(preorder[1 : index + 1], inorder[0 : index])
        root.right = self.buildTree(preorder[index + 1 : ], inorder[index + 1 :])

        #print(root.data)
        return root
