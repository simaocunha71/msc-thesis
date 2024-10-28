    type point struct {
        num int
        sum int
        idx int
    }

    points := make([]point, len(nums))
    for i, num := range nums {
        points[i].num = num
        points[i].sum = sumDigits(num)
        points[i].idx = i
    }

    sort.Slice(points, func(i, j int) bool {
        if points[i].sum < points[j].sum {
            return true
        } else if points[i].sum == points[j].sum {
            return points[i].idx < points[j].idx
        }
        return false
    })

    result := make([]int, len(nums))
    for i, point := range points {
        result[i] = point.num
    }
    return result
}

func sumDigits(n int) int {
    sum := 0
    for ; n > 0; n /= 10 {
        sum += n % 10
    }
    return sum
}
}