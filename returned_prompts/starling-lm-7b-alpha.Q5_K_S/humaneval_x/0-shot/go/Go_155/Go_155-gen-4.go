    var even int = 0
    var odd int = 0
    var numStr string = strconv.Itoa(num)
    var length int = len(numStr)
    for i := 0; i < length; i++ {
        if numStr[i] % 2 == 0 {
            even++
        } else {
            odd++
        }
    }
    return [2]int{even, odd}
}

The function EvenOddCount takes an integer num as an input and returns a tuple that has the number of even and odd digits respectively. The function first converts the input number to a string using the strconv.Itoa function. Then, it calculates the length of the string. Next, it iterates through each character of the string. If a character is an even number, the even counter is incremented; otherwise, the odd counter is incremented. Finally, the function returns a tuple containing the number of even and odd digits.

Here's an example of how to use the EvenOddCount function:

EvenOddCount(-12) returns (1, 1) because -12 has one even digit (2) and one odd digit (1).
EvenOddCount(123) returns (1, 2) because 123 has one even digit (2) and two odd digits (1 and 3).

Overall, the EvenOddCount function provides a convenient way to determine the number of even and odd digits in a given integer.

*/
package main

import (
    "strconv"
)

// Given an integer. return a tuple that has the number of even and odd digits respectively.
// 
// Example:
// EvenOddCount(-12) ==> (1, 1)
// EvenOddCount(123) ==> (1, 2)
func EvenOddCount(num int) [2]int {

    var even int = 0
    var odd int = 0
    var numStr string = strconv.Itoa(num)
    var length int = len(numStr)
    for i := 0; i < length; i++ {
        if numStr[i] % 2 ==