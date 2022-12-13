
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


# """
# WIHTOUT OTPIMIZATIONS
# """
# class UnionFind:
    
#     # For efficiency, we aren't using makeset, but instead initialising
#     # all the sets at the same time in the constructor.
#     def __init__(self, n):
#         self.parent = [node for node in range(n)]
        
#     # The find method, without any optimizations. It traces up the parent
#     # links until it finds the root node for A, and returns that root.
#     def find(self, A):
#         while A != self.parent[A]:
#             A = self.parent[A]
#         return A
        
#     # The union method, without any optimizations. It returns True if a
#     # merge happened, False if otherwise.
#     def union(self, A, B):
#         # Find the roots for A and B.
#         root_A = self.find(A)
#         root_B = self.find(B)
#         # Check if A and B are already in the same set.
#         if root_A == root_B:
#             return False
#         # Merge the sets containing A and B.
#         self.parent[root_A] = root_B
#         return True
