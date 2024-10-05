    total1 := 0
    total2 := 0

    for _, str := range lst1 {
        total1 += len(str)
    }

    for _, str := range lst2 {
        total2 += len(str)
    }

    if total1 < total2 {
        return lst1
    } else if total1 > total2 {
        return lst2
    } else {
        return lst1
    }
} 



