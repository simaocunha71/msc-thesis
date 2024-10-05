    max := 0
    for _, i := range lst {
        if i > max {
            max = i
        }
    }
    var max_str string = strconv.Itoa(max)
    var result int = 0
    for _, j := range max_str {
        result += int(j) - int('0')
    }
    return result
}



