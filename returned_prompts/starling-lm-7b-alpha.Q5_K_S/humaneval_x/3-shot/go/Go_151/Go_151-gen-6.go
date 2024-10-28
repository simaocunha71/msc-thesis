    result := 0
    for _, c := range lst {
        if c > 0 && math.Floor(c) == c {
            result += c*c
        }
    }
    return result
}



