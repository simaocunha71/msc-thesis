import "sort"

func TriplesSumToZero(l []int) bool {
    sort.Ints(l)
    for i := range l {
        if i > 0 && l[i] == l[i-1] {
            continue
        }
        for j, k := i+1, len(l)-1; j < k; {
            if l[i]+l[j]+l[k] == 0 {
                return true
            } else if l[i]+l[j]+l[k] < 0 {
                j++
            } else {
                k--
            }
        }
    }
    return false
}
