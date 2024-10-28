// Create a new struct to hold the start and end of the interval
type Interval struct {
    Start int
    End   int
}

// Create a new interval from the given interval1 and interval2
var interval Interval
interval.Start = interval1[0]
interval.End = interval2[1]

// Check if the two intervals intersect
if interval.Start > interval.End {
    return "NO"
}

// Check if the length of the intersection is a prime number
if isPrime(interval.End - interval.Start + 1) {
    return "YES"
} else {
    return "NO"
}

// Create a function to check if a number is prime
func isPrime(n int) bool {
    if n <= 1 {
        return false
    }
    for i := 2; i*i <= n; i++ {
        if n%i == 0 {
            return false
        }
    }
    return true
}