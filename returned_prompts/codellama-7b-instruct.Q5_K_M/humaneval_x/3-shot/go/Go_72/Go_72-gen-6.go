    for i:=0; i<len(q); i++{
        if q[i] != q[len(q)-1-i]{
            return false
        }
    }
    return true
}