    var total1, total2 int
    for _, str := range lst1 {
        total1 += len(str)
    }
    for _, str := range lst2 {
        total2 += len(str)
    }
    if total1 <= total2 {
        return lst1
    } else {
        return lst2
    }
}



