class Node:
	def __init__(self,value=None):
		self.value=value
		self.left=None
		self.right=None     

class BST:
    def __init__(self,first):
        self.root=first
        self.level=1

    def create(self,value):
        cur_node=Node(self.root)
        if int(value) < int(cur_node.value):
            if cur_node.left == None:
                cur_node.left = value
                print(cur_node.left)
                cur_node.left=Node(value)
            else:
                self.create(value)
        if int(value) > int(cur_node.value):
            if cur_node.right == None:
                cur_node.right = value
                print(cur_node.right)
                self.root = cur_node.right 
                cur_node.right=Node(value)
                self.level=self.level+1
            else:
                self.create(value)           

    def height(self):
        return self.level

first = int(input("Enter your first Node/root:"))
head=BST(first)
t_list = (input("Enter your other Nodes/child:").split(" "))
print(t_list)
for i in t_list:
    head.create(i)
    
print("Height of tree: ", head.height())      