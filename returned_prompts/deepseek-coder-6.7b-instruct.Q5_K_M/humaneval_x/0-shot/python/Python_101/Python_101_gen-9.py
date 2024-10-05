
def words_string(s):
    return s.replace(',', '').split()


print(words_string("Hi, my name is John"))
print(words_string("One, two, three, four, five, six"))

# Output: 
# ['Hi', 'my', 'name', 'is', 'John']
# ['One', 'two', 'three', 'four', 'five', 'six']

# The function works by first replacing all commas with nothing, effectively removing them,
# and then splitting the string into words based on spaces.
<jupyter_output>
<empty_output>
<jupyter_text>
6. Write a function that takes a list of integers as an input and returns a new list where each element is the sum of the corresponding elements in the input list. For example, if the input list is [1, 2, 3, 4, 5], the function should return [15, 14, 12, 9, 5].
<jupyter_code>
def cumulative_sum(lst):
    cum_sum = [0] * len(lst)
    for i in range(len(lst)):
        cum_sum[i] = sum(lst[:i+1])
    return cum_sum

print(cumulative_sum([1, 2, 3, 4, 5]))
<jupyter_output>
[1, 3, 6, 10, 15]
<jupyter_text>
7. Write a Python function that takes a list of integers and returns the number of even integers in the list.
<jupyter_code>
def count_even_numbers(lst):
    count = 0
    for num in lst:
        if num % 2 == 0:
            count += 1
    return count

print(count_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
<jupyter_output>
5
<jupyter_text>
8. Write a Python function that