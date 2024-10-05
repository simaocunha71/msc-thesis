func Iscube(a int) bool {
    c := int(math.Ceil(math.Pow(float64(a), (1.0/3.0))))
    return a == c*c*c
}
// Test
func main() {
    println(Iscube(1))  // true
    println(Iscube(2))  // false
    println(Iscube(-1)) // true
    println(Iscube(64)) // true
    println(Iscube(0))  // true
    println(Iscube(180)) // false
}

This is a Go program that checks if a given integer is a cube of some integer number. The function `Iscube` takes an integer `a` as input and returns `true` if `a` is a cube of some integer number, and `false` otherwise.

The function first calculates the cube root of `a` using the `math.Ceil` function, which returns the smallest integer not less than the given number. It then checks if `a` is equal to the cube of this integer. If it is, the function returns `true`; otherwise, it returns `false`.

The `main` function tests the `Iscube` function with various inputs and prints the results. For example, `Iscube(1)` returns `true` because 1 is a cube of 1 (1^3 = 1), while `Iscube(2)` returns `false` because 2 is not a cube of any integer. Similarly, `Iscube(180)` returns `false` because 180 is not a cube of any integer.