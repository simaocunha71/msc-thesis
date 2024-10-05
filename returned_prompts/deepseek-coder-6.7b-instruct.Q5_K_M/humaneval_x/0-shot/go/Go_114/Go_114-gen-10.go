    // Write your code here
}

// ANSWER:
func Minsubarraysum(nums []int) int {
    sum := 0
    min := math.MaxInt64
    for _, num := range nums {
        sum += num
        if sum < min {
            min = sum
        }
        sum = min
    }
    return min
}
```

### 3.2 动态规划解法：
```go
