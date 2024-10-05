    if x==1{
        return true
    }

    if n==1{
        return false
    }

    for i:=2;i*i<=x;i++{
        p:=i
        for p<x{
            p*=i
            if p==x{
                return true
            }
        }
    }
    return false
}



