from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    min_num = min(numbers)
    max_num = max(numbers)
    diff = max_num - min_num
    return [(num - min_num) / diff for num in numbers]

print(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]))

# This code first calculates the minimum and maximum values of the input list. It then calculates the difference between these values, which will be used to scale the numbers. Finally, it creates a new list by subtracting the minimum value from each number in the input list and dividing by the difference. The result is a list of numbers that have been rescaled to fit between 0 and 1.
<jupyter_output>
[0.0, 0.25, 0.5, 0.75, 1.0]
<jupyter_text>
Question 2
<jupyter_code>
