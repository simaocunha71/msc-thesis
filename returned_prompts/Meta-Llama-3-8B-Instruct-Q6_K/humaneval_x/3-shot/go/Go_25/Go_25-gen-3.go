    result := make([]int, 0)
    i := 2
    for n > 1 {
        count := 0
        for n%i == 0 {
            count++
            n /= i
        }
        if count > 0 {
            result = append(result, int(i))
            for count > 0 {
                count--
                result = append(result, int(i))
            }
        }
        i++
    }
    return result
}