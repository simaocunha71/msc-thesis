func GenerateIntegers(a, b int) []int {
    var ret []int
    for i := a; i <= b; i++ {
        if i%2 == 0 {
            ret = append(ret, i)
        }
    }
    return ret
}

func GenerateIntegers(a, b int) []int {
    var ret []int
    for i := a; i <= b; i++ {
        for _, j := range strconv.Itoa(i) {
            if j%2 == 0 {
                ret = append(ret, i)
                break
            }
        }
    }
    return ret
}