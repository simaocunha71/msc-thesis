    var result string
    var count_digit int = 0
    var count_dot int = 0
    var index_dot int = 0
    var index_start int = 0

    for index, c := range file_name{
        if c >= '0' && c <= '9' {
            count_digit += 1
            if count_digit > 3 {
                result = "No"
                goto A
            }
        }else if c == '.' {
            count_dot += 1
            index_dot = index
            if count_dot > 1 {
                result = "No"
                goto A
            }
        }else if (c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z') {
            if count_digit == 0 {
                index_start = index
            }
        }else {
            result = "No"
            goto A
        }
    }

    if count_digit == 0 || count_dot == 0 || index_start == 0 || index_dot == 0 {
        result = "No"
    }else {
        var extension string = file_name[index_dot+1:]
        if extension == "txt" || extension == "exe" || extension == "dll" {
            result = "Yes"
        }else{
            result = "No"
        }
    }

    return result
}



