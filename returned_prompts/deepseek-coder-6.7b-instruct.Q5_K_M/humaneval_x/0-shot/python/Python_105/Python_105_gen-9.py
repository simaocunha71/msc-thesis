
def by_length(arr):
    num_names = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    arr = [i for i in arr if 1 <= i <= 9]
    arr.sort(reverse=True)
    return [num_names[i] for i in arr]

print(by_length([2, 1, 1, 4, 5, 8, 2, 3]))
print(by_length([]))
print(by_length([1, -1, 55]))
print(by_length([2, 7, 11, 0, 1, 10]))
print(by_length([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
<jupyter_output>
['Eight', 'Five', 'Four', 'Three', 'Two', 'Two', 'One', 'One']
[]
['One']
['Seven', 'Two', 'One', 'One', 'Zero']
['Nine', 'Eight', 'Seven', 'Six', 'Five', 'Four', 'Three', 'Two', 'One', 'Zero']
<jupyter_text>
Problem 2
<jupyter_code>
