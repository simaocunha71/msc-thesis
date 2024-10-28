    count := 0
    for _, char := range brackets {
        if string(char) == "(" {
            count += 1
        } else if string(char) == ")" {
            if count == 0 {
                return false
            }
            count -= 1
        }
    }
    return count == 0
}



