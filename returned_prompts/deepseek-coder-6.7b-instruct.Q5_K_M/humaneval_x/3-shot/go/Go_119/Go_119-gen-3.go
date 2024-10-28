    var count int
    for _, str := range lst {
        for _, c := range str {
            if c == '(' {
                count++
            } else if c == ')' {
                count--
                if count < 0 {
                    return "No"
                }
            }
        }
    }
    if count != 0 {
        return "No"
    }
    return "Yes"
}



