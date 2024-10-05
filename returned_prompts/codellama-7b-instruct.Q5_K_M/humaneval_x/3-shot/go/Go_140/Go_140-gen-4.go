    result := ""
    space_count := 0
    for _, c := range text {
        if c == ' ' {
            if space_count > 2 {
                result += "-"
                space_count = 0
            }else{
                result += "_"
                space_count += 1
            }
        }else{
            result += string(c)
            space_count = 0
        }
    }
    return result
}



