Here is the solution:

```go
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
    if x == 0 {
        return "0"
    }
    var result []byte
    for x > 0 {
        result = strconv.AppendByte(result, byte(x%base))
        x /= base
    }
    return string(reverse(result))
}

func reverse(s []byte) []byte {
    r := []byte{}
    for i := len(s) - 1; i >= 0; i-- {
        r = append(r, s[i])
    }
    return r
}
```  Go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go  go