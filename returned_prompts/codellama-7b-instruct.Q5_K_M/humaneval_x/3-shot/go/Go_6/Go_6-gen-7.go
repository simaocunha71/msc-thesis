    result := make([]int, 0)
    current_level := 0
    current_string := make([]rune, 0)

    for _, c := range paren_string {
        if c == '(' {
            current_level += 1
            current_string = append(current_string, c)
        }else if c== ')'{
            current_level -= 1
            current_string = append(current_string, c)

            if current_level == 0{
                result = append(result, len(current_string) - 2)
                current_string =  make([]rune, 0)
            }
        }

    }
    return result
}



