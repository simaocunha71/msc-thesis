    sort.Slice(lst, func(i, j int) bool {
        if lst[i] < lst[j] {
            return true
        }else if lst[i] > lst[j] {
            return false
        }else{
            return i < j
        }
    })
    return lst
}



