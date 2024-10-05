    min_sum := math.MaxInt64
    cur_sum := 0
    for _, num := range nums {
        cur_sum += num
        if cur_sum < min_sum {
            min_sum = cur_sum
        }
        cur_sum = min(cur_sum, 0)
    }
    return min_sum
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}
```

这个问题可以通过使用滑动窗口的思想来解决。我们用两个指针来表示滑动窗口的起始和结束位置。我们用一个变量来记录当前的最小和，以及全局的最小和。

当当前的和小于0时，我们需要将窗口向右滑动，所以我们将结束指针向右移动，并将结束位置的元素加到当前的和上。当当前的和大于等于0时，我们尝试将窗口向右滑动，所以我们将起始指针向右移动，并从当前的和中减去起始位置的元素。

在每次移动窗口后，我们都会更新全局的最小和。

这种方法的时间复杂度是O(n)，其中n是数组的长度，空间复杂度是O(1)，因为我们只使用了常数的空间。

这个问题是LeetCode上的一道困难题，题目链接是https://leetcode.com/problems/minimum-size-subarray-sum/。

这个问题可以通过动态规划来解决，但由于这个问题没有要求我们找出具体的子数组，所以动态规划并不是最优的解法。
*/

func Minsubarraysum(nums []int) int {
	min_sum := math.MaxInt64
	cur_sum := 0
	for _, num := range nums {
		cur_sum += num
		if cur_sum < min_sum {
			min_sum = cur_sum
		}
		cur_sum = min(cur_sum, 0)
	}
	return min_sum
}

func