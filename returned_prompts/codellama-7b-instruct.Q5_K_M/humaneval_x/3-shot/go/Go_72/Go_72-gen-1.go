    if len(q)==1{
        return q[0]<=w
    }

    mid :=len(q)>>1
    left := q[:mid]
    right:=q[mid:]

    if len(left)==1 && len(right)==1{
        if left[0]==right[0]{
            return left[0]<=w
        }
    }

    if left[0]==right[len(right)-1]{
        return WillItFly(left,w) || WillItFly(right,w)
    }

    return false
}



