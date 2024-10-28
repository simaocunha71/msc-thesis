    sort.Slice(lst, func(i int, j int) bool {
        return len(lst[i]) < len(lst[j]) || (len(lst[i]) == len(lst[j]) && lst[i] < lst[j])
    })
    return lst


func list_sort(lst []string) []string {
    newLst := make([]string, 0)
    for _, v := range lst {
        if len(v)%2 != 0 {
            continue
        }
        newLst = append(newLst, v)
    }
    sort.Slice(newLst, func(i int, j int) bool {
        return len(newLst[i]) < len(newLst[j]) || (len(newLst[i]) == len(newLst[j]) && newLst[i] < newLst[j])
    })
    return newLst
}


func list_sort(lst []string) []string {
    newLst := make([]string, 0)
    for _, v := range lst {
        if len(v)%2 != 0 {
            continue
        }
        newLst = append(newLst, v)
    }
    sort.Slice(newLst, func(i int, j int) bool {
        return len(newLst[i]) < len(newLst[j]) || (len(newLst[i]) == len(newLst[j]) && newLst[i] < newLst[j])
    })
    return newLst
}


func list_sort(lst []string) []string {
    newLst := make([]string, 0)
    for _, v := range lst {
        if len(v)%2 != 0 {
            continue
        }
        newLst = append(newLst, v)
    }
    sort.Slice(newLst, func(i int, j int) bool {
        return len(newLst[i]) < len(newLst[j]) || (len(newLst[i]) == len(new