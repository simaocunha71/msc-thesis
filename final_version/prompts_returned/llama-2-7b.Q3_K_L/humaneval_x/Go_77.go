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
    if a < 0 || a == 0 {
        return true;
    } else if a > 0 {
        var n1,n2,n3,sum float64 = 0.0
        for i := 0; i <= math.MaxInt32(); i++ {
            sum += math.Pow(a*i, 2)
            if sum >= 576 {
                return true;
            } else if sum == 1825 {
                break;
            }
        }
    }
    return false;
}
