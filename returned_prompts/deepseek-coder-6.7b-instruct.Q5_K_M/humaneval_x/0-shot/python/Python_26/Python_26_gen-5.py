from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    return [numbers[i] for i in range(len(numbers)) if numbers[i