    for _, v := range lst1{
        if v%2!=0{
            for _, v2 := range lst2{
                if v2%2==0{
                    return "YES"
                }
            }
            return "NO"
        }
    }
    return "YES"
}



