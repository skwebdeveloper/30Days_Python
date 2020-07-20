class Node:
    def __init__(self,value):
        self.left = None
        self.right = None
        self.info = value
        
class Tree:
    def __init__(self):
        self.root = None
        
        
# ================================================================

# BASIC INORDER, PREORDER AND POSTORDER OPERATIONS  

# ================================================================        
       
# Inorder -- LEFT, ROOT, RIGHT
def Inorder(root):
    if root:
            Inorder(root.left)
            print(root.info, " ", end= " ")
            Inorder(root.right)

# Preorder -- Root, Left, Right
# def Preorder(root):
#     if root:
#             print(root.info, " ", end= " ")
#             Preorder(root.left)
#             Preorder(root.right)
     
# Postorder -- Left, Right, Root
# def Postorder(root):
#     if root:
#             Postorder(root.left)
#             Postorder(root.right)
#             print(root.info, " ", end= " ")

        
# ================================================================
# ================================================================          
    
# BASIC OPERATION VIA STACK 

# Inorder

# def Inorder(root):
#     current = head
#     stack = []
#     while(True):
#         if current is not None:
#             stack.append(current)
#             current = current.left

#         elif(stack):
#             current = stack.pop()
#             print(current.info)
#             current = current.right
#         else:
#             break
#     print()         



# ================================================================

# Level order traversal 

# ================================================================       

# def LOT(root):
#     if root is None:
#         return 
#     que = []
#     que.append(root)
#     while(len(que) > 0):
#         print(que[0].info, " ", end = " ")
#         temp = que.pop(0)
#         if temp.left is not None:
#             que.append(temp.left)
#         if temp.right is not None:
#             que.append(temp.right)    


# ================================================================

# Left and Right View of a Tree

# ================================================================       


# def leftview(root):
#         max_level = [0]
#         leftutil(root, 1, max_level)
        
# def leftutil(root, level, max_level):
#         if root is None:
#             return 
#         if max_level[0] < level:
#             print("%d \t"%(root.info)),
#             max_level[0] = level
#         leftutil(root.left, level+1, max_level)
#         leftutil(root.right, level+1, max_level) 
        
# # Right View  
# def rightutil(root, level, max_level):
#     if root is None:
#         return
#     if max_level[0] < level:
#         print("%d \t"%(root.info))
#         max_level[0] = level 
#     rightutil(root.right, level+1, max_level)
#     rightutil(root.left, level+1, max_level)       
      
# def rightview(root):
#     max_level = [0]
#     rightutil(root, 1, max_level)    
    




  
  
  
  
  
  
  
  
  
  
  
    
    #        0    
    #     /     \
    #    1       2   
    #   / \     / \
    #  3   4   5   6
     
root = Node(1)
root.left = Node(2)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)
root.right.left = Node(4)
root.right.right = Node(3)
print("Inorder")
Inorder(root)
# print(" ")
# print("Preorder")
# Preorder(root)
# print(" ")
# print("Postorder")
# Postorder(root)
# print(" ")
# print("Level order traversal")
# LOT(root)
# print(" ")
# print("Left view of a tree")
# leftview(root)
# print(" ")
# print("Rigth view of a tree")
# rightview(root)
      
      
    
    
        