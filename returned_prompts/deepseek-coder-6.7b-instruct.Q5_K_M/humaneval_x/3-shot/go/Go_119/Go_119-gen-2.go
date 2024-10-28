    var count int
    for _, str := range lst {
        for _, char := range str {
            if string(char) == "(" {
                count++
            } else if string(char) == ")" {
                if count == 0 {
                    return "No"
                }
                count--
            }
        }
    }
    if count != 0 {
        return "No"
    }
    return "Yes"
}



