    if len(q)==1{
        if q[0]<=w{
            return true
        }else{
            return false
        }
    }

    if len(q)==0{
        return false
    }

    if q[0]==q[len(q)-1]{
        q=q[1:len(q)-1]
        return WillItFly(q,w)
    }else{
        return false
    }
}



