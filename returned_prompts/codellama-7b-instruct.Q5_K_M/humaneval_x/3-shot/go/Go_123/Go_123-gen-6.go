    var result []int

    for n > 1 {
        if n % 2 == 0 {
            n /= 2
        }else{
            n = 3 * n + 1
        }
        result = append(result, n)
    }

    sort.Ints(result)
    return result
}



