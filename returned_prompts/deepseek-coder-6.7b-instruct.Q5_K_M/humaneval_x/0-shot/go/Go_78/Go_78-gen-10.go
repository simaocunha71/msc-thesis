
    primes := []rune{'2', '3', '5', '7', 'B', 'D'}
    count := 0
    for _, v := range num {
        for _, p := range primes {
            if v == p {
                count++
                break
            }
        }
    }
    return count
}

// You have been tasked to write a function that receives
// a hexadecimal number as a string and counts the number of hexadecimal
// digits that are primes  (prime number, or a prime, is a natural number
// greater than 1 that is not a product of two smaller natural numbers).
// Hexadecimal digits are 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F.
// Prime numbers are 2, 3, 5, 7, 11, 13, 17,...
// So you have to determine a number of the following digits: 2, 3, 5, 7,
// B  (=decimal 11), D  (=decimal 13).
// Note: you may assume the input is always correct or empty string,
// and symbols A,B,C,D,E,F are always uppercase.
// Examples:
// For num 
// the output should be .
// For num 
// the output should be .
// For num 
// the output should be .
// For num 
// the output should be .
// For num 
// the output should be .

package main

import "fmt"

func main() {

    fmt.Println(HexKey("AB")) // 1
    fmt.Println(HexKey("1077E")) // 2
    fmt.Println(HexKey("ABED1A33")) // 4
    fmt.Println(HexKey("123456789ABCDEF0")) // 6
    fmt.Println(HexKey("2020")) // 2

}

