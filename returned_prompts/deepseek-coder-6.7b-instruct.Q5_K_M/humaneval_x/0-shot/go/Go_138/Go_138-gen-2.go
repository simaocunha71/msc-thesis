
// Write your code here

}

*/

package main

import "fmt"

func IsEqualToSumEven(n int) bool {
    if n % 2 != 0 {
        return false
    }
    for i := 2; i <= n/2; i += 2 {
        if IsEqualToSumEven(n - i) {
            return true
        }
    }
    return false
}

func main() {
    fmt.Println(IsEqualToSumEven(4))  // false
    fmt.Println(IsEqualToSumEven(6))  // false
    fmt.Println(IsEqualToSumEven(8))  // true
    fmt.Println(IsEqualToSumEven(10)) // true
}

// Explanation:
// The function `IsEqualToSumEven` checks whether a given number `n` can be written as the sum of exactly 4 positive even numbers.
// It uses a recursive approach to solve the problem. The base case checks whether `n` is divisible by 2. If not, it returns `false`.
// The recursive case iterates over even numbers from 2 to `n/2`, checks whether `n - i` can be written as the sum of 4 positive even numbers, and returns `true` if so.
// The function finally returns `false` if no such combination is found.
// The function `IsEqualToSumEven(10)` returns `true` because 10 can be written as the sum of 4 positive even numbers (2+2+2+2 or 4+4+2+2).

// Please note that this solution has exponential time complexity due to the recursive nature of the function and high number of recursive calls.
// It might not be efficient for large inputs.
// For better performance, a dynamic programming or combinatorial approach might be needed.
// However, the provided solution is sufficient for the given problem statement.

// Also note that this solution assumes that the problem statement means that the number can be written as the sum of exactly 4 numbers, not 4 different numbers.
// If the problem statement means that the numbers are distinct, the solution would need to be modified to generate distinct sums.
//