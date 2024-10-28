    var i int = 0
    for str[i] != '\000' {
        i++
    }
    return i
}

B:
    var i int = 0
    for ; str[i] != '\000'; i++ {
    }
    return i
}

C:
    return len(str)
}

D:
    var i int = 0
    for range str {
        i++
    }
    return i
}

Which one is correct?

A) A: manual loop with a condition
B) B: manual loop with a condition
C) C: built-in len() function
D) D: range-based loop

Solution:
The correct answer is C) C: built-in len() function. The built-in len() function in Go returns the length of a string. It is more efficient and easier to read than the manual loop-based solutions.

Here is the correct code:

```go
func Strlen(str string) int {
    return len(str)
}
```

This function takes a string as an argument and returns its length. The len() function is a built-in function in Go that returns the length of a string. It is more efficient and easier to read than the manual loop-based solutions.