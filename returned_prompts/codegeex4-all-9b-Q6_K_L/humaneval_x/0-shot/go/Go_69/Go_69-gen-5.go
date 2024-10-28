func Search(lst []int) int {
    m := map[int]int{}
    for _, v := range lst {
        m[v]++
    }
    max := -1
    for k, v := range m {
        if v >= k && k > max {
            max = k
        }
    }
    return max
}