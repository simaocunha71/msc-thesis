    odd1, odd2 := 0, 0
    for i := 0; i < len(lst1); i++ {
        if lst1[i] % 2 != 0 {
            odd1++
        }
    }

    for i := 0; i < len(lst2); i++ {
        if lst2[i] % 2 != 0 {
            odd2++
        }
    }

    if odd1 > odd2 {
        return "NO"
    }

    return "YES"
}



