    result := make([]rune, 0)

    for _, s := range lst{
        for _, c := range s {
            result = append(result, c)
        }
    }

    for _, c := range result {
        if c == '(' {
            result = append(result, ')')
        }
    }

    open := 0
    for _, c := range result {
        if c == '(' {
            open += 1
        } else {
            open -= 1
        }

        if open < 0 {
            return "No"
        }
    }

    if open > 0 {
        return "No"
    }

    return "Yes"
}

