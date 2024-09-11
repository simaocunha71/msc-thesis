"""
To solve this problem, you can follow these steps:

1. Define a function called heap_sort that takes a list as an argument.
2. In the function, implement the heap sort algorithm to sort the given list. Here's a high-level overview of the algorithm:

- Build a max heap from the input array.
- At each step, swap the root of the max heap (which is the largest element) with the last element of the max heap. Then, reduce the size of the max heap by one and heapify the root.
- Repeat these steps until the entire array is sorted.

3. Implement the necessary helper functions within the heap_sort function to build the max heap and heapify the root. Here's a breakdown of the helper functions:

- max_heapify: This function takes an array, the index of the root, and the length of the heap as arguments. It recursively builds a max heap by comparing and swapping elements until the heap property is satisfied.
- build_max_heap: This function takes an array as an argument and builds a max heap by calling max_heapify on all non-leaf nodes in reverse order.
- heap_sort: This function takes an array as an argument and performs the heap sort algorithm by calling build_max_heap, swapping the root with the last element, and reducing the heap size. It repeats these steps until the entire array is sorted.

4. Finally, call the heap_sort function with the given list and assert that the sorted list matches the expected result.
"""
def heap_sort(arr):
    n = len(arr)
    # Build a max heap from the input array
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(arr, n, i)

    # One by one extract elements from the max heap
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        max_heapify(arr, i, 0)

def max_heapify(arr, n, i):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i
    if left < n and