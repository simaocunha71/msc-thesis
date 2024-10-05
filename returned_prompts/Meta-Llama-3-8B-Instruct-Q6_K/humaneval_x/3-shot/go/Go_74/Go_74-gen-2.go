    var sum1 int
    var sum2 int
    for _, str := range lst1 {
        sum1 += len(str)
    }
    for _, str := range lst2 {
        sum2 += len(str)
    }
    if sum1 < sum2 {
        return lst1
    } else if sum1 > sum2 {
        return lst2
    } else {
        return lst1
    }
}
