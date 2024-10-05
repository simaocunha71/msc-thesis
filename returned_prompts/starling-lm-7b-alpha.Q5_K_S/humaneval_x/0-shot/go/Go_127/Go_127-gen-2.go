    if interval1[0] > interval2[1] || interval2[0] > interval1[1] {
        return "NO"
    }
    if interval1[0] > interval2[0] {
        return Intersection(interval2, interval1)
    }
    if interval1[1] < interval2[0] {
        return "NO"
    }
    return isPrime(interval1[1] - interval2[0]) ? "YES" : "NO"
}

func isPrime(n int) bool {
    for i := 2; i * i <= n; i++ {
        if n % i == 0 {
            return false
        }
    }
    return true
}

*/

// You are given two intervals,
// where each interval is a pair of integers. For example, interval = (start, end) = (1, 2).
// The given intervals are closed which means that the interval (start, end)
// includes both start and end.
// Your task is to determine whether the length of Intersection of these two
// intervals is a prime number.
// Example, the Intersection of the intervals (1, 3), (2, 4) is (2, 3)
// which its length is 1, which not a prime number.
// If the length of the Intersection is a prime number, return "YES",
// otherwise, return "NO".
// If the two intervals don't intersect, return "NO".
// 
// 
// [input/output] samples:
// Intersection((1, 2), (2, 3)) ==> "NO"
// Intersection((-1, 1), (0, 4)) ==> "NO"
// Intersection((-3, -1), (-5, 5)) ==> "YES"
func Intersection(interval1, interval2 [2]int) string {
    if interval1[0] > interval2[1] || interval2[0] > interval1[1] {
        return "NO"
    }
    if interval1[0] > interval2[0] {
        return Intersection(interval2, interval1)
    }
