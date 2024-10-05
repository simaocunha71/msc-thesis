    var count int
    for _, str := range lst {
        for _, ch := range str {
            if string(ch) == "(" {
                count++
            } else if string(ch) == ")" {
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



