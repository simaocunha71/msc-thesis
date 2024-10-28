    var result string = ""
    var current_string string = ""

    for _, char := range text {
        if char == ' ' {
            if len(current_string) > 1 {
                current_string = current_string + "-"
            }
            current_string = current_string + "_"
        }else{
            current_string = current_string + string(char)
        }
    }

    return current_string
}



