    var oddLengths := make([]string, 0)
    for _, s := range lst {
        if len(s) % 2 == 1 {
            oddLengths = append(oddLengths, s)
        }
    }
    oddLengths = oddLengths[:len(oddLengths)/2:len(oddLengths)]
    lst = append(lst, oddLengths...)

    sort.Slice(lst, func(i, j int) bool {
        return len(lst[i]) < len(lst[j]) || len(lst[i]) == len(lst[j]) && lst[i] < lst[j]
    })

    return lst
}



