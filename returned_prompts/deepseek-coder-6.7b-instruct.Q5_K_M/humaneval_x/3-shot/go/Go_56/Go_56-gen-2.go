    count := 0
    for _, bracket := range brackets {
        if bracket == '<' {
            count++
        } else if bracket == '>' {
            if count == 0 {
                return false
            }
            count--
        }
    }
    return count == 0
}



