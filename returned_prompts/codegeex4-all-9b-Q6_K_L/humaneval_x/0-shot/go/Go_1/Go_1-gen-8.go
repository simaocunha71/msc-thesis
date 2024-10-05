You can solve this problem by iterating through the input string character by character, keeping track of the current group of parentheses and adding it to the result when you find a closing parenthesis that matches the last open parenthesis.

Here is a possible implementation of the function in Go:

```go
func SeparateParenGroups(paren_string string) []string {
    var groups []string
    var currentGroup []rune
    var openCount int

    for _, c := range paren_string {
        if c == '(' {
            openCount++
            currentGroup = append(currentGroup, c)
        } else if c == ')' && openCount > 0 {
            openCount--
            currentGroup = append(currentGroup, c)
            if openCount == 0 {
                groups = append(groups, string(currentGroup))
                currentGroup = []rune{}
            }
        }
    }

    return groups
}
```

This function uses a slice of runes to store the current group of parentheses and an integer to keep track of the number of open parentheses. It iterates through the input string character by character, and when it finds an open parenthesis, it increments the openCount and appends the character to the currentGroup. When it finds a closing parenthesis and the openCount is greater than 0, it decrements the openCount, appends the character to the currentGroup, and if the openCount is 0, it adds the currentGroup to the groups slice and resets the currentGroup.

You can test the function with the example you provided:

```go
func main() {
    paren_string := "( ) (( )) (( )( ))"
    groups := SeparateParenGroups(paren_string)
    fmt.Println(groups) // Output: ['()', '(())', '(()())']
}
```