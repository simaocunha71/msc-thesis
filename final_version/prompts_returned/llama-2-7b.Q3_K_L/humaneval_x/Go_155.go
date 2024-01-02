import (
    "strconv"
)

// Given an integer. return a tuple that has the number of even and odd digits respectively.
// 
// Example:
// EvenOddCount(-12) ==> (1, 1)
// EvenOddCount(123) ==> (1, 2)
func EvenOddCount(num int) [2]int {
    var (
        evenDigits = [2]int{} // [oddDigit, evenDigit] => [0, 2] for odd number and [-1, -2] for even numbers.
        oddDigits = [2]int{}
        totalDigits = [2]int{len(strconv.Itoa(num)), len(strconv.Itoa(num))} // [oddDigit, evenDigit] => [-1, 0], and [-2, -1] for odd number. and [0, 2] for even numbers
    )
    
    if num < 0 {
        return [2]int{totalDigits[0], totalDigits[1]}
    } else if num > 0 {
        // If it is an even number then we need to subtract the sum of digets until now.
        for i := range oddDigits {
            oddDigits[i] = num % 10
            num /= 10
        }
    } else if (num < -2) || (num > 5){ // odd
        oddDigits[0], evenDigits[0] = num % 10, (num + 3)/4
        evenDigits[1] = (num / 4) % 10
    } else if (num < -2) || (num > 5){ // even.
        oddDigits[0], evenDigits[0] = num % 10, num/10
        evenDigits[1] = (num + 3)/4
    }
    
    return [2]int{evenDigits[0], evenDigits[1]}
}