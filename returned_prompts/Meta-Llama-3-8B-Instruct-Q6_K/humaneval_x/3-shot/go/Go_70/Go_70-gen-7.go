    if len(lst) == 0 {
        return []int{}
    }

    sort.Slice(lst, func(i, j int) bool {
        if i%2 == 0 {
            return lst[i] < lst[j]
        } else {
            return lst[i] > lst[j]
        }
    })

    return lst
} 





