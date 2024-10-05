import (
    "fmt"
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

    // Convert base to string.
    baseStr := strconv.Itoa(base)

    // Convert x to string.
    xStr := strconv.Itoa(x)

    // Convert xStr from base 10 to base baseStr.
    var result string
    result, err := strconv.ParseInt(xStr, 10, 64)
    if err != nil {
        fmt.Println(err)
        return ""
    }
    resultStr := strconv.FormatInt(result, base)

    return resultStr
}
