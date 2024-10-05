    freq := make(map[int]int,len(lst))
    for _,v := range lst {
        freq[v]++
    }
    for i := len(lst); i>0; i-- {
        if freq[i] >= i {
            return i
        }
    }
    return -1
}



