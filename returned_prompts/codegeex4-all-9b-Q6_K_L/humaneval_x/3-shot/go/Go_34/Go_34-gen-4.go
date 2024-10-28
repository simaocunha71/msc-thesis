    sort.Ints(l)
    newlist := make([]int, 0)
    for _, v := range l {
        if len(newlist) == 0 || newlist[len(newlist)-1] != v {
            newlist = append(newlist, v)
        }
    }
    return newlist
}



