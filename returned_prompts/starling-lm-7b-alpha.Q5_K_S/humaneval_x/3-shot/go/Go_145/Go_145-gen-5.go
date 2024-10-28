    type point struct {
        value     int
        index     int
        sum_of_digits int
    }

    nums_points := make([]point, len(nums))

    for i, num := range nums {
        nums_points[i] = point{num, i, sumOfDigits(num)}
    }

    sort.Slice(nums_points, func(i, j int) bool {
        return nums_points[i].sum_of_digits < nums_points[j].sum_of_digits
    })

    result := make([]int, len(nums))
    for i := range result {
        result[i] = nums_points[i].value
    }

    return result
}

func sumOfDigits(n int) int {
    s := 0
    for ; n != 0; n /= 10 {
        s += n % 10
    }
    return s
}



