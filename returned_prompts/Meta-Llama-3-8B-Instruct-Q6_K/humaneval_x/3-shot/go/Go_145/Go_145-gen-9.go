    type Point struct {
        num int
        sum int
        idx int
    }
    points := make([]Point, len(nums))
    for i, num := range nums {
        points[i].num = num
        points[i].sum = getSum(num)
        points[i].idx = i
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

func getSum(num int) int {
    sum := 0
    for num > 0 {
        sum += num % 10
        num /= 10
    }
    return sum
}