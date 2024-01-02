
// Circular shift the digits of the integer x, shift the digits right by shift
// and return the result as a string.
// If shift > number of digits, return digits reversed.
// >>> CircularShift(12, 1)
// "21"
// >>> CircularShift(12, 2)
// "12"
func CircularShift(x int,shift int) string {
    var i = 0
    var j = 0
    k := x % 10
    b := ""
    switch shift{
        case 3:
            for i < len(string(k)) {
                if (i == 2) {
                    j+= 1
                }
                b += string(k[j])
                i++
            }
            
            break
        default:
            for i < shift+len(string(k)){
                if (i == len(string(k))) {
                    j--
                }
                b += string(k[j])
                i++
            }
            break
    }
    return b
}