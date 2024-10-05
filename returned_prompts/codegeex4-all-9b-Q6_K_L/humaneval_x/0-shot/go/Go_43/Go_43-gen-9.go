func PairsSumToZero(l []int) bool {
    for i, a := range l {
        for j, b := range l {
            if i != j && a+b == 0 {
                return true
            }
        }
    }
    return false
}
