
class RecursiveSegmentTree:
    def __init__(self, B):
        def build_rec(i, _l, _r):
            if _l == _r:
                self.A[i] = B[l]
            else:
                _m = (_l + _r) // 2
                build_rec(i*2, _l, _m)
                build_rec(i*2+1, _m+1, _r)
                self.A[i] = self.A[i*2] + self.A[i*2+1]

        self.n = len(B)
        self.A = [0] * (4*self.n)
        build_rec(1, 0, self.n-1)

    def sum(l, r):
        def sum_rec(i, _l, _r, l, r)
            if _l > _r:
                return 0
            if l == _l and r == _r:
                return self.A[i]
            m = (_l+_r)//2
            return sum_rec(i*2, _l, _m, l, min(r, _m)) + sum_rec(i*2+1, _m+1, _r, max(l, _m+1), r)
        return sum_rec(1, 0, self.n-1, l, r)
    

    