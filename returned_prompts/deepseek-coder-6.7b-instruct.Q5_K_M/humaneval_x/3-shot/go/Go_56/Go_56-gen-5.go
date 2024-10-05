    count := 0
    for _, char := range brackets {
        if char == '<' {
            count++
        } else if char == '>' {
            if count == 0 {
                return false
            }
            count--
        }
    }
    return count == 0
}



