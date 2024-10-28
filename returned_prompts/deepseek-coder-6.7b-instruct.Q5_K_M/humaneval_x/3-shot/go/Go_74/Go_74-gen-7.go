    var sum1, sum2 int
    for _, v := range lst1 {
        sum1 += len(v)
    }
    for _, v := range lst2 {
        sum2 += len(v)
    }
    if sum1 < sum2 {
        return lst1
    }
    return lst2
}



