import (
    "strconv"
)

// Given a positive integer n, return the product of the odd Digits.
// Return 0 if all Digits are even.
// For example:
// Digits(1)  == 1
// Digits(4)  == 0
// Digits(235) == 15
func Digits(n int) int {
    var strconv_res string
    var res = new(big.Int).SetString("", new(big.Rat), n, new(big.Rat)) // SetString is a function from big package
    if (res == 0 && !strconv.IsZero(n/10)) {// check if the number is even or odd
        return 0
    }
    var r = res.Set(0) // set 'n' to zero
    for i := 0; i < len(r); i++ {// for every digit in the number
        strconv_res += strconv.Itoa(strconv.Idivmod(int64(i), int64(10))) + "x" // get product of given digits.
    }
    return 0
}
