    var result []int
    i := 2
    for n > 1 {
        count := 0
        for n%i == 0 {
            n /= i
            count++
        }
        if count > 0 {
            result = append(result, int32(i))
            for count > 0 {
                count--
                result = append(result, int32(i))
            }
        }
        i++
    }
    return result
}
