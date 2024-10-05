```go
package main
import "fmt"
func HowManyTimes(str string, substring string) int {
    count := 0
    pos := 0
    for pos < len(str) {
        pos = stringIndex(str, substring, pos)
        if pos == -1 {
            break
        }
        count++
        pos++
    }
    return count
}

func stringIndex(str string, substring string, pos int) int {
    if pos >= len(str) {
        return -1
    }
    if len(substring) > len(str)-pos {
        return -1
    }
    for i := 0; i < len(substring); i++ {
        if str[pos+i] != substring[i] {
            return -1
        }
    }
    return pos
}

func main() {
    fmt.Println(HowManyTimes("", "a")) // 0
    fmt.Println(HowManyTimes("aaa", "a")) // 3
    fmt.Println(HowManyTimes("aaaa", "aa")) // 3
}
```
In the function HowManyTimes, I use a for loop to iterate over the string. For each iteration, I use the function stringIndex to find the next occurrence of the substring. The stringIndex function returns the position of the substring if found, otherwise it returns -1. If the substring is not found, the for loop breaks and the function returns the count. If the substring is found, the count is incremented and the loop continues. The stringIndex function checks if the current position is out of bounds, and if the substring is longer than the remaining string. If either condition is true, it returns -1. Otherwise, it compares each character of the substring with the corresponding character of the string, starting from the current position. If a mismatch is found, it returns -1. Otherwise, it returns the current position. The main function tests the HowManyTimes function with different inputs.