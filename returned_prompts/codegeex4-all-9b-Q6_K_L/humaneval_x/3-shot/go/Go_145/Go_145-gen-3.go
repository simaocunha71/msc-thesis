    points := make([]int, len(nums))
    for i, n := range nums {
        points[i] = sumDigits(n)
    }

    sort.Slice(nums, func(i, j int) bool {
        return points[i] < points[j]
    })

    return nums
}

func sumDigits(n int) int {
    s := strconv.Itoa(n)
    sum := 0
    for _, c := range s {
        d, _ := strconv.Atoi(string(c))
        sum += d
    }
    return sum
}

