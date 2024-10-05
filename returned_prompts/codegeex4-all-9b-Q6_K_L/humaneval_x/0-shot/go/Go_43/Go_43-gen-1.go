import "sort"

func PairsSumToZero(l []int) bool {
    sort.Ints(l)
    for i := 0; i < len(l)-1; i++ {
        for j := i + 1; j < len(l); j++ {
            if l[i]+l[j] == 0 {
                return true
            }
        }
    }
    return false
}
