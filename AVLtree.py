class AVL:

    class Node:

        def __init__(self, val=None, left=None, right=None, diff=0):
            self.v = val
            self.size = 1
            self.diff = 0
            self.left = None
            self.right = None
            if left is not None:
                self.left = left
                self.size = left.size+1
                self.diff = left.size
            if right is not None:
                self.right = right
                self.size = max(self.size, right.size+1)
                self.diff -= right.size

        def __str__(self):
            return (f'(val = {self.v}, ' +
                    f'size = {self.size}, ' +
                    f'diff = {self.diff}, ' +
                    f'l = {self.left is None} ' +
                    f'r = {self.right is None}')

    def __init__(self, x=None, node=None):
        if node is not None:
            self.root = node
        elif x is not None:
            self.root = self.Node(x)
        else:
            self.root = self.Node()

    def _slr(self, node):
        b = node.right
        node.right = b.left
        b.left = node

        self._update(node)
        self._update(b)
        return b

    def _blr(self, node):
        c = self._srr(node.right)
        node.right = c
        c = self._slr(node)
        return c

    def _srr(self, node):
        b = node.left
        node.left = b.right
        b.right = node

        self._update(node)
        self._update(b)
        return b

    def _brr(self, node):
        c = self._slr(node.left)
        node.left = c
        c = self._srr(node)
        return c

    def balance(self, node):
        if abs(node.diff) > 1:
            if node.diff == -2 and node.right.diff in [-1, 0]:
                return self._slr(node)
            if node.diff == -2 and node.right.diff == 1:
                return self._blr(node)
            if node.diff == 2 and node.left.diff in [1, 0]:
                return self._srr(node)
            if node.diff == 2 and node.left.diff == -1:
                return self._brr(node)
        else:
            return node

    def _inorder_trav(self, node):
        if node.left:
            yield from self._inorder_trav(node.left)
        yield node
        if node.right:
            yield from self._inorder_trav(node.right)

    def __iter__(self):
        if self.root:
            return self._inorder_trav(self.root)

    def _update(self, node):
        l_size = 0 if node.left is None else node.left.size
        r_size = 0 if node.right is None else node.right.size
        node.size = max(l_size, r_size) + 1
        node.diff = l_size - r_size

    def _add(self, x, node=None):
        if node is None or node.v is None:
            node = self.Node(x)
        elif node.v < x:
            right = self._add(x, node.right)
            node.right = right
            self._update(node)
        elif node.v > x:
            left = self._add(x, node.left)
            node.left = left
            self._update(node)
        node = self.balance(node)

        return node

    def add(self, x):
        self.root = self._add(x, self.root)

    def string(self, node):
        if node is None:
            return ''
        s = f'({self.string(node.left)}) {node.v} ({self.string(node.right)})'
        return s

    def __str__(self):
        return self.string(self.root)

    def _find(self, x, node):
        if node is None:
            return None
        if node.v == x:
            return node
        elif node.v < x:
            return self._find(x, node.right)
        else:
            return self._find(x, node.left)

    def __contains__(self, x):
        return self._find(x, self.root) is not None

    def __getitem__(self, x):
        return self._find(x, self.root)

    def _len(self, node):
        if node is None:
            return 0
        return 1 + self._len(node.left) + self._len(node.right)

    def __len__(self):
        return self._len(self.root)
