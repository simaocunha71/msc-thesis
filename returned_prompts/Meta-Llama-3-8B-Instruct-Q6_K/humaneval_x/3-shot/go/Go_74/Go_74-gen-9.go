    var sum1 int
    var sum2 int

    for _, s := range lst1 {
        sum1 += len(s)
    }
    for _, s := range lst2 {
        sum2 += len(s)
    }

    if sum1 < sum2 {
        return lst1
    } else if sum1 > sum2 {
        return lst2
    } else {
        return lst1
    }
}