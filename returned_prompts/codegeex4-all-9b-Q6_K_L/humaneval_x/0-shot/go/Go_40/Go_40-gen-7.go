import "fmt"

// TriplesSumToZero takes a list of integers as an input.
// it returns true if there are three distinct elements in the list that
// sum to zero, and false otherwise.
// 
// >>> TriplesSumToZero([1, 3, 5, 0])
// false
// >>> TriplesSumToZero([1, 3, -2, 1])
// true
// >>> TriplesSumToZero([1, 2, 3, 7])
// false
// >>> TriplesSumToZero([2, 4, -5, 3, 9, 7])
// true
// >>> TriplesSumToZero([1])
// false
func TriplesSumToZero(l []int) bool {
    // sort the list
    sort.Ints(l)

    for i := 0; i < len(l)-2; i++ {
        // use two pointers to search for the two numbers that sum to -l[i]
        left := i + 1
        right := len(l) - 1
        for left < right {
            if l[i]+l[left]+l[right] == 0 {
                return true
            } else if l[i]+l[left]+l[right] < 0 {
                left++
            } else {
                right--
            }
        }
    }
    return false
}
func main() {
    fmt.Println(TriplesSumToZero([]int{1, 3, 5, 0}))      // false
    fmt.Println(TriplesSumToZero([]int{1, 3, -2, 1}))     // true
    fmt.Println(TriplesSumToZero([]int{1, 2, 3, 7}))      // false
    fmt.Println(TriplesSumToZero([]int{2, 4, -5, 3, 9, 7})) // true
    fmt.Println(TriplesSumToZero([]int{1}))                // false
}