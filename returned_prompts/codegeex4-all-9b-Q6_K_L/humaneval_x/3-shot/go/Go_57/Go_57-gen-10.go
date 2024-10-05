    if len(l) < 2{
        return true
    }
    is_increase := l[1] > l[0]
    for i := 2; i < len(l); i++{
        if is_increase && l[i] < l[i-1]{
            return false
        }
        if !is_increase && l[i] > l[i-1]{
            return false
        }
    }
    return true
}



