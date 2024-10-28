    if len(s)==0{
        return false
    }
    var stack []rune
    var current_char rune
    for _,char := range s{
        current_char = char
        if current_char == '['{
            stack = append(stack,current_char)
        }else if current_char == ']'{
            if len(stack)==0{
                return false
            }
            last_char := stack[len(stack)-1]
            if last_char == '['{
                stack = stack[:len(stack)-1]
            }else{
                return true
            }
        }
    }
    return len(stack)==0
}



