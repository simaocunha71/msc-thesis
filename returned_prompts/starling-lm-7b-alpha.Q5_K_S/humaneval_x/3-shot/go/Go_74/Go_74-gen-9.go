    total_char_lst1:=0
    for _,s:=range(lst1){
        total_char_lst1+=len(s)
    }
    total_char_lst2:=0
    for _,s:=range(lst2){
        total_char_lst2+=len(s)
    }
    if total_char_lst1<total_char_lst2{
        return lst1
    }else if total_char_lst1>total_char_lst2{
        return lst2
    }else{
        return lst1
    }
}



