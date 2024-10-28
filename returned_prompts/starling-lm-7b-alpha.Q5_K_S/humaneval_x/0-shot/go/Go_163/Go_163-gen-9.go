
func GenerateIntegers(a, b int) []int {
    res := make([]int, 0)
    for i := a; i <= b; i++ {
        str := strconv.Itoa(i)
        for _, v := range str {
            if v%2 == 0 {
                res = append(res, v)
            }
        }
    }
    sort.Ints(res)
    return res
}






























// Given two positive integers a and b, return the even digits between a
// and b, in ascending order.
// 
// For example:
// GenerateIntegers(2, 8) => [2, 4, 6, 8]
// GenerateIntegers(8, 2) => [2, 4, 6, 8]
// GenerateIntegers(10, 14) => []
func GenerateIntegers(a, b int) []int {
    res := make([]int, 0)
    for i := a; i <= b; i++ {
        str := strconv.Itoa(i)
        for _, v := range str {
            if v%2 == 0 {
                res = append(res, v)
            }
        }
    }
    sort.Ints(res)
    return res
}





































































































































































