    var result []int
    for n > 1 {
        if n % 2 == 1 {
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