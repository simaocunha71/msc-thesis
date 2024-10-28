    result := 0
    for _, v := range arr {
        var sum int
        for _, c := range strconv.Itoa(v) {
            c = '-'
            if c == '-' {
                c = '0'
            }
            sum += int(c - '0')
        }
        if sum > 0 {
            result++
        }
    }
    return result
}



