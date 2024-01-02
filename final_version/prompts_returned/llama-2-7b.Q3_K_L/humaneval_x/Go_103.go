import (
    "fmt"
    "math"
)

// You are given two positive integers n and m, and your task is to compute the
// average of the integers from n through m (including n and m).
// Round the answer to the nearest integer and convert that to binary.
// If n is greater than m, return -1.
// Example:
// RoundedAvg(1, 5) => "0b11"
// RoundedAvg(7, 5) => -1
// RoundedAvg(10, 20) => "0b1111"
// RoundedAvg(20, 33) => "0b11010"
func RoundedAvg(n, m int) interface{} {
    if n > m {
        return -1
    } else {
        s := formatBinary(int64(m-1)) + "10" + formatBinary(int64((n+m)/2))
        // fmt.Println("RoundedAvg", s)
        if len(s) >= 5 {
            return "" + (formatBinary(s[len(s)-1]) - '0')
        } else {
            return s[:5] + "0"
        }
    }
}

func formatBinary(n int64) string {
    ret := fmt.Sprintf("%b", n)
    if len(ret) >= 2 && ret[len(ret)-1] == '0' {
        return ret[:len(ret)-1] + "1"
    } else if len(ret) > 3 && ret[len(ret)-1:len(ret)] == "10" {
        return ret[:len(ret)-2+1:-1] + "1"
    } else {
        return ret
    }
}