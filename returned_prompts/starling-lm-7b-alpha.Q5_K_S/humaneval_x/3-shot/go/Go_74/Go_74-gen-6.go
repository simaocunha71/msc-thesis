    c1,c2:=0,0
    for _,s:=range lst1{
        c1+=len(s)
    }
    for _,s:=range lst2{
        c2+=len(s)
    }
    if c1<c2{
        return lst1
    }else if c1==c2{
        return lst1
    }else {
        return lst2
    }
}



