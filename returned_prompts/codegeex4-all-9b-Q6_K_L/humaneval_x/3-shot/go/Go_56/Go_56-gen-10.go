    current_depth := 0
    for _, c := range brackets {
        if c == '<'{
            current_depth += 1
        }else{
            current_depth -= 1
        }
        if current_depth < 0{
            return false
        }
    }
    return current_depth == 0
}



