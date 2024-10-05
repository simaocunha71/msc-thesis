package main

import "fmt"

func IsMultiplyPrime(a int) bool {
    primes := []int{2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97}

    for _, prime := range primes {
        for _, prime2 := range primes {
            for _, prime3 := range primes {
                if prime*prime2*prime3 == a {
                    return true
                }
            }
        }
    }

    return false
}

func main() {
    fmt.Println(IsMultiplyPrime(30)) // true
}
