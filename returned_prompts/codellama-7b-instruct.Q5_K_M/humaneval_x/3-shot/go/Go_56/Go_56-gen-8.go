    var opening_brackets []rune = []rune{'<','>'}
    var closing_brackets []rune = []rune{'>','<'}
    var stack []rune = make([]rune, 0)
    var is_correct bool = true

    for i := 0; i < len(brackets); i++ {
        var c = brackets[i]

        if contains(opening_brackets, c){
            stack = append(stack, c)
        }else if contains(closing_brackets, c){
            var last_bracket = stack[len(stack)-1]
            var matching_bracket rune = -1

            for j := 0; j < len(opening_brackets); j++ {
                if opening_brackets[j] == last_bracket{
                    matching_bracket = closing_brackets[j]
                    break
                }
            }

            if matching_bracket == c{
                stack = stack[:len(stack)-1]
            }else{
                is_correct = false
                break
            }
        }
    }

    if len(stack) > 0{
        is_correct = false
    }

    return is_correct
}

func contains(s []rune, e rune) bool {
    for _, a := range s {
        if a == e {
            return true
        }
    }
    return false
}



