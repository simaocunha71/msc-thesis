    letter_freq := make(map[rune]int)
    max_freq := 0

    for _, letter := range test {
        if letter != ' ' {
            letter_freq[letter]++
            if letter_freq[letter] > max_freq {
                max_freq = letter_freq[letter]
            }
        }
    }

    result := make(map[rune]int)

    for letter, freq := range letter_freq {
        if freq == max_freq {
            result[letter] = freq
        }
    }

    return result
}

// Test cases:
func main() {
    fmt.Println(Histogram("a b c")) // should print: map[97:1 98:1 99:1]
    fmt.Println(Histogram("a b b a")) // should print: map[97:2 98:2]
    fmt.Println(Histogram("a b c a b")) // should print: map[97:2 98:2]
    fmt.Println(Histogram("b b b b a")) // should print: map[98:4]
    fmt.Println(Histogram("")) // should print: map[]
}
```

## Question 3

```go
