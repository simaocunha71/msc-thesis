from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    min_num = min(numbers)
    max_num = max(numbers)
    range_num = max_num - min_num
    return [(num - min_num) / range_num for num in numbers]

print(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]))

In this solution, we first find the minimum and maximum numbers in the list. Then we calculate the range of the numbers (maximum - minimum). Finally, we apply the linear transformation to each number in the list. This transformation is done by subtracting the minimum from the number and then dividing by the range. This results in each number being rescaled so that the minimum becomes 0 and the maximum becomes 1.

The time complexity of this function is O(n), where n is the length of the input list. This is because we are iterating over the list once to find the minimum and maximum, and then again to apply the transformation.

The space complexity is also O(n), as we are creating a new list that is the same size as the input list.
