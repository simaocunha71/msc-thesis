    type Point struct {
        num int
        sum int
        idx int
    }

    points := make([]Point, len(nums))
    for i, num := range nums {
        points[i].num = num
        points[i].sum = sumDigits(num)
        points[i].idx = i
    }

    sort.Slice(points, func(i, j int) bool {
        if points[i].sum != points[j].sum {
            return points[i].sum < points[j].sum
        }
        return points[i].idx < points[j].idx
    })

    result := make([]int, len(points))
    for i, p := range points {
        result[i] = p.num
    }
    return result
}

func sumDigits(n int) int {
    sum := 0
    for n > 0 {
        sum += n % 10
        n /= 10
    }
    return sum
}