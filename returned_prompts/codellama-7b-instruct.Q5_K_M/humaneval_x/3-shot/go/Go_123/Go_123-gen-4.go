    result := make([]int, 0)

    for {
        if n == 1 {
            break
        }

        if n % 2 == 0 {
            n = n / 2
        } else {
            n = 3 * n + 1
        }

        result = append(result, n)
    }

    sort.Ints(result)
    return result
}



