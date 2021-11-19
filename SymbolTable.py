"""
Symbol Table represented as a BST()

>>> s = ST()       # empty symbol table
>>> s.set('x', 5)
>>> s.set('y', 3)
>>> s.set('z', s.get('x'))
>>> assert s.get('z') == s.get('x')
>>> assert not s.get('z') == s.get('y')
>>> print(s)
('x', 5)[('y', 3)[('z', 5)]]

BST test cases

>>> t = BST()
>>> assert t.empty()
>>> t.insert("JD")

>>> assert not t.empty()
>>> assert t.lookup("JD")
>>> t.insert("Dave")
>>> t.insert("Steven")

>>> assert t.size() == 3

>>> assert t.lookup("JD")
>>> assert t.lookup("Dave")
>>> assert t.lookup("Steven")
>>> assert not t.lookup("jd")
>>> assert not t.lookup("Sorelle")

>>> t.insert("Sorelle")
>>> assert t.lookup("Sorelle")

>>> assert not t.lookup("Kris")

"""
# copy the codes from classnotes.
class node:
    def __init__(self, ltree, v, rtree):
        self.value = v
        self.ltree = ltree
        self.rtree = rtree
        
    def __repr__(self):
        return str(self.value)


class BT:
    # constructor: a BT is either empty, or
    #       a top node (root) connected to two (sub)BTs
    #   primitive: BT()
    #   extending: BT(l, t, r)
    def __init__(self, left=None, top=None, right=None):
        if top == None:         # primitive
            self.rep = None
        else:                   # extending
            self.rep = node(left, top, right)

    # axioms:
    #   empty(BT()) === True
    #   empty(BT(l, t, r)) === False
    def empty(self):
        return self.rep == None

    # axioms:
    #   root(BT()) === undefined
    #   root(BT(l, t, r)) === t
    def root(self):
        assert(not self.empty())
        return self.rep.value

    # axioms:
    #   left(BT()) === undefined
    #   left(BT(l, t, r)) === l
    def left(self):
        assert(not self.empty())
        return self.rep.ltree
    
    # axioms:
    #   right(BT()) === undefined
    #   right(BT(l, t, r)) === r
    def right(self):
        assert(not self.empty())
        return self.rep.rtree

    # print with inorder traversal
    def __repr__(self):
        a = ""
        if not self.empty():
            if not self.left().empty():
                a += "["+str(self.left())+"]"
            a += str(self.rep)
            if not self.right().empty():
                a += "["+str(self.right())+"]"
        return a
    
    # size function for binary trees;
    # should work on any representation
    # of a binary tree
    def size(self):
        if self.empty():
            return 0
        else:
            return self.left().size() + self.right().size() + 1

    # preorder traversal
    def preorder(self, f):
        if not self.empty():
            f(self.root())
            self.left().preorder(f)
            self.right().preorder(f)
            
    # inorder traversal
    def inorder(self, f):
        if not self.empty():
            self.left().inorder(f)
            f(self.root())
            self.right().inorder(f)
            
    # postorder traversal
    def postorder(self, f):
        if not self.empty():
            self.left().postorder(f)
            self.right().postorder(f)
            f(self.root())


#from BinTreeLinked import *	# file name must match (minus .py)

# BST inherits from BT, you get for free:
#   - constructors
#   - accessors:
#       - empty(), root(), left() & right()
#   - display traversals:
#       - pre, in, and postorder
class BST(BT):
    # insert mutator using a overwrite protocol for duplicates
    def insert(self, x):
        if self.empty():
            self.rep = node(BST(),x, BST())
        elif x == self.root():         # replace protocol
            self.rep.value = x
        elif x < self.root():           # insert to the left
            self.left().insert(x)
        else:
            self.right().insert(x)

    # accessor lookup axioms:
    #   lookup(BST(), key) === False
    #   lookup(BST(top, left, right))
    #    === (top == key) or lookup(left, key) or lookup(right,key)
    def lookup(self, key):
        if type(key) == int or type(key) == float:
            return False
        if self.empty():
            return False
        
        if type(self.root()) == tuple:
            if self.root()[0] == key:
                return True
            elif self.root()[0] > key:
                return self.left().lookup(key)
            else:
                return self.right().lookup(key)
        else:
            if self.root() == key:
                return True
            elif self.root() > key:
                return self.left().lookup(key)
            else:
                return self.right().lookup(key)
        

'''
# the python dict type ST
class ST:                   # symbol table
    def __init__(self):             # construct an empty ST
        self.rep = {}
    def set(self, where, what):     # setter (mutator)
        self.rep[where] = what

    def get(self, where):           # getter (accessor)
        return self.rep[where]

    def __str__(self):              # abstract to text
        return str(self.rep)
'''

class ST:
    def __init__(self):
        self.rep = BST()
    
    def set(self, where, what):
        self.rep.insert((where, what))

    def get(self, where):
        if where == self.rep.root()[0]:
            return self.rep.root()[1]
        elif where < self.rep.root()[0]:
            s = ST()
            s.rep = self.rep.left()
            return s.get(where)
        else:
            s = ST()
            s.rep = self.rep.right()
            return s.get(where)
    
    def __str__(self):              # abstract to text
        return str(self.rep)    

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print("doctests completed")
