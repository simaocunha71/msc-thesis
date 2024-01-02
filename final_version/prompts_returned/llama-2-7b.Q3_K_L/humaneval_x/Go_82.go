
// Write a function that takes a string and returns true if the string
// length is a prime number or false otherwise
// Examples
// PrimeLength('Hello') == true
// PrimeLength('abcdcba') == true
// PrimeLength('kittens') == true
// PrimeLength('orange') == false
func PrimeLength(s string) bool {
    if s == "" || len(s) < 2 {
        return true
    } else {
        for i := 0; i<len(s); i++{
            var x int = int(s[i]) - 'a'
            if (x != 0 && x % 10 == 0){
                break;
            }else{}
        }
    }
}
