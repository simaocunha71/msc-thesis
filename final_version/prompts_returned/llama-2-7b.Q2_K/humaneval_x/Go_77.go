import (
    "math"
)

// Write a function that takes an integer a and returns true
// if this ingeger is a cube of some integer number.
// Note: you may assume the input is always valid.
// Examples:
// Iscube(1) ==> true
// Iscube(2) ==> false
// Iscube(-1) ==> true
// Iscube(64) ==> true
// Iscube(0) ==> true
// Iscube(180) ==> false
func Iscube(a int) bool {
    if a == 0 || a == -1 {
        return a != -1 && (a + 2 * int64(math.Sqrt(-float32(1))) * math.Pow(int64(1), float64(3)) == 0) // (a < 0 && (Math.Pow(int, float) == 0) || Math.Abs(a) == Abs)
    } else {
        return false
    }
}
