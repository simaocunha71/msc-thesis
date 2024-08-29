
def heap_queue_largest(lst: list, n: int) -> list:
    import heapq
    return heapq.nlargest(n, lst)

print(heap_queue_largest([25, 35, 22, 85, 14, 65, 75, 22, 58], 3))

# Alternatively, you can use the sorted function with a slice:

def heap_queue_largest(lst: list, n: int) -> list:
    return sorted(lst, reverse=True)[:n]

print(heap_queue_largest([25, 35, 22, 85, 14, 65, 75, 22, 58], 3))

"""
Output:
[85, 75, 65]
[85, 75, 65]
"""
<jupyter_output>
<empty_output>
<jupyter_text>
6. Write a Python program to check if a given string is a Palindrome or not using a stack.
<jupyter_code>
"""
