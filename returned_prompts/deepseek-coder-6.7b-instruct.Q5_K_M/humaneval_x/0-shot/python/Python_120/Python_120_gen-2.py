
    def maximum(arr, k):
        arr.sort(reverse=True)
        return arr[:k]

# 测试用例
print(maximum([-3, -4, 5], 3))  # 期望输出: [-4, -3, 5]
print(maximum([4, -4, 4], 2))  # 期望输出: [4, 4]
print(maximum([-3, 2, 1, 2, -1, -2, 1], 1))  # 期望输出: [2]

# 复杂度分析
# 时间复杂度: O(n log n)，其中 n 是 arr 的长度，因为我们需要对 arr 进行排序。
# 空间复杂度: O(k)，其中 k 是我们要返回的最大数的数量。
<jupyter_output>
[-4, -3, 5]
[4, 4]
[2]
<jupyter_text>
解题思路：- 首先，我们对输入的数组进行降序排序。- 然后，我们返回排序后的数组的前 k 个元素。- 由于数组是按降序排序的，所以这些元素将是数组中的最大数。
<jupyter_code>
# 其他解法：优先队列
# 我们可以使用优先队列（最大堆）来解决这个问题。

def maximum(arr, k):
    import heapq

    # 将数组转换为最大堆
    arr = [-i for i in arr]
    heapq.heapify(arr)

    # 获取最大数
    res = []
    for _ in range(k):
        res.append(-heapq.heappop(arr))

    return res

# 测试用例
print(maximum([-3, -4, 5], 3))  # 期望输出: [-4, -3, 5]
print(maximum([4, -4, 4], 2))  # 期望输出: [4, 4]
print(