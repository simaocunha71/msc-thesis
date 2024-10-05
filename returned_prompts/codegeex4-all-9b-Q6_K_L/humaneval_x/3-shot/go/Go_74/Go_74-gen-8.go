    total1 := 0
    total2 := 0

    for _, s := range lst1{
        total1 += len(s)
    }
    for _, s := range lst2{
        total2 += len(s)
    }

    if total1 <= total2{
        return lst1
    }else{
        return lst2
    }
}



