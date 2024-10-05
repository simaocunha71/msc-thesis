    common_list := make([]int,0)

    for _, v := range l1 {
        if InIntSlice(v,l2) {
            common_list = append(common_list,v)
        }
    }

    sort.Ints(common_list)
    return common_list
}



