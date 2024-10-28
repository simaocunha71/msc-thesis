    points := make([]int,0)

    for _, n := range nums{
        points = append(points, getSum(n))
    }

    sort.Slice(nums, func(i, j int) bool {
        if points[i] == points[j] {
            return i < j
        }
        return points[i] < points[j]
    })

    return nums
}

func getSum(n int) int{
    sum := 0
    if n < 0{
        n *= -1
    }
    for n > 0{
        sum += n%10
        n = n / 10
    }
    return sum
}



