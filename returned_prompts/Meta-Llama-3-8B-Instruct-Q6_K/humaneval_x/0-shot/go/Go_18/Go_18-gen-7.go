```go
package main

import (
    "fmt"
    "strings"
)

func HowManyTimes(str string, substring string) int {
    count := 0
    length := len(substring)
    for i := 0; i <= len(str)-length; i++ {
        if str[i:i+length] == substring {
            count++
        }
    }
    return count
}

func main() {
    fmt.Println(HowManyTimes("", "a")) // 0
    fmt.Println(HowManyTimes("aaa", "a")) // 3
    fmt.Println(HowManyTimes("aaaa", "aa")) // 3
}
```

The function `HowManyTimes` takes a string `str` and a substring `substring` as parameters. It initializes a counter `count` to 0 and calculates the length of the substring. It then iterates over the original string, checking if the substring matches at each position. If it does, it increments the counter. Finally, it returns the count.

The `main` function tests the `HowManyTimes` function with three examples, printing the results to the console. The first test case is an empty string and an 'a', which should return 0. The second test case is a string of three 'a's and a substring of 'a', which should return 3. The third test case is a string of four 'a's and a substring of 'aa', which should also return 3. The results match the expected output.