// get the total character of each list
    sum1 := 0
    for _, str := range lst1 {
        sum1 += len(str)
    }
    sum2 := 0
    for _, str := range lst2 {
        sum2 += len(str)
    }
// return the list with less character
    if sum1 < sum2 {
        return lst1
    }
    return lst2
}