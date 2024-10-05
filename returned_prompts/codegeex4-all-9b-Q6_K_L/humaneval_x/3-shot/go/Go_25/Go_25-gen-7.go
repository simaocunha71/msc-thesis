    result := make([]int, 0)
    current := 2

    for current <= n{
        if n % current == 0{
            result = append(result, current)
            n = n / current
        }else{
            current += 1
        }
    }

    return result
}



