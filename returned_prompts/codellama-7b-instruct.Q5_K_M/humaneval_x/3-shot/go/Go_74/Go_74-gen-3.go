    var total_chars_lst1 int = 0
    for _,s := range lst1{
        total_chars_lst1 += len(s)
    }

    var total_chars_lst2 int = 0
    for _,s := range lst2{
        total_chars_lst2 += len(s)
    }

    if total_chars_lst1 < total_chars_lst2{
        return lst1
    }else if total_chars_lst1 > total_chars_lst2{
        return lst2
    }else{
        return lst1
    }
}



