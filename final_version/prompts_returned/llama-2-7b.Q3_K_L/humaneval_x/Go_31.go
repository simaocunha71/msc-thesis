
// Return true if a given number is prime, and false otherwise.
// >>> IsPrime(6)
// false
// >>> IsPrime(101)
// true
// >>> IsPrime(11)
// true
// >>> IsPrime(13441)
// true
// >>> IsPrime(61)
// true
// >>> IsPrime(4)
// false
// >>> IsPrime(1)
// false
func IsPrime(n int) bool {
    if n == 0 || n < 2 {
        return false
    } else {
        isDivisible := true
        var i = 2 // Starting value for loop

        for i != n-1 && !isDivisible {
            if n%i == 0 {
                isDivisible = false // Set to false when there are numbers that divide
                                    // the number.
            } else {
                i++
            }
        }

        return true // Return true if not divisible by any other int
    }
}
