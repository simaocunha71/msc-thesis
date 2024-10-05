    var total1 int
    var total2 int
    for _, word := range lst1 {
        total1 += len(word)
    }
    for _, word := range lst2 {
        total2 += len(word)
    }
    if total1 < total2 {
        return lst1
    }else if total1 > total2 {
        return lst2
    }else {
        return lst1
    }
}



