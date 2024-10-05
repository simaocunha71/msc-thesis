    for _, v := range lst {
        if v == ")" && len(lst) > 0 {
            lst = append(lst[:0], lst[1:]...)
            return MatchParens(lst)
        }
        if v == "(" {
            for i, w := range lst {
                if w == ")" && i != 0 {
                    lst = append(lst[:i], lst[i+1:]...)
                    return MatchParens(lst)
                }
            }
        }
    }
    if len(lst) == 0 {
        return "Yes"
    }
    return "No"
}



