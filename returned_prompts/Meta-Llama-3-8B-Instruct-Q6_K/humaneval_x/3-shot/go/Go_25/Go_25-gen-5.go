    result := make([]int, 0)
    i := 2

    for n > 1 {
        count := 0
        for n%i == 0 {
            count += 1
            n /= i
        }
        if count > 0 {
            result = append(result, i)
            for count > 0 {
                count -= 1
                result = append(result, i)
            }
        }
        i += 1
    }
    return result
}