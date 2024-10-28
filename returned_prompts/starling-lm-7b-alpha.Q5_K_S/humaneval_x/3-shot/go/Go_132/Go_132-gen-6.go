    result := false
    for _, c := range s {
        if c == '[' {
            result = true
        }
    }
    return result
}



