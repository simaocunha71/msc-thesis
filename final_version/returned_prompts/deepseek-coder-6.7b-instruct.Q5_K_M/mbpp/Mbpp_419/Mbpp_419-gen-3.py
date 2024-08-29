def round_and_sum(lst):
    rounded_lst = [round(i) for i in lst]
    return sum(rounded_lst) * len(lst)

print(round_and_sum([22.4, 4.0, -16.22, -9.10, 11.00, -12.22, 14.20, -5.20, 17.50]))

#Output: 243

Explanation:
The function 'round_and_sum' takes a list of numbers as input. It applies the built-in 'round' function to each number in the list, producing a new list 'rounded_lst'. Then it calculates the sum of 'rounded_lst' and multiplies it by the length of the original list.
<jupyter_output>
<empty_output>
<jupyter_text>
Question 2:Write a function that takes in a string and returns a dictionary where the keys are the words in the string and the values are the number of times each word appears.
<jupyter_code>
