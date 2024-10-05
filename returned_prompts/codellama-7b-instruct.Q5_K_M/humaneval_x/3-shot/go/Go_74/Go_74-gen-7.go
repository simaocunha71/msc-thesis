    var total_chars1 int = 0
    var total_chars2 int = 0

    for _, word := range lst1 {
        total_chars1 += len(word)
    }
    for _, word := range lst2 {
        total_chars2 += len(word)
    }

    if total_chars1 < total_chars2 {
        return lst1
    }else if total_chars1 > total_chars2{
        return lst2
    }else{
        return lst1
    }

}



