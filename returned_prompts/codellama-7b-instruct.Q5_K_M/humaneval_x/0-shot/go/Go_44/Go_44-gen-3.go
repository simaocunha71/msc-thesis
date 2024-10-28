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
    // convert number to string
    s := strconv.Itoa(x)
    // convert string to rune slice
    r := []rune(s)
    // reverse rune slice
    for i, j := 0, len(r)-1; i < j; i, j = i+1, j-1 {
        r[i], r[j] = r[j], r[i]
    }
    // convert rune slice back to string
    s = string(r)
    // convert string to base
    ans, _ := strconv.ParseInt(s, base, 64)
    // convert to string
    return strconv.Itoa(int(ans))
}

