    depth := 0
    for _, c := range brackets{
        if c == '('{
            depth += 1
        }else if c == '){
            depth -= 1
        }
        if depth < 0{
            return false
        }
    }
    if depth == 0{
        return true
    }
    return false
}