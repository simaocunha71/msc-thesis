//     count_even, count_odd := 0, 0
//     for i := 1; i <= n; i++ {
//         if isPalindrome(i) {
//             if i%2 == 0 {
//                 count_even++
//             } else {
//                 count_odd++
//             }
//         }
//     }
//     return [2]int{count_even, count_odd}
// }

func isPalindrome(n int) bool {
    str := strconv.Itoa(n)
    for i := 0; i < len(str)/2; i++ {
        if str[i] != str[len(str)-i-1] {
            return false
        }
    }
    return true
}

import (
	"testing"
	"github.com/stretchr/testify/assert"
)

func TestEvenOddPalindrome(t *testing.T) {
	assert := assert.New(t)
	assert.Equal([2]int{4, 6}, EvenOddPalindrome(12), "they should be equal")
	assert.Equal([2]int{1, 2}, EvenOddPalindrome(3), "they should be equal")
}

// Your code here along with explanation
func EvenOddPalindrome(n int) [2]int {

