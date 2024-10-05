import "fmt"

func main() {
    fmt.Println(TriplesSumToZero([]int{1, 3, 5, 0}))
    fmt.Println(TriplesSumToZero([]int{1, 3, -2, 1}))
    fmt.Println(TriplesSumToZero([]int{1, 2, 3, 7}))
    fmt.Println(TriplesSumToZero([]int{2, 4, -5, 3, 9, 7}))
    fmt.Println(TriplesSumToZero([]int{1}))
}

func TriplesSumToZero(l []int) bool {
    for i := 0; i < len(l)-2; i++ {
        for j := i + 1; j < len(l)-1; j++ {
            for k := j + 1; k < len(l); k++ {
                if l[i]+l[j]+l[k] == 0 {
                    return true
                }
            }
        }
    }
    return false
}
