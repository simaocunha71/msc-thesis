    result := 0
    for _, e := range arr {
        number := strconv.Itoa(e)
        sum := 0
        for _, c := range number {
            sum += int(c - '0')
        }
        if sum > 0 {
            result += 1
        }
    }
    return result
}



