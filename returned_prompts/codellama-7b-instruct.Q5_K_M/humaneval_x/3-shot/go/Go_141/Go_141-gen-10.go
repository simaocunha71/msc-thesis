    var sub_before_dot, sub_after_dot string
    var has_dot, has_more_than_three_digits bool
    var is_valid bool

    sub_before_dot, sub_after_dot = strings.Split(file_name, ".")

    if len(sub_before_dot) == 0 {
        return "No"
    }
    if len(sub_after_dot) == 0 {
        return "No"
    }
    if len(sub_before_dot) > 3 {
        has_more_than_three_digits = true
    }
    if sub_after_dot != "txt" && sub_after_dot != "exe" && sub_after_dot != "dll"{
        return "No"
    }

    for _, c := range sub_before_dot {
        if !(c >= 'a' && c <= 'z') && !(c >= 'A' && c <= 'Z') {
            return "No"
        }
    }

    if has_dot && !has_more_than_three_digits {
        is_valid = true
    }else{
        is_valid = false
    }

    if is_valid {
        return "Yes"
    }else{
        return "No"
    }

}



