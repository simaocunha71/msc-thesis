    result := make([]int, 0)
    current_string := make([]rune, 0)
    current_depth := 0
    max_depth := 0

    for _, c := range paren_string {
        if c == '(' {
            current_depth += 1
            current_string = append(current_string, c)

            if current_depth > max_depth {
                max_depth = current_depth
            }

        }else if c== ')'{
            current_depth -= 1
            current_string = append(current_string, c)

            if current_depth == 0{
                result = append(result, max_depth)
                current_string =  make([]rune, 0)
                max_depth = 0
            }
        }

    }
    return result
}



