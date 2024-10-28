    levels := make([]int, 0)
    level := 0
    max_level := 0

    for _, c := range strings.Replace(paren_string, " ", "", -1) {
        if c == '(' {
            level++
            if level > max_level {
                max_level = level
            }
        } else if c == ')' {
            level--
        }
    }

    levels = append(levels, max_level)
    return levels
}



