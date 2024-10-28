```
def heap_queue_largest(nums,n):
    import heapq
    h = []
    for i in nums:
        heapq.heappush(h,i)
        if len(h)>n:
            heapq.heappop(h)
    return list(heapq.nlargest(n,h))
```

This function uses the `heapq` module in Python, which provides an implementation of a heap queue. A heap queue is a special type of queue that always maintains its elements in a specific order, in this case, in descending order. 

The function starts by initializing an empty heap, `h`. Then, for each number in the given list of `nums`, it uses `heapq.heappush()` to add the number to the heap, ensuring that it is inserted in the correct position to maintain the descending order. 

If the length of the heap becomes greater than `n`, it means that we have already found `n` largest numbers. In this case, the function uses `heapq.heappop()` to remove the smallest number from the heap, as the smallest number will be at the top of the heap due to the heap's properties. 

Finally, the function returns a list of the `n` largest numbers, obtained using `heapq.nlargest(n,h)`. This function returns the `n` largest elements from the heap, in descending order. 

By using the heap queue properties and the provided `heapq` module functions, this solution efficiently finds the `n` largest integers from the given list, while ensuring that the result is returned in descending order.

The provided assert statement verifies that the function correctly finds the three largest numbers from the given list, which are `[85, 75, 65]`.

To use this function, simply call it with the desired list of numbers and the value of `n` as arguments. For example, to find the three largest numbers from the list `[25, 35, 22, 85, 14, 65, 75, 22, 58]`, you can call `heap_queue_largest([25, 35, 22, 