    var result_string := make([]rune, 0)
    for x > 0 {
        remainder := x % base
        x /= base
        result_string = append(result_string, strconv.Itoa(int(remainder))[0])
    }
    return string(result_string)
}



