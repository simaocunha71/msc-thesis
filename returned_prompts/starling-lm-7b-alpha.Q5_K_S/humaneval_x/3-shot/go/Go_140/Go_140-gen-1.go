    var result string = ""
    var consecutive_spaces = false

    for _,c := range text {
        if c == ' ' {
            if consecutive_spaces {
                result += "-"
                consecutive_spaces = false
            } else {
                result += "_"
            }
        } else {
            result += string(c)
            consecutive_spaces = false
        }
    }
    return result
}



