class FenwickTree:
    """
    Árvore de Fenwick (Binary Indexed Tree)
    """
    def __init__(self, size):
        self.tree = [0] * (size + 1)

    def update(self, index, delta):
        index += 1
        while index < len(self.tree):
            self.tree[index] += delta
            index += index & (-index)

    def query(self, index):
        index += 1
        s = 0
        while index > 0:
            s += self.tree[index]
            index -= index & (-index)
        return s

class Solution:
    def goodTriplets(self, nums1: list[int], nums2: list[int]) -> int:
        n = len(nums1)
        
        pos2 = {val: i for i, val in enumerate(nums2)}
        
        A = [pos2[val] for val in nums1]

        menores_a_esquerda = [0] * n
        bit1 = FenwickTree(n)
        for j in range(n):
            val = A[j]
            # query(val - 1) = soma cumulativa até o índice val-1
            menores_a_esquerda[j] = bit1.query(val - 1)
            bit1.update(val, 1)

        maiores_a_direita = [0] * n
        bit2 = FenwickTree(n)
        for j in range(n - 1, -1, -1):
            val = A[j]
            # bit2.query(n - 1) é o total de elementos adicionados
            maiores_a_direita[j] = bit2.query(n - 1) - bit2.query(val)
            bit2.update(val, 1)

        total_trios = 0
        for j in range(n):
            total_trios += menores_a_esquerda[j] * maiores_a_direita[j]
            
        return total_trios