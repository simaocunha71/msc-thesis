func Common(l1 []int, l2 []int) []int {
    var common []int
    for _, v1 := range l1 {
        for _, v2 := range l2 {
            if v1 == v2 && !contains(common, v1) {
                common = append(common, v1)
            }
        }
    }
    sort.Ints(common)
    return common
}

func contains(arr []int, x int) bool {
    for _, v := range arr {
        if v == x {
            return true
        }
    }
    return false
}

