
    // Your code goes here
    var start int = max(interval1[0], interval2[0])
    var end int = min(interval1[1], interval2[1])
    var length int = end - start + 1

B:

    if length <= 1 {
        return "NO"
    }

C:

    for i := 2; i*i <= length; i++ {
        if length%i == 0 {
            return "NO"
        }
    }

D:

    return "YES"

}

func max(x, y int) int {
    if x > y {
        return x
    }
    return y
}

func min(x, y int) int {
    if x < y {
        return x
    }
    return y
}

// Check your code
// The function Intersection() takes as input two intervals and returns "YES"
// if the length of the intersection is a prime number, "NO" otherwise.
// The function max() and min() are helper functions that return the maximum
// and minimum of two numbers, respectively.
// The function Intersection() works by first computing the start and end points
// of the intersection. It then computes the length of the intersection by
// subtracting the start from the end and adding 1 (since the start and end
// are included in the interval). If the length is less than or equal to 1,
// it returns "NO". Otherwise, it checks if the length is a prime number by
// iterating from 2 to the square root of the length and checking if the
// length is divisible by any of these numbers. If it is, it returns "NO".
// Otherwise, it returns "YES".
// Note: This code assumes that the input intervals are well-formed, i.e.,
// the start is less than or equal to the end. If this is not the case,
// the code may not behave as expected.
// Note: The code uses integer division to check for prime numbers. If the
// length of the intersection is not a prime number, it will return "NO",
// even if the intersection has a length of 1. This is because in Go,
// integer division