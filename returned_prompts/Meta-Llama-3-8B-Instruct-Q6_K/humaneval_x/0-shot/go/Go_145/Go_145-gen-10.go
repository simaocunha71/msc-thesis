Here is a Go solution for the problem. It uses a custom sorting function that sorts the slice of integers based on the sum of their digits and their original index.

```go
import (
    "sort"
    "strconv"
)

func OrderByPoints(nums []int) []int {
    type point struct {
        num int
        sum int
        idx int
    }

    points := make([]point, len(nums))
    for i, num := range nums {
        str := strconv.Itoa(abs(num))
        for _, c := range str {
            points[i].sum += int(c - '0')
        }
        points[i].idx = i
    }

    sort.Slice(points, func(i, j int) bool {
        if points[i].sum != points[j].sum {
            return points[i].sum < points[j].sum
        }
        return points[i].idx < points[j].idx
    })

    result := make([]int, len(nums))
    for i, p := range points {
        result[i] = p.num
    }
    return result
}

func abs(x int) int {
    if x < 0 {
        return -x
    }
    return x
}
```

This function first converts each number to a string, calculates the sum of the digits, and stores the result in a slice of `point` structs along with the original index. Then it sorts the slice of `point` structs based on the sum of the digits and the original index. Finally, it constructs the result slice from the sorted slice of `point` structs.

The `abs` function is used to calculate the absolute value of an integer. This is needed because the problem statement doesn't specify how to handle negative numbers. In this solution, negative numbers are handled by treating them as positive numbers when calculating the sum of their digits. This means that `-1` and `1` will be treated as having the same sum of digits, and will be sorted together. If you want to handle negative numbers differently, you can modify the `abs` function accordingly. For example, you could sort negative numbers before positive numbers by returning `points[i].sum > points[j].sum` in the `sort.Slice` function. Alternatively, you could sort negative numbers after positive numbers by returning `points[i].sum < points[j].sum` in the `sort.Slice` function. The choice of how to handle negative numbers depends on the specific requirements of your problem.