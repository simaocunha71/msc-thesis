    for i := 0; i < len(lst2); i++ {
        if lst2[i]%2==0{
            lst1[i%len(lst1)] = lst2[i]
        }
    }
    for i:=0; i < len(lst1); i++{
        if lst1[i]%2!=0{
            return "NO"
        }
    }
    return "YES"
}



