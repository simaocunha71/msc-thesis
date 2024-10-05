import (
    "math"
    "strconv"
)

// Write a function CountNums which takes an array of integers and returns
// the number of elements which has a sum of digits > 0.
// If a number is negative, then its first signed digit will be negative:
// e.g. -123 has signed digits -1, 2, and 3.
// >>> CountNums([]) == 0
// >>> CountNums([-1, 11, -11]) == 1
// >>> CountNums([1, 1, 2]) == 3
func CountNums(arr []int) int {
    count := 0
    for _, n := range arr {
        if n < 0 {
            n = -n
        }
        sum := 0
        for n > 0 {
            sum += n % 10
            n /= 10
        }
        if sum > 0 {
            count++
        }
    }
    return count
}

// Another solution:
func CountNums(arr []int) int {
    count := 0
    for _, n := range arr {
        if n < 0 {
            n = -n
        }
        count += n > 0
    }
    return count
}

// Yet another solution:
func CountNums(arr []int) int {
    count := 0
    for _, n := range arr {
        if n < 0 {
            n = -n
        }
        if n > 0 {
            count++
        }
    }
    return count
}

// Yet another solution:
func CountNums(arr []int) int {
    count := 0
    for _, n := range arr {
        if n < 0 {
            n = -n
        }
        count += n/10 > 0
    }
    return count
}

// Yet another solution:
func CountNums(arr []int) int {
    count := 0
    for _, n := range arr {
        if n < 0 {
            n = -n
        }
        count += n > 0