    if len(q)==1{
        if q[0] <= w{
            return true
        }
    }

    if len(q)==2{
        if q[0] == q[1] && q[0] <= w{
            return true
        }
    }

    if len(q)>2{
        if q[0] == q[len(q)-1]{
            if len(q)-2 <= w{
                return true
            }
        }

        if q[0] < q[len(q)-1] && q[0] <= w{
            return true
        }
    }

    return false
}



