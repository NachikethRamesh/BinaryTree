import Node


class Trees:

    def __init__(self):
        self.root = None

    def addValue(self, n):
        # Every element of the tree is a node object
        node = Node.Nodes(n)
        if(self.root == None):
            self.root = node
            return self.root
        else:
            return self.root.addNode(node)

    # All the node functions are tree functions because tree elements are nodes.
    def traverse(self):
        self.root.visit()

    def find(self, num):
        found = self.root.search(num)

        if(found):
            print("Found " + str(num))
        else:
            print("Not found")
