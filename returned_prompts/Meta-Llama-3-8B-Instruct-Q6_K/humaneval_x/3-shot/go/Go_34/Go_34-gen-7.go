    m := make(map[int]bool)
    list := []int{}
    for _, v := range l {
        if _, value := m[v]; !value {
            m[v] = true
            list = append(list, v)
        }
    }
    sort.Ints(list)
    return list
}  //or using sort package
func Unique(l []int) []int {
    sort.Uniq(l)
    return l
}  //Note: sort.Uniq is only available in go 1.7 and later versions. For earlier versions, you should use the above solution.