
// Return maximum element in the list.
// >>> MaxElement([1, 2, 3])
// 3
// >>> MaxElement([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
// 123
func MaxElement(l []int) int {
    if len(l) == 0 {
        return 0
    }
    m := l[0]
    for _, v := range l[1:] {
        if v > m {
            m = v
        }
    }
    return m
}
