
def recursive_list_sum(input_list):
    total_sum = 0
    for element in input_list:
        if type(element) == list:
            total_sum += recursive_list_sum(element)
        else:
            total_sum += element
    return total_sum

print(recursive_list_sum([1, 2, [3,4],[5,6]]))
<jupyter_output>
21
<jupyter_text>
Question 2:Write a Python function to find the maximum and minimum numbers from a sequence of numbers. For instance, if the input is [3, 5, 7, 2, 8, 9, 1], the expected output is 'Max: 9, Min: 1'.
<jupyter_code>
