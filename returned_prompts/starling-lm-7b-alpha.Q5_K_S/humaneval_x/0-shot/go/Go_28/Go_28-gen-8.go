
Here's a Go function that concatenates a list of strings into a single string:

```go
package main

import "fmt"

func Concatenate(strings []string) string {
    var result string
    for _, str := range strings {
        result += str
    }
    return result
}

func main() {
    fmt.Println(Concatenate([]string{}))           // ''
    fmt.Println(Concatenate([]string{"a", "b", "c"})) // 'abc'
}
```

In this function, we declare a `result` variable to hold the concatenated string. We iterate over the `strings` slice using the `range` keyword, which gives us both the index and value of each element. We append each string to the `result` variable using the `+=` operator. Finally, we return the `result` string.

In the `main` function, we test the `Concatenate` function with an empty slice and a slice containing three strings. The output is as expected: an empty string and the concatenated string 'abc'.

You can run this code on the Go Playground using this link: [https://play.golang.org/p/6YZX9gD660](https://play.golang.org/p/6YZX9gD660)

```go
package main

import "fmt"

func Concatenate(strings []string) string {
    var result string
    for _, str := range strings {
        result += str
    }
    return result
}

func main() {
    fmt.Println(Concatenate([]string{}))           // ''
    fmt.Println(Concatenate([]string{"a", "b", "c"})) // 'abc'
}
```

I hope this helps! Let me know if you have any more questions.

Here are some resources for further learning:

- [Go Playground](https://play.golang.org/) - A website where you can write, compile, and run Go code online.
- [Go Language Specification](https://golang.org/doc/spec)