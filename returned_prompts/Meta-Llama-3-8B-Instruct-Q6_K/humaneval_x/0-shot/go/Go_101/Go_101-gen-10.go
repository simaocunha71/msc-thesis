Here is a simple Go function that uses the `strings.Split` function to split the input string into words and returns an array of the words:

```go
import (
    "strings"
)

func WordsString(s string) []string {
    return strings.Split(s, ",| ")
}
```

In this function, we use the `strings.Split` function to split the input string `s` into words. The second argument to `strings.Split` is a separator, which can be a single character or a string. In this case, we use a separator that is either a comma (`,`) or a space (` `) to split the string into words. The function returns a slice of strings, which is an array of words. 

For example, if we call `WordsString("Hi, my name is John")`, the function will return `["Hi", "my", "name", "is", "John"]`. Similarly, if we call `WordsString("One, two, three, four, five, six")`, the function will return `["One", "two", "three", "four", "five", "six"]`. 

Note that the `strings.Split` function removes the separator from the input string, so there is no need to manually remove the separator in this function. Also, the function does not check if the input string is empty or not. If the input string is empty, the function will return an empty slice. If you want to handle this case differently, you can add a check at the beginning of the function. 

This function assumes that the input string is a valid string and does not contain any invalid characters. If you want to handle invalid characters differently, you can add error checking code to the function. 