    var result int
    for _, c := range s {
        result += int(c - '0')
    }
    return result
}



