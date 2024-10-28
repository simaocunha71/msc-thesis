"""
def heap_queue_largest(nums,n):
    max_heap = []
    for num in nums:
        if len(max_heap) > n:
            if num > max_heap[0]:
                max_heap[0] = num
                heapify(max_heap)
        else:
            max_heap.append(num)
            heapify(max_heap)
    return max_heap

def heapify(nums):
    # 获取堆顶元素
    top = nums[0]
    # 弹出堆顶元素
    nums[0] = nums[-1]
    del nums[-1]
    # 对堆进行调整
    i = 0
    while True:
        # 左子结点
        left = i * 2 + 1
        # 右子结点
        right = i * 2 + 2
        # 如果左子结点大于堆顶元素并且左子结点存在
        if left < len(nums) and nums[left] > top:
            # 左子结点大于右子结点并且右子结点存在
            if right < len(nums) and nums[right] > nums[left]:
                nums[i] = nums[left]
                nums[left] = top
                i = left
            # 右子结点大于左子结点并且右子结点存在
            else:
                nums[i] = nums[right]
                nums[right] = top
                i = right
        # 如果右子结点大于堆顶元素并且右子结点存在
        elif right < len(nums) and nums[right] > top:
            nums[i] = nums[right]
            nums[right] = top
            i = right
        # 如果堆顶元素最大，终止调整
        else:
            break
    return nums
"""

def heap_queue_largest(nums,n):
    max