    result := true
    current_depth := 0
    for _, c := range brackets {
        if c == '<' {
            current_depth += 1
        }else if c== '>'{
            current_depth -= 1
            if current_depth < 0{
                result = false
                break
            }
        }
    }
    return result && current_depth == 0
}



