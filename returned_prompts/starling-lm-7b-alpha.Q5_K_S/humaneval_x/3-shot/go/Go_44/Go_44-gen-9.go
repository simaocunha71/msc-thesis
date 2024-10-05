    var result []rune

    for x > 0 {
        result = append(result, []rune(strconv.Itoa(x % base))...)
        x /= base
    }
    return string(result)
}



