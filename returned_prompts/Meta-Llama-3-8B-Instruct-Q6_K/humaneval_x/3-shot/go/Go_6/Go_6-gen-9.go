    result := make([]int, 0)
    current_depth := 0

    for _, c := range strings.Split(paren_string," "){
        for _, d := range []rune(c){
            if d == '(' {
                current_depth += 1
            }else if d == ')' {
                current_depth -= 1
            }
        }
        result = append(result, current_depth)
        current_depth = 0
    }
    return result
}