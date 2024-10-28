
// convert int to string
    str := strconv.Itoa(x)

B:

    if shift > len(str){
        // if shift > number of digits, return digits reversed.
        str = Reverse(str)
    } else {
        // Circular shift the digits of the integer x, shift the digits right by shift
        str = str[len(str)-shift:] + str[0:len(str)-shift]
    }

C:

    return str
}

func Reverse(s string) string {
    runes := []rune(s)
    for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
        runes[i], runes[j] = runes[j], runes[i]
    }
    return string(runes)
}

func main() {
    fmt.Println(CircularShift(12, 1))
    fmt.Println(CircularShift(12, 2))
    fmt.Println(CircularShift(12345, 3))
    fmt.Println(CircularShift(12345, 6))
}




















































































































































































































