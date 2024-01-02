
// Return list with elements incremented by 1.
// >>> IncrList([1, 2, 3])
// [2, 3, 4]
// >>> IncrList([5, 3, 5, 2, 3, 3, 9, 0, 123])
// [6, 4, 6, 3, 4, 4, 10, 1, 124]
func IncrList(l []int) []int {
    var (
        l = append([]int{}, l...)
        // copy slices and increment each element
        o = make([]int, len(l))

        n = 0
        for i := range l {
            o[n] = l[i]+1
            n++
        }
    )

    return o
}