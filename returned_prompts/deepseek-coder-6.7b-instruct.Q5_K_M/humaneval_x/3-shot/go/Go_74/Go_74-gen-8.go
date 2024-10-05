    sum1  := 0
    sum2  := 0
    for _, s := range lst1  {
        sum1 += len(s)
    }
    for _, s := range lst2  {
        sum2 += len(s)
    }
    if sum1 < sum2  {
        return lst1
    }else if sum2 < sum1  {
        return lst2
    }
    return lst1
}


