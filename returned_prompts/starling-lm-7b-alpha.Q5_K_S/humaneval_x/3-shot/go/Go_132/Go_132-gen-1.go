    result := 0
    for _, c := range s {
        if c == '[' {
            result += 1
        }else if c == ']' {
            result -= 1
            if result < 0 {
                return true
            }
        }
    }
    return false
}



