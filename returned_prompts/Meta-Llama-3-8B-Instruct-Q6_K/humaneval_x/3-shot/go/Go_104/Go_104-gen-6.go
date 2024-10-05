    result := make([]int, 0)
    for _, num := range x {
        var isOk bool
        s := strconv.Itoa(num)
        for _, c := range s {
            if c % 2 == 0 {
                isOk = false
                break
            }
        }
        if isOk {
            result = append(result, num)
        }
    }
    sort.Ints(result)
    return result
}