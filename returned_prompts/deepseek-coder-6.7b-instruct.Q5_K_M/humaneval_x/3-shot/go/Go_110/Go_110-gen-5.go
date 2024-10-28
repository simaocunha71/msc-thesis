    odd1, even1 := 0, 0
    odd2, even2 := 0, 0

    for _, v := range lst1 {
        if v%2 == 0 {
            even1++
        } else {
            odd1++
        }
    }

    for _, v := range lst2 {
        if v%2 == 0 {
            even2++
        } else {
            odd2++
        }
    }

    if even1+odd2 >= odd1 && even2+odd1 >= odd2 {
        return "YES"
    }
    return "NO"
}



