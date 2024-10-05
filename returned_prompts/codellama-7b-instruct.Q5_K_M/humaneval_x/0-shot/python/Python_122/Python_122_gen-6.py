
class Solution:
    def add_elements(self, arr: List[int], k: int) -> int:
        return sum(sorted(arr[:k])[:2])

```

