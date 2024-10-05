func Common(l1 []int, l2 []int) []int {
    set1 := make(map[int]bool)
    set2 := make(map[int]bool)
    var common []int

    for _, num := range l1 {
        set1[num] = true
    }

    for _, num := range l2 {
        if set1[num] {
            set2[num] = true
        }
    }

    for num := range set2 {
        common = append(common, num)
    }

    sort.Ints(common)
    return common
}
