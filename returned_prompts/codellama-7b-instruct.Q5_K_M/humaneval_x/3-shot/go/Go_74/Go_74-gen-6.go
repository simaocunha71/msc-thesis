    if len(lst1)==0 {return lst2}
    if len(lst2)==0 {return lst1}

    var total_lst1 int
    var total_lst2 int

    for _,s := range lst1 {
        total_lst1 += len(s)
    }

    for _,s := range lst2 {
        total_lst2 += len(s)
    }

    if total_lst1 < total_lst2 {return lst1}
    if total_lst1 > total_lst2 {return lst2}

    return lst1
}



