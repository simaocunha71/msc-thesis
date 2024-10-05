func GenerateIntegers(a, b int) []int {
    if a > b {
        a, b = b, a
    }
    res := []int{}
    for i := a; i <= b; i++ {
        if i%2 == 0 {
            res = append(res, i)
        }
    }
    return res
}