
    total := 0

    for _, c := range x {

B:

        if unicode.IsUpper(c) {

C:

            total += int(c)
        }
    }

    return total
}

func main() {

D:

    fmt.Println(Digitsum("")) // 0
    fmt.Println(Digitsum("abAB")) // 131
    fmt.Println(Digitsum("abcCd")) // 67
    fmt.Println(Digitsum("helloE")) // 69
    fmt.Println(Digitsum("woArBld")) // 131
    fmt.Println(Digitsum("aAaaaXa")) // 153
}


*/

// Task
// Write a function that takes a string as input and returns the sum of the upper characters only'
// ASCII codes.
// 
// Examples:
// Digitsum("") ➞ 0
// Digitsum("abAB") ➞ 131
// Digitsum("abcCd") ➞ 67
// Digitsum("helloE") ➞ 69
// Digitsum("woArBld") ➞ 131
// Digitsum("aAaaaXa") ➞ 153

// Code:

func Digitsum(x string) int  {

    total := 0

    for _, c := range x {

        if unicode.IsUpper(c) {

            total += int(c)
        }
    }

    return total
}

func main() {

    fmt.Println(Digitsum("")) // 0
    fmt.Println(Digitsum("abAB")) // 131
    fmt.Println(Digitsum("abcCd")) // 67
    fmt.Println(Digitsum("helloE")) // 69
    fmt.Println(Digitsum("woArBld")) // 131
    fmt.Println(