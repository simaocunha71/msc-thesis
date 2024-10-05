    var count int = 0

    for _, c := range s {
        if c == '[' {
            count += 1
        } else if c == ']' {
            count -= 1
        }
        if count < 0 {
            return false
        }
    }
    return count == 0
}

