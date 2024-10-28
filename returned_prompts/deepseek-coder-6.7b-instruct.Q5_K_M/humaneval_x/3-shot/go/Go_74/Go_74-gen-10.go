    var lst1Total int 
    var lst2Total int 
    for _, str := range lst1 {
        lst1Total += len(str)
    }
    for _, str := range lst2 {
        lst2Total += len(str)
    }
    if lst1Total < lst2Total {
        return lst1
    }
    return lst2
}



