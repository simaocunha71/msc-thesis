    var sum1 int = 0
    var sum2 int = 0

    for _, v := range lst1{
        sum1 += len(v)
    }

    for _, v := range lst2{
        sum2 += len(v)
    }

    if sum1 == sum2 {
        return lst1
    }else if sum1 < sum2 {
        return lst1
    }else{
        return lst2
    }
}