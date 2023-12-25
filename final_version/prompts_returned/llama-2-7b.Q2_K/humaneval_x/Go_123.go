import (
    "sort"
)

// Given a positive integer n, return a sorted list that has the odd numbers in collatz sequence.
// 
// The Collatz conjecture is a conjecture in mathematics that concerns a sequence defined
// as follows: start with any positive integer n. Then each term is obtained from the
// previous term as follows: if the previous term is even, the next term is one half of
// the previous term. If the previous term is odd, the next term is 3 times the previous
// term plus 1. The conjecture is that no matter what value of n, the sequence will always reach 1.
// 
// Note:
// 1. Collatz(1) is [1].
// 2. returned list sorted in increasing order.
// 
// For example:
// GetOddCollatz(5) returns [1, 5] # The collatz sequence for 5 is [5, 16, 8, 4, 2, 1], so the odd numbers are only 1, and 5.
func GetOddCollatz(n int) []int {
    var (
        list []int
        index int
        oddMap map[int]bool
    )
    
    for i := 2; i < n+1; i++ {
        if oddMap[i%2] == false && i % 2 != 0{
            list = append(list, i)
            oddMap[i%2] = true // odd numbers are in the map.
        }
    }
    
    // sort() in golang is stable by default
    sort.SliceStable(list, func (x, y int) bool { return list[x] < list[y] })
    
    for _, v := range list {
        fmt.Printf("(%d), ", v)
        
        if v == n-1 && index != 0 {
            fmt.Println("\n", index, " -> ", 1-index)
            break
        } else {
            index++
        }    
    }
    
    return list // in golang the var is a global variable, it can be used by all functions in all packages. You only need to declare