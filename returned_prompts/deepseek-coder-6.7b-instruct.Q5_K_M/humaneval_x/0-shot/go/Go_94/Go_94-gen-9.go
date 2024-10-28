    var max int
    max = -1
    for _, num := range lst {
        if num > max {
            max = num
        }
    }

B:
    for i := max; i >= 2; i-- {
        if isPrime(i) {
            return sumOfDigits(i)
        }
    }

    return 0
}

func isPrime(n int) bool {
    for i := 2; i <= int(math.Sqrt(float64(n))); i++ {
        if n%i == 0 {
            return false
        }
    }
    return n > 1
}

func sumOfDigits(n int) int {
    sum := 0
    for n != 0 {
        sum += n % 10
        n /= 10
    }
    return sum
}

Here are the steps you can follow to solve this problem:
1) Find the largest number in the list.
2) Start from this number and go down to 2. Check if each number is a prime number.
3) If you find a prime number, calculate the sum of its digits and return this sum.
4) If you do not find a prime number, return 0. 

isPrime function checks if a number is prime by checking if it can be divided by any number up to its square root.
sumOfDigits function calculates the sum of the digits of a number.
*/

package main

import (
	"fmt"
)

func main() {
	fmt.Println(Skjkasdkd([]int{0, 3, 2, 1, 3, 5, 7, 4, 5, 5, 5, 2, 181, 32, 4, 32, 3, 2, 32, 324, 4, 3}))
	fmt.Println(Skjkasdkd([]int{1, 0, 1, 8, 2, 4597, 2, 1, 3, 40, 1, 2, 1,