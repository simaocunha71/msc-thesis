
// Circular shift the digits of the integer x, shift the digits right by shift
// and return the result as a string.
// If shift > number of digits, return digits reversed.
// >>> CircularShift(12, 1)
// "21"
// >>> CircularShift(12, 2)
// "12"
func CircularShift(x int,shift int) string {
    var s = strconv.Itoa(x)
    var result = ""
    var len = len(s)
    if shift > len {
        shift = len
    }
    for i:=0; i < len; i++ {
        if i+shift < len {
            result += string(s[i+shift])
        } else {
            result += string(s[i+shift-len])
        }
    }
    return string(result[len-shift:])
}

// Circular shift the digits of the integer x, shift the digits right by shift
// and return the result as a string.
// If shift > number of digits, return digits reversed.
// >>> CircularShift(12, 1)
// "21"
// >>> CircularShift(12, 2)
// "12"
func CircularShift(x int,shift int) string {
    var s = strconv.Itoa(x)
    var result = ""
    var len = len(s)
    if shift > len {
        shift = len
    }
    for i:=0; i < len; i++ {
        if i+shift < len {
            result += string(s[i+shift])
        } else {
            result += string(s[i+shift-len])
        }
    }
    return string(result[len-shift:])
}

// Circular shift the digits of the integer x, shift the digits right by shift
// and return the result as a string.
// If shift > number of digits, return digits reversed.
// >>> CircularShift(12, 1)
// "21"
// >>> CircularShift(12, 2)
// "12"
func CircularShift(