    result := make([]int, 0)

    for _, v := range x {
        if is_odd_digits(v) {
            result = append(result, v)
        }
    }
    sort.Ints(result)
    return result
}

func is_odd_digits(n int) bool {
    digits := make([]int, 0)

    for n > 0 {
        digits = append(digits, n%10)
        n /= 10
    }
    for _, v := range digits {
        if v % 2 == 0 {
            return false
        }
    }
    return true
}



