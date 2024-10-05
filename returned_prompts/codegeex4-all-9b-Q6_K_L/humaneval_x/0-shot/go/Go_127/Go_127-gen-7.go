// 1. Sort the intervals by their start point.
// 2. Determine the intersection interval.
// 3. Calculate the length of the intersection interval.
// 4. Check if the length is a prime number.
// 5. Return "YES" if the length is prime, otherwise return "NO".

func Intersection(interval1 [2]int, interval2 [2]int) string {
    // Sort the intervals by their start point.
    if interval1[0] > interval2[0] {
        interval1, interval2 = interval2, interval1
    }

    // Determine the intersection interval.
    intersectionStart := max(interval1[0], interval2[0])
    intersectionEnd := min(interval1[1], interval2[1])

    // Calculate the length of the intersection interval.
    length := intersectionEnd - intersectionStart + 1

    // Check if the length is a prime number.
    if isPrime(length) {
        return "YES"
    } else {
        return "NO"
    }
}

// Helper function to determine if a number is prime.
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

// Helper function to get the maximum of two numbers.
func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}

// Helper function to get the minimum of two numbers.
func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}