    total1 := len(strings.Join(lst1, ""))
    total2 := len(strings.Join(lst2, ""))

    if total1 < total2 {
        return lst1
    } else if total1 > total2 {
        return lst2
    }
    return lst1
}



