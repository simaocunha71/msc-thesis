    var points []int
    var digit_sum []int

    for _, v := range nums {
        points = append(points, v)
        digit_sum = append(digit_sum, sum_digits(v))
    }

    sort.Slice(points, func(i, j int) bool {
        return digit_sum[i] < digit_sum[j]
    })

    return points
}

func sum_digits(n int) int {
    var sum int
    for n > 0 {
        sum += n % 10
        n = n / 10
    }
    return sum
}

// >>> sum_digits(123)
// 6
// >>> sum_digits(0)
// 0
// >>> sum_digits(567)
// 18

