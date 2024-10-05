    from typing import List
    def by_length(arr: List[int]) -> List[str]:
        number_names = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        return [number_names[i-1] for i in sorted(arr, reverse=True) if 1 <= i <= 9]


