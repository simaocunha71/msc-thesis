    if len(lst1)==0 || len(lst2)==0{
        return lst1
    }

    total_lst1 :=0
    for _,s := range lst1{
        total_lst1+=len(s)
    }

    total_lst2 :=0
    for _,s := range lst2{
        total_lst2+=len(s)
    }

    if total_lst2<total_lst1{
        return lst2
    }

    return lst1
}



