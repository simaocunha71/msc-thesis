
class Solution:
    def get_max_triples(self, n: int) -> int:
        a = [i*i - i + 1 for i in range(1, n+1)]
        return sum(a[i] + a[j] + a[k] for i in range(1, n) for j in range(i+1, n) for k in range(j+1, n) if a[i] + a[j] + a[k] % 3 == 0)
