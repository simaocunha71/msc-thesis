    s1 := lst[0]
    s2 := lst[1]
    for _, c := range s1 {
        if string(c) == "(" {
            s1 = s1 + ")"
        } else {
            s1 = s1 + "("
        }
    }
    for _, c := range s2 {
        if string(c) == "(" {
            s2 = s2 + ")"
        } else {
            s2 = s2 + "("
        }
    }
    if IsBalanced(s1+s2) {
        return "Yes"
    }
    return "No"
}

func IsBalanced(s string) bool {
    count := 0
    for _, c := range s {
        if string(c) == "(" {
            count++
        } else {
            count--
            if count < 0 {
                return false
            }
        }
    }
    return count == 0
}



