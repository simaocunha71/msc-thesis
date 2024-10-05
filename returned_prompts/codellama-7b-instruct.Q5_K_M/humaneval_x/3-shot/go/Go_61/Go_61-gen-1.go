    if len(brackets)%2 == 1 {
        return false
    }

    stack := make([]rune, 0)

    for _, c := range brackets{
        if c == '('{
            stack = append(stack, c)
        }else if len(stack) == 0{
            return false
        }else{
            stack = stack[:len(stack)-1]
        }
    }

    return len(stack) == 0
}



