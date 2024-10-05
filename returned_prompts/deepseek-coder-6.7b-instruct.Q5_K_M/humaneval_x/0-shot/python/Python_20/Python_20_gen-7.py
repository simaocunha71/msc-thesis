def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    numbers.sort()
    min_diff = float('inf')
    result = ()
    for i in range(1, len(numbers)):
        diff = numbers[i] - numbers[i - 1]
        if diff < min_diff:
            min_diff = diff
            result = (numbers[i - 1], numbers[i])
    return result


print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))

#OUTPUT:
#(2.0, 2.2)
#(2.0, 2.0)

#This program works by sorting the list of numbers first. Then it iterates over the sorted list, calculating the difference
#between each consecutive pair of numbers. If the difference is smaller than the current minimum difference, the program
#updates the minimum difference and remembers the pair of numbers. Finally, the program returns the pair of numbers with
#the smallest difference.

#The time complexity of this program is O(n log n) because of the sorting step, where n is the length of the input list.
#The space complexity is O(1) because the program uses a constant amount of extra space.
<jupyter_output>
(2.0, 2.2)
(2.0, 2.0)
<jupyter_text>
Question 2
<jupyter_code>
