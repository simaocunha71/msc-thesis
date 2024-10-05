    for i := 0; i < len(lst1); i++ {
        if lst1[i]%2 != 0 {
            for j := 0; j < len(lst2); j++ {
                if lst2[j]%2 == 0 {
                    lst1[i], lst2[j] = lst2[j], lst1[i]
                    break
                }
            }
        }
    }

    for i := 0; i < len(lst1); i++ {
        if lst1[i]%2 != 0 {
            return "NO"
        }
    }

    return "YES"
}



