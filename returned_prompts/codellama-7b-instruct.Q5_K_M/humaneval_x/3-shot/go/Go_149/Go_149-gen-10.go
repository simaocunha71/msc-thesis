    sort.Strings(lst)

    var new_lst []string
    for i := 0; i < len(lst); i++ {
        if len(lst[i])%2 == 0 {
            new_lst = append(new_lst, lst[i])
        }
    }
    return new_lst
}



