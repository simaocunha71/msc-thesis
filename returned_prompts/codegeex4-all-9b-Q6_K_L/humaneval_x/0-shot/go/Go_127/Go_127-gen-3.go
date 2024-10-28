// Write your code here
// return "NO"
// [input/output] samples:
// Intersection((1, 2), (2, 3)) ==> "NO"
// Intersection((-1, 1), (0, 4)) ==> "NO"
// Intersection((-3, -1), (-5, 5)) ==> "YES"
func Intersection(interval1 [2]int, interval2 [2]int) string {
    // Write your code here
    // return "NO"
    // [input/output] samples:
    // Intersection((1, 2), (2, 3)) ==> "NO"
    // Intersection((-1, 1), (0, 4)) ==> "NO"
    // Intersection((-3, -1), (-5, 5)) ==> "YES"
    // 1. Find the intersection of two intervals
    // 2. Check if the length of the intersection is a prime number
    // 3. Return "YES" if the length is a prime number, otherwise return "NO"
    // 4. If the two intervals don't intersect, return "NO"

    // 1. Find the intersection of two intervals
    var intersection [2]int
    if interval1[0] >= interval2[0] && interval1[0] <= interval2[1] {
        intersection[0] = interval1[0]
    } else if interval2[0] >= interval1[0] && interval2[0] <= interval1[1] {
        intersection[0] = interval2[0]
    } else {
        return "NO"
    }

    if interval1[1] >= interval2[0] && interval1[1] <= interval2[1] {
        intersection[1] = interval1[1]
    } else if interval2[1] >= interval1[0] && interval2[1] <= interval1[1] {
        intersection[1] = interval2[1]
    } else {
        return "NO"
    }

    // 2. Check if the length of the intersection is a prime number
    var length int
    if intersection[1] > intersection[0] {
        length = intersection[1] - intersection[0]
    } else {
        length = intersection[0] - intersection[1]
    }

    if length < 2 {
        return "NO"
    }

    for i := 2;