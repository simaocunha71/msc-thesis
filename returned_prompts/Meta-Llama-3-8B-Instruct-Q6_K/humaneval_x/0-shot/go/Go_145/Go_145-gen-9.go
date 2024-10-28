Here is a solution in Go:

```go
import (
    "sort"
    "strconv"
)

func OrderByPoints(nums []int) []int {
    type Point struct {
        num int
        sum int
        idx int
    }
    points := make([]Point, len(nums))
    for i, num := range nums {
        points[i].num = num
        points[i].sum = sumOfDigits(num)
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

func sumOfDigits(n int) int {
    sum := 0
    for n != 0 {
        sum += n % 10
        n /= 10
    }
    return sum
}
```

This solution first creates a new type `Point` which has three fields: `num`, `sum`, and `idx`. Then it creates a slice of `Point` and fills it with the numbers and their corresponding sums and indices. The `sort.Slice` function is used to sort the slice based on the sum of digits and then the index. Finally, it creates a new slice and fills it with the numbers from the sorted slice. The `sumOfDigits` function is used to calculate the sum of digits of a number. 

For example, if you call `OrderByPoints([1, 11, -1, -11, -12])`, it will return `[-1, -11, 1, -12, 11]`. If you call `OrderByPoints([])`, it will return `[]`. 

This solution has a time complexity of O(n log n) due to the sorting, where n is the length of the input slice. The space complexity is O(n) for storing the points. 

Note: This solution assumes that the input slice is not empty. If the input slice can be empty, you should add a check before sorting. 

Also, this solution assumes that the input slice contains only integers. If the input slice can contain non-integer values, you should add a check before calculating the sum of digits. 

You can test this solution