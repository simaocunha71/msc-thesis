
// Task
// Write a function that takes a string as input and returns the sum of the upper characters only'
// ASCII codes.
// 
// Examples:
// Digitsum("") => 0
// Digitsum("abAB") => 131
// Digitsum("abcCd") => 67
// Digitsum("helloE") => 69
// Digitsum("woArBld") => 131
// Digitsum("aAaaaXa") => 153
func Digitsum(x string) int {
    var a = ""
    for i := range x {
        if(i == len(x)-1){ continue }
        a += string(tolower(x[i]))
    }
    return len(a) + int64(len(x)) * 256 / byteCount
}
