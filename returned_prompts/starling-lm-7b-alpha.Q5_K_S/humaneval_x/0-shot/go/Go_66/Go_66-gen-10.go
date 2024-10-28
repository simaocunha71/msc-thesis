
    ret := 0
    for _, r := range x {
        if r >= 'A' && r <= 'Z' {
            ret += int(r) - int('A') + 1
        }
    }
    return ret
}

// Time complexity: O(n)
// Space complexity: O(1)

// Reference:
// https://stackoverflow.com/questions/10891753/convert-upper-case-to-lower-case-in-go

*/

package main

import "fmt"

func main() {
    fmt.Println(Digitsum("")) // => 0
    fmt.Println(Digitsum("abAB")) // => 131
    fmt.Println(Digitsum("abcCd")) // => 67
    fmt.Println(Digitsum("helloE")) // => 69
    fmt.Println(Digitsum("woArBld")) // => 131
    fmt.Println(Digitsum("aAaaaXa")) // => 153
}

```
