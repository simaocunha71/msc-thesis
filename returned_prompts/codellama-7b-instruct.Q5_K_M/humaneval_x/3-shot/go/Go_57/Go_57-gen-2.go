    if len(l) < 2 {
        return true
    }

    if l[1] > l[0] {
        for i := 1; i < len(l); i++ {
            if l[i] < l[i-1] {
                return false
            }
        }
    }else{
        for i := 1; i < len(l); i++ {
            if l[i] > l[i-1] {
                return false
            }
        }
    }
    return true
}



