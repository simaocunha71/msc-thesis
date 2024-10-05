    var result int = 0
    for _, c := range str {
        r := string(c)
        if strings.Count(str, r) > 0 {
            result += 1
        }
    }
    return result
}




