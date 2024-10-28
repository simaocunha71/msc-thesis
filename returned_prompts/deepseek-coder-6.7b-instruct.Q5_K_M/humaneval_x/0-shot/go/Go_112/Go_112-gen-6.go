  str := strings.Builder{}

  for _, v := range s {
    if !strings.ContainsRune(c, v) {
      str.WriteRune(v)
    }
  }

  r := str.String()
  return [2]interface{}{r, r == Reverse(r)}
}

func Reverse(s string) string {
  runes := []rune(s)
  for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
    runes[i], runes[j] = runes[j], runes[i]
  }
  return string(runes)
}
```

## Explanation

In this code, we first create a strings.Builder and iterate over the string `s`. If the character in `s` is not in string `c`, we add it to the string. This will effectively remove any character in `s` that is present in `c`.

After we have our new string, we check if it is the same as its reverse. If it is, we return it along with `true`, otherwise we return the string and `false`.

The function `Reverse` is used to reverse the given string. We create a rune array from the string, then we swap the first and last runes, then the second and second-to-last runes, and so on, until we reach the middle of the string. We then convert this rune array back into a string and return it.

This program uses Go's strings package and the Rune type, which allows for easy manipulation of individual characters in a string.

## Testing

```go
package main

import (
    "fmt"
)

func main() {
    fmt.Println(ReverseDelete("abcde", "ae"))    // Output: [bcd false]
    fmt.Println(ReverseDelete("abcdef", "b"))    // Output: [acdef false]
    fmt.Println(ReverseDelete("abcdedcba", "ab")) // Output: [cdedc true]
}
```