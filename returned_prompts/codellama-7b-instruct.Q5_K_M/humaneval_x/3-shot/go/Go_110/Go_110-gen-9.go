    for i := 0; i < len(lst1); i++{
        if lst1[i]%2 != 0{
            continue
        }
        for j := 0; j < len(lst2); j++{
            if lst2[j]%2 != 0{
                continue
            }
            temp := lst1[i]
            lst1[i] = lst2[j]
            lst2[j] = temp
            return "YES"
        }
    }
    return "NO"
}



