    opening := 0
    closing := 0

    for _, b := range brackets {
        if b == '(' {
            opening += 1
        }else if b == ')' {
            closing += 1
        }

        if closing > opening {
            return false
        }
    }
    return closing == opening
}



