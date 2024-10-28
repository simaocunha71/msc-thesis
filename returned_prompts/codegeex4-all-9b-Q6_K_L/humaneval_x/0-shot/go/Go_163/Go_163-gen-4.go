func GenerateIntegers(a, b int) []int {
    min, max := a, b
    if a > b {
        min, max = b, a
    }
    res := []int{}
    for i := min; i <= max; i++ {
        for _, v := range strconv.Itoa(i) {
            if v&1 == 0 {
                res = append(res, int(v-'0'))
            }
        }
    }
    return res
}