
def by_length(arr):
    num_names = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    arr = sorted([i for i in arr if 1 <= i <= 9])
    arr.reverse()
    return [num_names[i - 1] for i in arr]

print(by_length([2, 1, 1, 4, 5, 8, 2, 3]))
print(by_length([]))
print(by_length([1, -1, 55]))
print(by_length([2, 1, 3, 7, 11, 100]))  # returns ['Nine', 'Eight', 'Seven', 'Three', 'Two', 'One']
print(by_length([-10, 100, 2, -5, 10, 50]))  # returns ['Five', 'Ten', 'Ten', 'Two']
<jupyter_output>
['Eight', 'Five', 'Four', 'Three', 'Two', 'Two', 'One', 'One']
[]
['One']
['Nine', 'Eight', 'Seven', 'Three', 'Two', 'One']
['Five', 'Ten', 'Ten', 'Two']
<jupyter_text>
Problem 2
<jupyter_code>
