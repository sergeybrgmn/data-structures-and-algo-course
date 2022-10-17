"""BST Example to insert elements"""


from re import L


class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        current = self.root
        inserted = False
        while not inserted:
            if current.value < new_val:
                if not current.right:
                    current.right = Node(new_val)
                    inserted = True
                else:
                    current = current.right
            elif current.value > new_val:
                if not current.left:
                    current.left = Node(new_val)
                else:
                    current = current.left          
            else:
                inserted = True
        return inserted

        

    def search(self, find_val):
        current = self.root
        found = -1
        while found < 0:
            if current.value == find_val:
                found = 1
            elif current.value < find_val:
                if current.right:
                    current = current.right
                else:
                    found = 0
            else:
                if current.left:
                    current = current.left
                else:
                    found = 0         

        if found > 0:
            return True
        else:
            return False
    
# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)


# Check search
# Should be True
print(tree.search(4))
# Should be False
print(tree.search(6))