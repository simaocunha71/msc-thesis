    left_brackets := 0
    right_brackets := 0

    for _, c := range brackets {
        if c == "<" {
            left_brackets += 1
        }else if c == ">" {
            right_brackets += 1
        }
    }
    if left_brackets == right_brackets {
        return true
    }else {
        return false
    }
}



