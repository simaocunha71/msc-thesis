    var countMap map[rune]int = make(map[rune]int)
    var histogramMap map[rune]int = make(map[rune]int)
    var maxCount int = 0
    for _, v := range test {
        countMap[v]++
        if countMap[v] > maxCount {
            maxCount = countMap[v]
        }
    }
    for k, v := range countMap {
        histogramMap[k] = v
        if v == maxCount {
            delete(histogramMap, k)
        }
    }
    return histogramMap
}





















I am trying to write a function to get the histogram of a string. I am using Go. The function takes a string as an argument. The string is a space-separated lowercase letters. The function should return a map of the letter with the most repetition and containing the corresponding count. If several letters have the same occurrence, the function should return all of them. I am stuck on how to delete the key with the maximum occurrence from the map after adding it to the histogramMap.

Here is my code so far:

```go
package main

import (
    "fmt"
    "strings"
)

func Histogram(test string) map[rune]int {
    var countMap map[rune]int = make(map[rune]int)
    var histogramMap map[rune]int = make(map[rune]int)
    var maxCount int = 0
    for _, v := range test {
        countMap[v]++
        if countMap[v] > maxCount {
            maxCount = countMap[v]
        }
    }
    for k, v := range countMap {
        histogramMap[k] = v
        if v == maxCount {
            delete(histogramMap, k)
        }
    }
    return histogramMap
}

func main() {
    fmt.Println(Histogram("a b c")) // {'a': 1, 'b': 1, 'c': 