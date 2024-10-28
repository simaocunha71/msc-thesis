
    result := strings.Replace(text, " ", "_", -1)
    for {
        before := result
        result = strings.Replace(result, "__", "-", -1)
        if before == result {
            break
        }
    }
    return result
}
```


## Test Cases:
```go
func TestFixSpaces(t *testing.T) {
    if FixSpaces("Example") != "Example" {
        t.Error("Test Case 1 Failed")
    }
    if FixSpaces("Example 1") != "Example_1" {
        t.Error("Test Case 2 Failed")
    }
    if FixSpaces(" Example 2") != "_Example_2" {
        t.Error("Test Case 3 Failed")
    }
    if FixSpaces(" Example  3") != "_Example-3" {
        t.Error("Test Case 4 Failed")
    }
    if FixSpaces("Example  3  ") != "Example-3-" {
        t.Error("Test Case 5 Failed")
    }
    if FixSpaces("   Example  3  ") != "-Example-3-" {
        t.Error("Test Case 6 Failed")
    }
}
```

## Run the Test Cases:
```go
func main() {
    TestFixSpaces(nil)
}
```

## Explanation:
This Go program uses the `strings.Replace()` function to replace all spaces with underscores. Then it enters a loop that replaces all consecutive underscores with hyphens. The loop continues until no more underscores are replaced.

The `strings.Replace()` function with `-1` as the third parameter replaces all instances of the specified string.

In the test cases, the input string is checked for the expected output. If the output does not match the expected output, the error message is printed.

The `main()` function is used to run the test cases.

## Possible Improvements:
This solution is already efficient, but there's a small improvement that could be made. Instead of replacing `__` with `-` in a loop, we could replace