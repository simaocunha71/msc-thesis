Here is a solution to the problem:
```go
import (
    "sort"
    "strconv"
)

func OrderByPoints(nums []int) []int {
    type point struct {
        num  int
        sum  int
        idx  int
    }
    points := make([]point, len(nums))
    for i, num := range nums {
        str := strconv.Itoa(num)
        sum := 0
        for _, ch := range str {
            sum += int(ch - '0')
        }
        points[i] = point{num, sum, i}
    }
    sort.Slice(points, func(i, j int) bool {
        if points[i].sum != points[j].sum {
            return points[i].sum < points[j].sum
        }
        return points[i].idx < points[j].idx
    })
    result := make([]int, len(points))
    for i, point := range points {
        result[i] = point.num
    }
    return result
}
```
This solution defines a custom type `point` to hold the original number, the sum of its digits, and its original index. It then creates a slice of `point`s and populates it with the given numbers. The `sort.Slice` function is used to sort the `point`s based on the sum of their digits, and then by their original index in case of a tie. Finally, the sorted `point`s are converted back to a slice of integers and returned.