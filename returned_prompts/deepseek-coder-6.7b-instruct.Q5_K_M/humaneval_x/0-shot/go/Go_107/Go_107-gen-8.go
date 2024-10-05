    isPalindrome := func(num int) bool {
        str := strconv.Itoa(num)
        for i := 0; i < len(str)/2; i++ {
            if str[i] != str[len(str)-1-i] {
                return false
            }
        }
        return true
    }

    even, odd := 0, 0
    for i := 1; i <= n; i++ {
        if isPalindrome(i) {
            if i%2 == 0 {
                even++
            } else {
                odd++
            }
        }
    }
    return [2]int{even, odd}
}

In the code above, we first create a function isPalindrome to check if a number is a palindrome or not. We then iterate from 1 to n and for every number we check if it's a palindrome. If it's a palindrome, we then check if it's even or odd and increment the respective counter. Finally we return the count of even and odd palindromes.

This code runs in O(n*k) time where n is the input number and k is the number of digits in n. This is because for each number from 1 to n we are checking if it's a palindrome which takes O(k) time.
*/

package main

import (
	"fmt"
)

func EvenOddPalindrome(n int) [2]int {
	isPalindrome := func(num int) bool {
		str := fmt.Sprintf("%d", num)
		for i := 0; i < len(str)/2; i++ {
			if str[i] != str[len(str)-1-i] {
				return false
			}
		}
		return true
	}

	even, odd := 0, 0
	for i := 1; i <= n; i++ {
		if isPalindrome(i) {
			if i%2 == 0 {
				even++
			} else {
				odd