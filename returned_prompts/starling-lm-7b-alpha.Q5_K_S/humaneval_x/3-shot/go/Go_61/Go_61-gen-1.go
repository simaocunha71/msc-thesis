    opening_brackets := 0
    for _, c := range brackets {
        if c == '(' {
            opening_brackets += 1
        }else if c==')'{
            if opening_brackets > 0 {
                opening_brackets -= 1
            }else {
                return false
            }
        }
    }
    return opening_brackets == 0
}



