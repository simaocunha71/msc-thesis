    count := 0
    for _, c := range brackets {
        if c == '(' {
            count++
        } else if c == ')' {
            if count == 0 {
                return false
            }
            count--
        }
    }
    return count == 0
}



