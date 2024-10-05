    count1 := 0
    for _, s := range lst1 {
        count1 += len(s)
    }
    count2 := 0
    for _, s := range lst2 {
        count2 += len(s)
    }
    if count1 <= count2 {
        return lst1
    }
    return lst2
}



