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

    if a == 0 {
        return true
    }

    for i := 1; i < a; i++ {
        if math.Pow(float64(i), 3) == float64(a) {
            return true
        }
    }

    return false
}

func TestIscube(t *testing.T) {
    tests := []struct {
        a int
        expect bool
    }{
        {1, true},
        {2, false},
        {-1, true},
        {64, true},
        {0, true},
        {180, false},
    }

    for _, test := range tests {
        result := Iscube(test.a)
        if result != test.expect {
            t.Errorf("Iscube(%d) == %t, expected %t", test.a, result, test.expect)
        }
    }
}

