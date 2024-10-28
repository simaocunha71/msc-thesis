    if len(brackets) == 0{
        return true
    }

    var stack []rune
    for _, c := range brackets{
        if c == '<'{
            stack = append(stack, c)
        }else if c == '>' {
            if len(stack) == 0{
                return false
            }
            stack = stack[:len(stack)-1]
        }
    }

    return len(stack) == 0
}



