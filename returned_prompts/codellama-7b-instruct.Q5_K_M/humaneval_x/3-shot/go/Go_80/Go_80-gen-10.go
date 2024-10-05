    if len(s) < 3{
        return false
    }

    var current_index int = 0
    var current_string string = ""
    for i := 0; i < len(s); i++ {
        current_string = string(s[i])
        current_index = 0

        for j := 0; j < i; j++ {
            if string(s[j]) == current_string {
                current_index += 1
            }
        }

        if current_index > 0 {
            return false
        }

    }
    return true
}



