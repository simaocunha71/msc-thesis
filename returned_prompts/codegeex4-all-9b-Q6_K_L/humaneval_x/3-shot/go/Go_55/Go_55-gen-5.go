
For your first question, you are on the right track. However, the second loop should start from i+1, not i. This is because we don't need to compare a number with itself. Here's the corrected code:

```go
func HasCloseElements(numbers []float64, threshold float64) bool {
    for i := 0; i < len(numbers); i++ {
        for j := i + 1; j < len(numbers); j++ {
            var distance float64 = math.Abs(numbers[i] - numbers[j])
            if distance < threshold {
                return true
            }
        }
    }
    return false
}
```

For your second question, your code looks good. However, you can simplify it by using a stack to keep track of the current depth of parentheses. Here's the simplified code:

```go
func SeparateParenGroups(paren_string string) []string {
    result := make([]string, 0)
    stack := make([]rune, 0)
    current_string := make([]rune, 0)

    for _, c := range paren_string {
        if c == '(' {
            stack = append(stack, c)
            current_string = append(current_string, c)
        } else if c == ')' {
            stack = stack[:len(stack)-1]
            current_string = append(current_string, c)

            if len(stack) == 0 {
                result = append(result, string(current_string))
                current_string = make([]rune, 0)
            }
        }
    }

    return result
}
```

For your third question, your code is correct. However, you can optimize it by using memoization to avoid recalculating the same Fibonacci numbers multiple times. Here's the optimized code:

```go
func Fib(n int) int {
    memo := make(map[int]int)
    return fibHelper(n, memo)
}

func fibHelper(n int, memo map[int]int) int {
    if n <= 0 {
        return 0
    }

    if n == 1 {
        return 1
    }

    if val, ok := memo[n]; ok {
        return val
    }

    result := fibHelper(n-1, memo) + fibHelper(n-2, memo)
    memo