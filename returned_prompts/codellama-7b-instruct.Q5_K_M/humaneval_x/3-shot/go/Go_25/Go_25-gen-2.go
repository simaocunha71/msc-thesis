    result := make([]int, 0)
    i := 2
    for n > 1 {
        if n % i == 0 {
            result = append(result, i)
            n /= i
        } else {
            i += 1
        }
    }
    return result
}



