import random
import Tree

# Tree object
tree = Tree.Trees()

for i in range(4):
    tree.addValue(random.randint(1, 100))

tree.traverse()
print("")
tree.find(23)
