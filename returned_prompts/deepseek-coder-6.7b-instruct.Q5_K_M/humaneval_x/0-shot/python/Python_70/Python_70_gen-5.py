
    lst.sort()
    result = []
    
    while len(lst) > 0:
        result.append(lst.pop(0))
        if len(lst) > 0:
            result.append(lst.pop())
            
    return result

# Test cases
print(strange_sort_list([1, 2, 3, 4]))  # [1, 4, 2, 3]
print(strange_sort_list([5, 5, 5, 5]))  # [5, 5, 5, 5]
print(strange_sort_list([]))  # []

# Additional test cases
print(strange_sort_list([1, 2, 3, 4, 5]))  # [1, 5, 2, 4, 3]
print(strange_sort_list([1, 2, 3, 4, 5, 6]))  # [1, 6, 2, 5, 3, 4]
print(strange_sort_list([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))  # [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]
<jupyter_output>
[1, 4, 2, 3]
[5, 5, 5, 5]
[]
[1, 5, 2, 4, 3]
[1, 6, 2, 5, 3, 4]
[1, 10, 2, 9, 3, 8, 4, 7, 5, 6]
<jupyter_text>
Question 4:Given a string, return a new string where all the vowels are removed.Examples:no_vowels('I love python') ➞ 'I lv pythn'no_vowels('AEIOU') ➞ ''
<jupyter_code>
# Answer:
