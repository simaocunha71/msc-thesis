"""
Write a function to sort the given list.
assert heap_sort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])==[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
"""

def heap_sort(nums):
    if len(nums) <= 0:
        return [None]*len(nums)
    
    def left_rotate(heap_nums):
        size = len(heap_nums)
        
        for i in range(1, size-1, -1):
            heap_nums[i] = heap_nums[size]
            heap_nums[size] = nums[0]
            
            if i > 1:
                nums.pop()
                
        return heap_nums
    
    heap = [None]*len(nums)
    for x in range(0, len(nums)):
        heap = left_rotate(heap)
        
        if heap[x] != None:
            nums.append(heap[x])
            
    return nums