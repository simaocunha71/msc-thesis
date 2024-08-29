def sum_list(a,b):
    return [x+y for x,y in zip(a,b)]

print(sum_list([10,20,30],[15,25,35])) #==[25,45,65]
<jupyter_output>
[25, 45, 65]
<jupyter_text>
Q2: Write a function to find the maximum and minimum number in a list. Return these as a list.For example:max_min_list([10,20,30,40,50])==[50,10]
<jupyter_code>
def max_min_list(numbers):
    return [max(numbers), min(numbers)]

print(max_min_list([10,20,30,40,50])) #==[50,10]
<jupyter_output>
[50, 10]
<jupyter_text>
Q3: Write a function that takes a list and returns a new list with unique elements of the first list.
<jupyter_code>
def unique_list(lst):
    return list(set(lst))

print(unique_list([1,2,2,3,3,4,4,5,5])) #==[1,2,3,4,5]
<jupyter_output>
[1, 2, 3, 4, 5]
<jupyter_text>
Q4: Write a function that takes a list of numbers and returns the average of these numbers.
<jupyter_code>
def average_list(numbers):
    return sum(numbers) / len(numbers)

print(average_list([10,20,30,40,50])) #==30
<jupyter_output>
30.0
<jupyter_text>
Q5: Write a function that takes a string and returns a list with all characters of the string.
<jupyter_code>
def string_