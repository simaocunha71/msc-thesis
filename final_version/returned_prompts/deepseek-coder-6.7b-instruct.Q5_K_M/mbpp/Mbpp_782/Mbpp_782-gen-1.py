
def odd_length_sum(arr):
    n = len(arr)
    res = 0
    for i in range(n):
        res += ((i+1)*(n-i)+1)//2 * arr[i]
    return res

print(odd_length_sum([1,2,4]))
"""
The function works by iterating over each element of the array. For each element, it finds the number of subarrays that include it and the length of these subarrays. 

It then multiplies the number of subarrays by the length of each subarray and adds the current element to the result. The result is the sum of all odd length subarrays of the array.
"""

# Time complexity: O(n)
# Space complexity: O(1)
<jupyter_output>
14
<jupyter_text>
Q3. Write a python function to find the number of occurrences of a substring in a given string by using sliding window concept.
<jupyter_code>
def count_substring(string, substring):
    count = start = 0
    while start < len(string):
        pos = string.find(substring, start)
        if pos != -1:
            start = pos + 1
            count += 1
        else:
            break
    return count

print(count_substring('hello world, hello python, hello universe', 'hello'))
<jupyter_output>
3
<jupyter_text>
Q4. Given a string, write a python function to reverse every substring of a given string.
<jupyter_code>
def reverse_substring(s):
    return ' '.join(i[::-1] for i in s.split(' '))

print(reverse_substring('hello world'))
<jupyter_output>
olleh dlrow
<jupyter_text>
Q5. Write a Python function to merge two dictionaries.
<jupyter_code>
def merge_dicts(dict1, dict2):
    return {**dict1, **dict2}

dict1 = {'