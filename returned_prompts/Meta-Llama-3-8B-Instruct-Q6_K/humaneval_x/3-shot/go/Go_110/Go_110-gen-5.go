    for _, v := range lst1 {
        if v%2 != 0 {
            for _, w := range lst2 {
                if w%2 == 0 {
                    return "YES"
                }
            }
            return "NO"
        }
    }
    return "YES"
} 





