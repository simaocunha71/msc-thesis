    max := 0
    for _, i := range lst {
        if i > max {
            max = i
        }
    }
    max_str := strconv.Itoa(max)
    result := 0
    for _, c := range max_str {
        result += int(c - '0')
    }
    return result
}



