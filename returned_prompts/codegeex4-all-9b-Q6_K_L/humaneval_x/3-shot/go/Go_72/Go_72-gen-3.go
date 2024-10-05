
You are doing a lot of unnecessary work in your for loops. You can simplify your logic by taking advantage of Go's built-in functions.
The first function can be simplified as follows:

func HasCloseElements(numbers []float64, threshold float64) bool {
    for i := 0; i < len(numbers); i++ {
        for j := i + 1; j < len(numbers); j++ {
            if math.Abs(numbers[i]-numbers[j]) < threshold {
                return true
            }
        }
    }
    return false
}

In the SeparateParenGroups function, you can use the strings package to remove spaces from the input string and then split the string on the parentheses. Here's a simplified version:

func SeparateParenGroups(paren_string string) []string {
    paren_string = strings.ReplaceAll(paren_string, " ", "")
    return strings.Split(paren_string, "()")
}

The TruncateNumber function can be simplified as follows:

func TruncateNumber(number float64) float64 {
    return math.Mod(number, 1)
}

The WillItFly function can be simplified as follows:

func WillItFly(q []int, w int) bool {
    if len(q) == 0 {
        return false
    }

    total := 0
    for _, v := range q {
        total += v
    }

    if total > w {
        return false
    }

    for i := 0; i < len(q)/2; i++ {
        if q[i] != q[len(q)-i-1] {
            return false
        }
    }

    return true
}