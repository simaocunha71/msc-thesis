func Common(l1 []int,l2 []int) []int {
    set := make(map[int]bool)
    for _, item := range l1 {
        set[item] = true
    }

    var common []int
    for _, item := range l2 {
        if set[item] {
            common = append(common, item)
            delete(set, item)
        }
    }

    sort.Ints(common)
    return common
}
