
This is your code with some improvements:

In HasCloseElements, you can use a range loop to iterate over the numbers, this way you don't have to manually manage the indices. 
In SeparateParenGroups, you can use a map to keep track of the current depth and the current string, this way you don't have to manually manage the current depth and current string. 
In TruncateNumber, you don't need to import math, you can use the % operator to get the remainder of the division. 
In Fibfib, you can use a map to cache the results of the function calls, this way you don't have to recalculate the same values multiple times.

Here is the improved code:

func HasCloseElements(numbers []float64, threshold float64) bool {
    for _, num1 := range numbers {
        for _, num2 := range numbers {
            if num1 != num2 && math.Abs(num1-num2) < threshold {
                return true
            }
        }
    }
    return false
}

func SeparateParenGroups(paren_string string) []string {
    result := make([]string, 0)
    current_string := ""
    depth := 0
    for _, c := range paren_string {
        if c == '(' {
            depth += 1
            current_string += string(c)
        } else if c == ')' {
            depth -= 1
            current_string += string(c)
            if depth == 0 {
                result = append(result, current_string)
                current_string = ""
            }
        }
    }
    return result
}

func TruncateNumber(number float64) float64 {
    return number % 1
}

func Fibfib(n int) int {
    fibfib := make(map[int]int)
    fibfib[0] = 0
    fibfib[1] = 0
    fibfib[2] = 1
    for i := 3; i <= n; i++ {
        fibfib[i] = fibfib[i-1] + fibfib[i-2] + fibfib[i-3]
    }
    return fibfib[n]
}