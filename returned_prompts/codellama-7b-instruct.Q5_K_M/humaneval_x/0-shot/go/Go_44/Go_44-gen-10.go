import (
    "strconv"
)

// Change numerical base of input number x to base.
// return string representation after the conversion.
// base numbers are less than 10.
// >>> ChangeBase(8, 3)
// '22'
// >>> ChangeBase(8, 2)
// '1000'
// >>> ChangeBase(7, 2)
// '111'
func ChangeBase(x int, base int) string {
    var res string
    for x > 0 {
        res = strconv.Itoa(x % base) + res
        x /= base
    }
    return res
}

