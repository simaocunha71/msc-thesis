    total_chars_lst1 := 0
    total_chars_lst2 := 0

    for _, s := range lst1{
        total_chars_lst1 += len(s)
    }

    for _, s := range lst2{
        total_chars_lst2 += len(s)
    }

    if total_chars_lst1 < total_chars_lst2{
        return lst1
    }else if total_chars_lst2 < total_chars_lst1{
        return lst2
    }else{
        return lst1
    }
}



