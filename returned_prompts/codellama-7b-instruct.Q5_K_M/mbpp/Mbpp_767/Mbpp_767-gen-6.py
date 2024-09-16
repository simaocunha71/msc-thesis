
from typing import List
def get_pairs_count(my_list: List, sum: int) -> int:
    count = 0
    for i in range(len(my_list)):
        for j in range(i+1, len(my_list)):
            if my_list[i] + my_list[j] == sum:
                count += 1
    return count
