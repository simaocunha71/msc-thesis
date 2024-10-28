
// Circular shift the digits of the integer x, shift the digits right by shift
// and return the result as a string.
// If shift > number of digits, return digits reversed.
// >>> CircularShift(12, 1)
// "21"
// >>> CircularShift(12, 2)
// "12"
func CircularShift(x int,shift int) string {
    if shift > len(strconv.Itoa(x)) {
        return strconv.Itoa(x)[len(strconv.Itoa(x))-1:] + strconv.Itoa(x)[:len(strconv.Itoa(x))-1]
    } else {
        return strconv.Itoa(x)[shift:] + strconv.Itoa(x)[:shift]
    }
}
