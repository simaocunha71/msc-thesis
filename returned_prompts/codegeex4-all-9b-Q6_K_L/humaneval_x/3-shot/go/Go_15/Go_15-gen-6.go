    var s string
    for i:=0;i<=n;i++{
        s += strconv.Itoa(i)
        if i!=n{
            s += " "
        }
    }
    return s
}



