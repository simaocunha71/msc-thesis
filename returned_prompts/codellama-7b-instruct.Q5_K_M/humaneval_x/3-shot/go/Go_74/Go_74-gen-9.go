    var total_chars_in_lst1 int = 0
    var total_chars_in_lst2 int = 0

    for i := 0; i < len(lst1); i++ {
        total_chars_in_lst1 += len(lst1[i])
    }

    for i := 0; i < len(lst2); i++ {
        total_chars_in_lst2 += len(lst2[i])
    }

    if total_chars_in_lst1 < total_chars_in_lst2 {
        return lst1
    }else{
        return lst2
    }
}



