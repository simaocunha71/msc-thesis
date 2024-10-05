    result := 0
    for _, n := range arr {
        if n > 0 {
            result += 1
        } else {
            var sum int = 0
            for _, c := range strconv.Itoa(n) {
                sum += int(c - '0')
            }
            if sum > 0 {
                result += 1
            }
        }
    }
    return result
}



