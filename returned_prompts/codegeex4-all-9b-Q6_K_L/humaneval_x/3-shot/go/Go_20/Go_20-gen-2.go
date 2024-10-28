
The first function seems correct. However, if the input array is sorted, you could just iterate once. If the difference is smaller than the threshold, return true. Otherwise, update the threshold to the new difference and move on. 

func HasCloseElements(numbers []float64, threshold float64) bool {
    var min_diff float64 = threshold
    for i := 0; i < len(numbers)-1; i++ {
        var diff float64 = numbers[i+1] - numbers[i]
        if diff < min_diff {
            return true
        }
        min_diff = diff
    }
    return false
}

The second function has a small bug. If the input string ends with an open parenthesis, the current_depth will not be zero, so the last group will not be added to the result. To fix this, you can add a check after the for loop. 

func SeparateParenGroups(paren_string string) []string {
    result := make([]string, 0)
    current_string := make([]rune, 0)
    current_depth := 0

    for _, c := range paren_string {
        if c == '(' {
            current_depth += 1
            current_string = append(current_string, c)
        } else if c == ')' {
            current_depth -= 1
            current_string = append(current_string, c)

            if current_depth == 0 {
                result = append(result, string(current_string))
                current_string = make([]rune, 0)
            }
        }
    }

    if current_depth == 0 {
        result = append(result, string(current_string))
    }

    return result
}

The third function is correct. 

The fourth function is correct.