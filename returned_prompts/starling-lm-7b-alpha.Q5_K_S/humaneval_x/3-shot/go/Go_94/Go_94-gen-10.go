    max := -1
    for _, v := range lst {
        if v > max {
            max = v
        }
    }
    if max == 0 {
        return 0
    }
    str_max := strconv.Itoa(max)
    result := 0
    for _, c := range str_max {
        result += int(c - '0')
    }
    return result
}



