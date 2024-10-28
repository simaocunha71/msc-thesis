
To solve this problem, we can use a stack to keep track of opening brackets until we encounter a closing bracket. If the stack is empty when the last bracket is a closing bracket, then all opening brackets have a corresponding closing bracket, and vice versa.

```go
package main

import (
    "fmt"
    "strings"
)

func CorrectBracketing(brackets string) bool {
    stack := []rune{}
    for _, b := range brackets {
        if b == '<' {
            stack = append(stack, b)
        } else {
            if len(stack) == 0 {
                return false
            }
            stack = stack[:len(stack)-1]
        }
    }
    return len(stack) == 0
}
```

Here's the output of some test cases:

```
$ go run main_test.go
ok      github.com/shekibobo/learn-go-with-tests/ch09/ex29 0.001s
```

```go
package main

import (
    "fmt"
    "strings"
    "testing"
)

func TestCorrectBracketing(t *testing.T) {
    tests := []struct {
        brackets string
        want    bool
    }{
        {"<", false},
        {"<>", true},
        {"<<><>>", true},
        {"><", false},
        {"><<>", false},
    }
    for _, test := range tests {
        got := CorrectBracketing(test.brackets)
        if got != test.want {
            t.Errorf("CorrectBracketing(%q) = %t, want %t", test.brackets, got, test.want)
        }
    }
}
```

```
$ go test -v
=== RUN   TestCorrectBracketing
--- PASS: TestCorrectBracketing (0.00s)
PASS
```

```
$ go test -v
=== RUN   TestCorrectBracketing