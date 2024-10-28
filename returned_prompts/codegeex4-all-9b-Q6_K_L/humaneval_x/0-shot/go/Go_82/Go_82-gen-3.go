package main

import (
	"fmt"
	"math"
)

func isPrime(n int) bool {
	if n <= 1 {
		return false
	}
	if n <= 3 {
		return true
	}
	if n%2 == 0 || n%3 == 0 {
		return false
	}
	i := 5
	for i*i <= n {
		if n%i == 0 || n%(i+2) == 0 {
			return false
		}
		i += 6
	}
	return true
}

func PrimeLength(s string) bool {
	return isPrime(len(s))
}

func main() {
	fmt.Println(PrimeLength("Hello"))         // true
	fmt.Println(PrimeLength("abcdcba"))       // true
	fmt.Println(PrimeLength("kittens"))       // true
	fmt.Println(PrimeLength("orange"))        // false
	fmt.Println(PrimeLength("a"))             // true
	fmt.Println(PrimeLength("ab"))            // true
	fmt.Println(PrimeLength("abc"))           // true
	fmt.Println(PrimeLength("abcd"))          // true
	fmt.Println(PrimeLength("abcde"))         // true
	fmt.Println(PrimeLength("abcdef"))        // false
	fmt.Println(PrimeLength("abcdefg"))       // false
	fmt.Println(PrimeLength("abcdefgh"))      // false
	fmt.Println(PrimeLength("abcdefghi"))     // false
	fmt.Println(PrimeLength("abcdefghij"))    // false
	fmt.Println(PrimeLength("abcdefghijk"))   // false
	fmt.Println(PrimeLength("abcdefghijkl"))  // false
	fmt.Println(PrimeLength("abcdefghijklm")) // false
	fmt.Println(PrimeLength("abcdefghijklmn"))// false
	fmt.Println(PrimeLength("abcdefghijklmno"))// false
	fmt.Println(PrimeLength("abcdefghijklmnop"))// false
	fmt.Println(PrimeLength("abcdefghijklmnopq"))// false
	fmt.Println(PrimeLength("abcdefghijklmnopqr"))// false
	fmt.Println(PrimeLength("abcdefghijklmnopqrs"))// false
	fmt.Println(PrimeLength("abcdefghijklmnopqrst"))// false
	fmt.Println(PrimeLength("abcdefghijklmnopqrstu"))// false
	fmt.Println(PrimeLength("abcdefghijklmnopqrstuv"))// false
	fmt.Println(PrimeLength("abcdefghijklmnopqrstuvw"))// false
	fmt.Println(PrimeLength("abcdefghijklmnopqrstuvwx"))// false
	fmt.Println(PrimeLength("abcdefghijklmnopqrstuvwx"))// false
	fmt.Println(PrimeLength("abcdefghijklmnopqrstuvwxy"))// false
	fmt.Println