    var count_left int = 0
    var count_right int = 0

    for _, c := range lst[0] {
        if c == '(' {
            count_left += 1
        }else if c == ')' {
            count_right += 1
        }
    }
    for _, c := range lst[1] {
        if c == '(' {
            count_left += 1
        }else if c == ')' {
            count_right += 1
        }
    }
    if count_left == count_right{
        return "Yes"
    }
    return "No"
}



