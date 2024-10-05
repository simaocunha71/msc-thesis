    var total1,total2 int
    for _,v := range lst1{
        total1 += len(v)
    }
    for _,v := range lst2{
        total2 += len(v)
    }
    if total1 < total2{
        return lst1
    }else if total2 < total1{
        return lst2
    }else{
        return lst1
    }
}