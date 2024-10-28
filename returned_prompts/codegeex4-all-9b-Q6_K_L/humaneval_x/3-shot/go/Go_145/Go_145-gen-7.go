    points := make([]int, len(nums))

    for i, num := range nums {
        points[i] = sumOfDigits(num)
    }

    sort.Slice(nums, func(i, j int) bool {
        return points[i] < points[j] || (points[i] == points[j] && i < j)
    })

    return nums
}

func sumOfDigits(num int) int {
    sum := 0
    if num < 0 {
        num = -num
    }
    for num > 0 {
        sum += num % 10
        num /= 10
    }
    return sum
}



