    left := 0
    right := 0
    for _, s := range lst {
        for _, c := range s {
            if c == '(' {
                left++
            }else if c == ')' {
                right++
            }
        }
    }
    if left == right {
        return "Yes"
    }else {
        return "No"
    }
}



