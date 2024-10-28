    sort.Slice(lst, func(i, j int) bool {
        if lst[i] < lst[j] {
            return true
        }else if lst[i] > lst[j] {
            return false
        }else {
            if i < j {
                return true
            }else {
                return false
            }
        }
    })
    return lst
}



