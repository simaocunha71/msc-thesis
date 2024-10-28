    type Point struct {
        num  int
        sum  int
        index int
    }

    points := make([]Point, len(nums))
    for i, num := range nums {
        points[i].num = num
        points[i].sum = sumOfDigits(num)
        points[i].index = i
    }

    sort.Slice(points, func(i, j int) bool {
        if points[i].sum != points[j].sum {
            return points[i].sum < points[j].sum
        }
        return points[i].index < points[j].index
    })

    result := make([]int, len(points))
    for i, point := range points {
        result[i] = point.num
    }
    return result
}

func sumOfDigits(n int) int {
    sum := 0
    for n > 0 {
        sum += n % 10
        n /= 10
    }
    return sum
}