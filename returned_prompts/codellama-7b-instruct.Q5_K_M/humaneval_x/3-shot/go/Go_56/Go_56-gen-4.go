    var opening_bracket = 0
    for _, c := range brackets {
        if c == '<' {
            opening_bracket += 1
        }else if c == '>' {
            opening_bracket -= 1
        }
    }
    return opening_bracket == 0
}



