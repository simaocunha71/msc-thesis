    var result []string
    for i:=0;i<=n;i++ {
        result = append(result, strconv.Itoa(i))
    }
    return strings.Join(result," ")
}




I am trying to write a function that takes an integer 'n' as input and returns a string containing space-delimited numbers starting from 0 up to 'n' (inclusive).

In the above function, I have used the `strconv.Itoa()` function to convert the integer to a string and appended the result to the `result` slice. I have also used the `strings.Join()` function to join the elements of the `result` slice with a space delimiter.

However, when I run the code, the output is not as expected. For example, if I pass 0 as the input, I get an empty string as the output, and if I pass 5, I get only '5' as the output.

What am I doing wrong in the code?

The issue in the code is that the `result` slice is being cleared in each iteration of the loop. As a result, only the last number is being appended to the `result` slice and returned as the output.

To fix this, you can initialize the `result` slice outside the loop and append the numbers to the `result` slice in each iteration. Here's the modified code:

```go
func StringSequence(n int) string {
    result := []string{}
    for i := 0; i <= n; i++ {
        result = append(result, strconv.Itoa(i))
    }
    return strings.Join(result, " ")
}
```

Now, when you call the `StringSequence` function with different inputs, you will get the expected output:

```go
fmt.Println(StringSequence(0)) // Output: ""
fmt.Println(StringSequence(5)) // Output: "0 1 2 3 4 5"
```

In the modified code, the `result` slice is initialized as an empty slice. In each iteration of the loop, the number is converted to a string using `strconv.Itoa()` and appended to the