
    if len(lst1) == 0 {
        return "YES"
    }
    if len(lst2) == 0 {
        return "NO"
    }
    if len(lst1) < len(lst2) {
        return "NO"
    }
    if len(lst1) > len(lst2) {
        return "YES"
    }
    lst1len := len(lst1)
    for i := 0; i < lst1len; i++ {
        if lst1[i] % 2 == 1 {
            if i+1 >= lst1len {
                return "NO"
            }
            for j := i+1; j < lst1len; j++ {
                if lst2[j] % 2 == 0 {
                    lst1[i] = lst2[j]
                    lst2[j] = lst1[i+1]
                    lst1[i+1] = lst2[j]
                    break
                }
            }
        }
    }
    return "YES"
}













































































































































































































































