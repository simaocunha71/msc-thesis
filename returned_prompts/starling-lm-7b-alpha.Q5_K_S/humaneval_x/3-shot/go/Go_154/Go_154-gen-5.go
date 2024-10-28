    for _,c := range a {
        if string(c) == b {
            return true
        }
    }
    for _, c := range a {
        if string(c) == b[len(b)-1:] {
            return true
        }
    }
    for _, c := range a {
        if string(c) == b[0:len(b)-1] {
            return true
        }
    }
    return false
}



