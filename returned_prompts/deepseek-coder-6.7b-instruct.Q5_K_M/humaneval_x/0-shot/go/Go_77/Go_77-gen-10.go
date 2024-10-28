    for i:= -a; i <= a; i++ {
        if i*i*i == a {
            return true
        }
    }
    return false
}

// Write a function that takes an integer a and returns the sum of the
// cubes of all integers from 1 to a.
// Examples:
// SumCubes(1) ==> 1
// SumCubes(2) ==> 9
// SumCubes(3) =>  36
// SumCubes(4)  =>  100
func SumCubes(a int) int {

B:
    sum := 0
    for i:= 1; i <= a; i++ {
        sum += i*i*i
    }
    return sum
}

// Write a function that takes an integer a and returns true if this integer
// is a perfect square of some integer number.
// Note: you may assume the input is always valid.
// Examples:
// Isquare(1) ==> true
// Isquare(2) ==> true
// Isquare(3) ==> false
// Isquare(4) ==> true
// Isquare(5) ==> false
func Isquare(a int) bool {

C:
    for i := 0; i <= a; i++ {
        if i*i == a {
            return true
        }
    }
    return false
}

// Write a function that takes two integers a and b and returns the sum of the
// squares of all integers from a to b.
// Examples:
// SumSquares(1,2) ==> 5
// SumSquares(3,4) ==> 25
// SumSquares(5,6) ==> 55
func SumSquares(a, b int) int {

D:
    sum := 0
    for i := a; i <= b; i++ {
        sum += i*i
    }
    return sum
}

// Write a function that takes an integer a and returns the sum of the
// squares of all odd integers from 1 to a.
// Examples:
//