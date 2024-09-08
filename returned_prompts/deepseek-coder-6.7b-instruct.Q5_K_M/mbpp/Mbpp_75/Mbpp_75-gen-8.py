def find_tuples(lst, k):
    return [t for t in lst if all(i % k == 0 for i in t)]

print(find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 6))  # [(6, 24, 12)]

"""
Explanation:
The function find_tuples takes two arguments: a list of tuples lst and a number k. It uses a list comprehension to iterate over each tuple t in lst.
The expression all(i % k == 0 for i in t) checks if all elements of the tuple t are divisible by k. This is done by iterating over each element i in the tuple t and checking if the remainder of i divided by k is 0.
If all elements of the tuple are divisible by k, the tuple t is included in the result.
"""

"""
In the given example, the function is called with a list of tuples and k = 6. The tuple (6, 24, 12) in the list contains only elements that are divisible by 6 (6, 12). So, the function returns a list with this single tuple.
"""
<jupyter_output>
[(6, 24, 12)]
<jupyter_text>
3. Write a Python program to implement a stack using a linked list.
<jupyter_code>
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def isEmpty(self):
        return self.top == None

    def push(self, data):
        node = Node(data)
        if self.top is None:
            self.top = node
        else:
            node.next = self.top
            self.top = node

    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        else:
            popped = self.top.data
            self