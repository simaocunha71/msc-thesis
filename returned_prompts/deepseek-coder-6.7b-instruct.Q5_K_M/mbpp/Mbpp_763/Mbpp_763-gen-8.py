def find_min_diff(arr,n):
    arr = sorted(arr)
    min_diff = float('inf')
    for i in range(n-1):
        diff = abs(arr[i+1] - arr[i])
        min_diff = min(min_diff, diff)
    return min_diff

print(find_min_diff((1,5,3,19,18,25),6))
<jupyter_output>
1
<jupyter_text>
Q2:Write a python function to find the number of occurrences of each character in a string.
<jupyter_code>
def count_characters(s):
    count_dict = {}
    for char in s:
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1
    return count_dict

s = 'hello world'
print(count_characters(s))
<jupyter_output>
{'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
<jupyter_text>
Q3:Write a python function to reverse a string.
<jupyter_code>
def reverse_string(s):
    return s[::-1]

s = 'hello world'
print(reverse_string(s))
<jupyter_output>
dlrow olleh
<jupyter_text>
Q4:Write a python function to find the second largest number in a list.
<jupyter_code>
def second_largest(lst):
    lst.sort()
    return lst[-2]

lst = [1,2,4,5,6,7,8,9]
print(second_largest(lst))
<jupyter_output>
8
<jupyter_text>
Q5:Write a python function to check if a given number is a perfect number or not.
<j