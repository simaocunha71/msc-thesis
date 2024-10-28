
    count := 0

    for _, c := range s {
        if unicode.IsLetter(c) {
            count++
        }
    }

    if count == 0 {
        return reverse(s)
    }

    b := []rune(s)

    for i, c := range b {
        if unicode.IsLetter(c) {
            if unicode.IsLower(c) {
                b[i] = unicode.ToUpper(c)
            } else {
                b[i] = unicode.ToLower(c)
            }
        }
    }

    return string(b)
}

func reverse(s string) string {
    b := []rune(s)
    for i := 0; i < len(b)/2; i++ {
        b[i], b[len(b)-i-1] = b[len(b)-i-1], b[i]
    }
    return string(b)
}

```

## 3. Write a function that returns the number of distinct characters in a string.

```go

package main

import "fmt"

func countDistinctCharacters(s string) int {
    count := make(map[rune]bool)

    for _, c := range s {
        count[c] = true
    }

    return len(count)
}

func main() {
    fmt.Println(countDistinctCharacters("hello"))
}

```

## 4. Write a function that returns the frequency of a character in a string.

```go

package main

import "fmt"

func charFrequency(s string, char rune) int {
    count := 0

    for _, c := range s {
        if c == char {
            count++
        }
    }

    return count
}

func main() {
    fmt.Println(charFrequency("hello", 'l'))
}

```

## 5. Write a function that returns a string with the words in reverse order.

```go