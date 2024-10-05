    strN := strconv.Itoa(N)

    sum := 0
    for _, v := range strN {
        num, _ := strconv.Atoi(string(v))
        sum += num
    }

    return strconv.FormatInt(int64(sum), 2)
}

func main() {
    fmt.Println(Solve(1000))
    fmt.Println(Solve(150))
    fmt.Println(Solve(147))
}

```


This is a simple problem to solve, but it requires a little bit of string manipulation and understanding of how to convert between different number systems in Go.

The main idea is that we first convert the integer to a string, then we iterate over each character in the string. Each character is then converted back to an integer and added to a running total. Finally, we convert the total sum back to binary and return it as a string.

This code should work as expected for the given constraints, and it should be easy to adapt for other similar problems.

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

