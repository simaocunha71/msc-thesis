    var opening_brackets map[rune]bool = make(map[rune]bool)
    opening_brackets['<'] = true

    var closing_brackets map[rune]bool = make(map[rune]bool)
    closing_brackets['>'] = true

    var stack []rune = make([]rune, 0)

    for _, c := range brackets {
        if opening_brackets[c] {
            stack = append(stack, c)
        }else if closing_brackets[c] {
            if len(stack) == 0 {
                return false
            }
            var top_bracket rune = stack[len(stack) - 1]
            stack = stack[:len(stack) - 1]
            if opening_brackets[top_bracket] != closing_brackets[c] {
                return false
            }
        }
    }
    return len(stack) == 0
}



