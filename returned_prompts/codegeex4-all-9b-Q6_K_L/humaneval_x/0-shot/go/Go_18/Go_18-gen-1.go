package main

import "fmt"

func HowManyTimes(str string, substring string) int {
    count := 0
    for {
        index := indexSubstring(str, substring)
        if index == -1 {
            break
        }
        count++
        str = str[index+len(substring):]
    }
    return count
}

func indexSubstring(str string, substring string) int {
    for i, c := range str {
        if i+len(substring) > len(str) {
            break
        }
        if c == substring[0] {
            if str[i:i+len(substring)] == substring {
                return i
            }
        }
    }
    return -1
}

func main() {
    fmt.Println(HowManyTimes("", "a")) // 0
    fmt.Println(HowManyTimes("aaa", "a")) // 3
    fmt.Println(HowManyTimes("aaaa", "aa")) // 3
}