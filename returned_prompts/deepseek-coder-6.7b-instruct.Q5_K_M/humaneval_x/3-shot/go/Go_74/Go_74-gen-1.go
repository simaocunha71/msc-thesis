    var count1, count2 int
    for _, v := range lst1 {
        count1 += len(v)
    }
    for _, v := range lst2 {
        count2 += len(v)
    }
    if count1 < count2 {
        return lst1
    }
    if count2 < count1 {
        return lst2
    }
    return lst1
}



