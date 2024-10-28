func Unique(l []int) []int {
    m := make(map[int]bool)
    for _, item := range l {
        if _, ok := m[item]; !ok {
            m[item] = true
        }
    }
    result := make([]int, 0, len(m))
    for key := range m {
        result = append(result, key)
    }

    sort.Ints(result)
    return result
}