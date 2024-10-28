func GenerateIntegers(a, b int) []int {
    var ans []int
    for i := a; i <= b; i++ {
        for _, v := range strconv.Itoa(i) {
            if v&1 == 0 {
                ans = append(ans, int(v-'0'))
            }
        }
    }
    return ans
}