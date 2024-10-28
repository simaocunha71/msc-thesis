    if len(q)==1 {
        if q[0]>w {
            return false
        }
        return true
    }

    if q[0]!=q[len(q)-1] {
        return false
    }

    if q[0]>w {
        return false
    }

    for i:=0;i<len(q)/2;i++ {
        if q[i]!=q[len(q)-i-1] {
            return false
        }
    }
    return true
}



