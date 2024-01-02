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
    x = strconv.Itoa(x)
    if x == "" || len(strconv.Itoa(base)) < 3 {
        return strconv.Itoa(x)
    }
    out := make([]rune, base+1)
    i := base - 2
    for j := 0; j < i; j++ {
        out[j] = strconv.Itoa(base)[j].Rune()
    }
    out[i] = strconv.Itoa(x)[len(strconv.Itoa(x)) - base]
    return string(out)
}