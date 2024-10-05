
def by_length(arr):
    num2words = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine'}
    return [num2words[i] for i in sorted([i for i in arr if 1 <= i <= 9], reverse=True)]

print(by_length([2, 1, 1, 4, 5, 8, 2, 3]))
print(by_length([]))
print(by_length([1, -1, 55]))
print(by_length([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(by_length([9, 8, 7, 6, 5, 4, 3, 2, 1]))
<jupyter_output>
['Eight', 'Five', 'Four', 'Three', 'Two', 'Two', 'One', 'One']
[]
['One']
['Nine', 'Eight', 'Seven', 'Six', 'Five', 'Four', 'Three', 'Two', 'One']
['Nine', 'Eight', 'Seven', 'Six', 'Five', 'Four', 'Three', 'Two', 'One']
<jupyter_text>
Problem 2
<jupyter_code>
