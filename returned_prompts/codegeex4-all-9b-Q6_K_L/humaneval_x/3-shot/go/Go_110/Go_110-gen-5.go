    even1, odd2 := 0, 0
    for _, v := range lst1 {
        if v % 2 == 0 {
            even1 += 1
        }
    }
    for _, v := range lst2 {
        if v % 2 == 1 {
            odd2 += 1
        }
    }
    if even1 >= odd2 {
        return "YES"
    }else{
        return "NO"
    }
}

