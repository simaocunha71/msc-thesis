    var result []int
    for n > 1 {
        if n%2 == 1 {
            result = append(result, n)
            n = n/2
        }else if n%2 == 0 {
            n = 3*n + 1
        }
    }
    sort.Ints(result)
    return result
}



