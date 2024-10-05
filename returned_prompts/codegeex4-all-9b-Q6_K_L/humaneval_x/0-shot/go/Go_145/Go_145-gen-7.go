```go
func OrderByPoints(nums []int) []int {
    var points = make([][2]interface{}, len(nums))
    for i, num := range nums {
        points[i] = [2]interface{}{num, digitsSum(num)}
    }
    sort.Slice(points, func(i, j int) bool {
        if points[i][1] == points[j][1] {
            return i < j
        }
        return points[i][1].(int) < points[j][1].(int)
    })
    result := make([]int, len(nums))
    for i, point := range points {
        result[i] = point[0].(int)
    }
    return result
}

func digitsSum(num int) int {
    if num == 0 {
        return 0
    }
    if num < 0 {
        return digitsSum(-num)
    }
    return num % 10 + digitsSum(num / 10)
}
```