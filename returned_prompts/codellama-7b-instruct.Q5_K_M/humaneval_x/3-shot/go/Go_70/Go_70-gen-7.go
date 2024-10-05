    sort.Slice(lst, func(i, j int) bool {
        if i == j {
            return false
        }
        if i < j {
            return true
        }
        return false
    })
    return lst
}



