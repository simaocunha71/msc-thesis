
    def add_elements(arr, k):
        sum = 0
        for i in range(0, k):
            if len(str(arr[i])) <= 2:
                sum += arr[i]
        return sum

    print(add_elements([111,21,3,4000,5,6,7,8,9], 4))

Output: 24

Explanation: The function iterates through the first k elements of arr and checks if the number of digits in the current element is less than or equal to 2. If it is, it adds the element to the sum. The sum of the elements with at most two digits from the first k elements of arr is 24.

"""

def add_elements(arr, k):
    sum = 0
    for i in range(0, k):
        if len(str(arr[i])) <= 2:
            sum += arr[i]
    return sum

print(add_elements([111,21,3,4000,5,6,7,8,9], 4))
<jupyter_output>
24
<jupyter_text>
Question 2:
<jupyter_code>
"""
