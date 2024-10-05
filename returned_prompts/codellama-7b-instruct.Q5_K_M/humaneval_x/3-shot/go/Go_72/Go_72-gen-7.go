    if len(q)==1 {
        return q[0]<=w
    }
    for i:=0;i<len(q)/2;i++ {
        if q[i]!=q[len(q)-i-1] {
            return false
        }
    }
    return true
}



