    if len(q)==1 && q[0]<=w{
        return true
    }

    for i:=0; i<len(q); i++{
        if q[i]==q[len(q)-1-i]{
            if q[i]<=w{
                return true
            }
        }
    }

    return false
}



