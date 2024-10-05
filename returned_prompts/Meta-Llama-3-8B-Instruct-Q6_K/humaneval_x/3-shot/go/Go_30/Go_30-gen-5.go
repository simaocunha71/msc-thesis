    var result []int
    for _, i := range l {
        if i > 0 {
            result = append(result, i)
        }
    }
    return result
} // Or using filter function
func GetPositive(l []int) []int {
    return Filter(l, func(i int) bool {
        return i > 0
    })
}
func Filter(data []int, predicate func(int) bool) []int {
    var result []int
    for _, item := range data {
        if predicate(item) {
            result = append(result, item)
        }
    }
    return result
}