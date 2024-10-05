    result := make([]int, 0)
    if n == 1 {
        return result
    }

    for n != 1 {
        if n % 2 == 0 {
            n = n / 2
        } else {
            n = 3*n + 1
        }
    }

    for n != 1 {
        if n % 2 != 0 {
            result = append(result, n)
        }
        if n % 2 == 0 {
            n = n / 2
        } else {
            n = 3*n + 1
        }
    }
    sort.Ints(result)
    return result
}
