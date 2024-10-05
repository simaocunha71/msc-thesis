    counter := 0
    for _, char := range brackets {
        if string(char) == "<" {
            counter += 1
        } else if string(char) == ">" {
            counter -= 1
            if counter < 0 {
                return false
            }
        }
    }
    return counter == 0
}



