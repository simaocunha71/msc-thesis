    result := 0
    for _, v := range arr {
        tmp := strconv.Itoa(v)
        sum := 0
        for _, c := range tmp {
            sum += int(c-'0')
        }
        if sum > 0 {
            result += 1
        }
    }
    return result
}



