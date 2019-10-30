class Nodes:

    def __init__(self, n):
        self.left = None
        self.right = None
        self.value = n

    def addNode(self, node):
        if(node.value < self.value):
            if(self.left == None):
                self.left = node
                return self.left
            else:
                return self.left.addNode(node)
        elif(node.value > self.value):
            if(self.right == None):
                self.right = node
                return self.right
            else:
                return self.right.addNode(node)

    def visit(self):
        if(self.left != None):
            self.left.visit()

        print(self.value)

        if(self.right != None):
            self.right.visit()

    def search(self, num):
        print(self.value)
        if(num == self.value):
            return True
        elif(num < self.value and self.left != None):
            return self.left.search(num)
        elif(num > self.value and self.right != None):
            return self.right.search(num)
