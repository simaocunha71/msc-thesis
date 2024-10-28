    odd1, even2 := 0, 0
    for _, v := range lst1 {
        if v % 2 != 0 {
            odd1++
        }
    }
    for _, v := range lst2 {
        if v % 2 == 0 {
            even2++
        }
    }
    if odd1 <= even2 {
        return "YES"
    } else {
        return "NO"
    }
}



