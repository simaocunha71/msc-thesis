    if n==1{
        return 1
    }

    prev := 1
    curr := 1

    for i:=2;i<n;i++{
        prev,curr = curr,prev+curr
    }
    return curr
}



