    count := 0
    for _, char := range brackets {
        if char == '(' {
            count += 1
        } else if char == ')' {
            count -= 1
            if count < 0 {
                return false
            }
        }
    }
    return count == 0
}



