
func isMultiplyPrime(a int) bool {
    primeNums := []int{2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97}
    for _, prime := range primeNums {
        if a%prime == 0 {
            return true
        }
    }
    return false
}

func IsMultiplyPrime(a int) bool {
    for i := 1; i < a; i++ {
        if a%i == 0 && !isMultiplyPrime(i) {
            return false
        }
    }
    return true
}

In the function above, first, we have a slice called primeNums which contains all prime numbers below 100. Then, we iterate through every prime number in the slice and check if the given number (a) is divisible by the prime number. If it is divisible, we return true.

The function isMultiplyPrime checks if the given number (a) is the multiplication of three prime numbers. We iterate through every prime number from 2 to a-1. If a is divisible by i and i is not a prime number, then we return false. If we finish the loop without returning false, it means that a is the multiplication of three prime numbers, and we return true.

In the main function, we first call the isMultiplyPrime function to check if the given number is the multiplication of three prime numbers. If it returns true, we print "true". Otherwise, we print "false".

*/
package main

import "fmt"

func main() {
    a := 30
    fmt.Println(isMultiplyPrime(a))
}

func isMultiplyPrime(a int) bool {
    primeNums := []int{2, 3, 5, 7, 11, 1