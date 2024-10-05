    if len(l) < 2 {
        return true
    }

    var increasing bool
    for i := 0; i < len(l)-1; i++ {
        if l[i] == l[i+1] {
            continue
        }
        if l[i] < l[i+1] {
            if increasing != true {
                increasing = true
            } else if increasing != true {
                return false
            }
        }
        if l[i] > l[i+1] {
            if increasing != false {
                increasing = false
            } else if increasing != false {
                return false
            }
        }
    }
    return true
}



