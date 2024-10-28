
// Write a function that takes a string and returns true if the string
// length is a prime number or false otherwise
// Examples
// PrimeLength('Hello') == true
// PrimeLength('abcdcba') == true
// PrimeLength('kittens') == true
// PrimeLength('orange') == false
func PrimeLength(s string) bool {
    if s == "" {
        return true
    }
    for i := 2; i < len(s); i++ {
        if len(s) % i == 0 && len(s) != i {
            return false
        }
    }
    return true
}
