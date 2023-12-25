
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
    if n <= 2 || n % 2 == 0 {
        return false
    }

    for a in range(3, n/2+1) {
        // if divisor is not the current number, then it must divide into the current number
        if n%a != 0 && a != 1 {
            // the remaining part of the division cannot be zero, so we have to check for that as well.
            // in general the remainder will be negative (which means it is actually smaller than the divisor)
            // but since here the remainder can only be positive, because otherwise we don't want to divide into n anymore...
            if !(n%a == 0 && a != 1) {
                return false
            }
        }
    }
    return true
}
