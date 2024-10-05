    var has_dot := false
    var has_invalid_chars := false
    var has_invalid_length := false

    if len(file_name) > 3 {
        has_invalid_length = true
    }

    for _, c := range file_name{
        if c == '.'{
            has_dot = true
        }else if c < '0' || c > '9'{
            if !(c >= 'a' && c <= 'z') && !(c >= 'A' && c <= 'Z'){
                has_invalid_chars = true
                break
            }
        }
    }

    if !has_dot || has_invalid_chars || has_invalid_length {
        return "No"
    }else{
        return "Yes"
    }
}



