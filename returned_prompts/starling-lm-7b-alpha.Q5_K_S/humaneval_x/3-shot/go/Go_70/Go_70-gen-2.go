    lst = append(lst, math.MaxInt32)
    sort.Slice(lst, func(i, j int) bool {
        return lst[i] < lst[j]
    })
    lst = lst[:len(lst)-1]
    return lst
}



