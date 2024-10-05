    var opening_brackets int = 0
    var closing_brackets int = 0
    for _, c := range brackets {
        if c == '(' {
            opening_brackets += 1
        } else if c == ')' {
            closing_brackets += 1
        }
    }
    if opening_brackets == closing_brackets {
        return true
    } else {
        return false
    }
}


