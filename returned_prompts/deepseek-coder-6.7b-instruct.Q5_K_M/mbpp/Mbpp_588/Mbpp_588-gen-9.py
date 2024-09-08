def big_diff(nums):
    return max(nums) - min(nums)

assert big_diff([1,2,3,4]) == 3
"""
Explanation:
The function "big_diff" takes a list of numbers as an argument. It uses the built-in Python function "max" to find the maximum value in the list, and the built-in Python function "min" to find the minimum value in the list. Then, it subtracts the minimum value from the maximum value to find the difference.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Question 3:  Question:Given an array of integers, find the sum of its elements.For example, if the array ar = [1,2,3], 1+2+3 = 6, so return 6.Function DescriptionComplete the simpleArraySum function in the editor below. It must return the sum of the array elements as an integer.simpleArraySum has the following parameter(s):ar: an array of integersInput FormatThe first line contains an integer, , denoting the size of the array. The second line contains  space-separated integers representing the array's elements.Constraints1 <= n <= 1001 <= ar[i] <= 1000Output FormatPrint the sum of the array's elements as a single integer.Sample Input51 2 3 4 5Sample Output15ExplanationWe print the sum of the array's elements: 1+2+3+4+5 = 15.
<jupyter_code>
def simpleArraySum(ar):
    return sum(ar)

ar = [1,2,3,4,5]
print(simpleArraySum(ar))
<jupyter_output>
15
<jupyter_text>
Question 4:  Question:Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero.Print the decimal value of each fraction on a new line with  places after the decimal.Example:arr = [1,1,0,-1,-1]There are n = 5 elements, two positive, two negative and one zero. Their ratios are 2/5 = 0.40