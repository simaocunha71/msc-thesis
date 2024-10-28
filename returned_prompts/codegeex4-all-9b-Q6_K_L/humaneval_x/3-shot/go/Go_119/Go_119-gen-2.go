    result := make([]rune, 0)

    for _, s := range lst{
        for _, c := range s{
            result = append(result, c)
        }
    }
    depth := 0
    for _, c := range result{
        if c == '('{
            depth += 1
        }else if c == ')'{
            depth -= 1
        }
        if depth < 0{
            return "No"
        }
    }
    if depth != 0{
        return "No"
    }
    return "Yes"
}