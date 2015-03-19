#########################################
#Compare whether two trees are the same.#
#########################################
class Tree:
    """A tree with entry as its root value."""
    def __init__(self, entry, branches=()):
        self.entry = entry
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = list(branches)

    def __repr__(self):
        if self.branches:
            branches_str = ', ' + repr(self.branches)
        else:
            branches_str = ''
        return 'Tree({0}{1})'.format(self.entry, branches_str)
class BinaryTree(Tree):
    """A tree with exactly two branches, which may be empty."""
    empty = Tree(None)
    empty.is_empty = True

    def __init__(self, entry, left=empty, right=empty):
        for branch in (left, right):
            assert isinstance(branch, BinaryTree) or branch.is_empty
        Tree.__init__(self, entry, (left, right))
        self.is_empty = False

    @property
    def left(self):
        return self.branches[0]

    @property
    def right(self):
        return self.branches[1]

    def __repr__(self):
        if self.left.is_empty and self.right.is_empty:
            return 'Bin({0})'.format(self.entry)
        else:
            left = 'Bin.empty' if self.left.is_empty else repr(self.left)
            right = 'Bin.empty' if self.right.is_empty else repr(self.right)
            return 'Bin({0}, {1}, {2})'.format(self.entry, left, right)
def is_leaf(t):
	if t.left is BinaryTree.empty and t.right is BinaryTree.empty:
		return True
	return False
def btree_check_eq(t1, t2):
	if is_leaf(t1) and is_leaf(t2):
		if t1.entry == t2.entry:
			return True
		return False
	if t1.entry != t2.entry:
		return False
	return btree_check_eq(t1.left,t2.left) and btree_check_eq(t1.right, t2.right)
#          1
#      2          4
#  3
#min(1+1,2) -> 2
#min(1+1, 1+0)
#Order n
def min_depth(t):
    if t is empty:
        return 0
    if is_leaf(t):
        return 1
    return min(1+min_depth(t.left), 1+min_depth(t.right))


# Test cases: 
t = BinaryTree(1, BinaryTree(2, BinaryTree(3)), BinaryTree(4))
t1 = BinaryTree(1, BinaryTree(2, BinaryTree(3), BinaryTree(4)), BinaryTree(5))
t2 = BinaryTree(1, BinaryTree(2, BinaryTree(3), BinaryTree(5)), BinaryTree(5, BinaryTree(6)))
print(btree_check_eq(t1,t2))