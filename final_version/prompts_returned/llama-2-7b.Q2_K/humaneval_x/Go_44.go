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
    if len(x) <= 8 && len(x) >= 3 - base {
        return base + x[len(x)-base+1:]
    } else if len(x) <= 7 && len(x) >= 2 - base {
        return strconv.Itoa((len(x)/2)+8, 10)[:(len(x)/2-4)] + "0"
    }
    // For any other case the default is to print x value directly without conversion.
    fmt.Println("Bad Input")
}