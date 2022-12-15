
class UnionFind:
    def __init__(self, n):
        self.parent = [node for node in range(n)]
        self.size = [1] * n

    def union(self, A, B):
        root_A = self.find(A)
        root_B = self.find(B)
        if root_A == root_B:
            return False
        if self.size[root_A] < self.size[root_B]:
            self.parent[root_A] = root_B
            self.size[root_B] += self.size[root_A]
        else:
            self.parent[root_B] = root_A
            self.size[root_A] += self.size[root_B]
        return True

    def find(self, A):
        if not (0 <= A <= len(self.parent) - 1):
            raise IndexError('find nonexistant node')
        root = A
        while root != self.parent[root]:
            root = self.parent[root]
        while A != root:
            old_root = self.parent[A]
            self.parent[A] = root
            A = old_root
        return root
