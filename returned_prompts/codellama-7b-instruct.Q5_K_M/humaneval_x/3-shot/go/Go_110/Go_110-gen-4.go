    for _, v1 := range lst1{
        for _, v2 := range lst2{
            if v1%2 != 0 && v2%2 == 0{
                return "YES"
            }
        }
    }
    return "NO"
}



