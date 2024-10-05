
You have some code that's pretty good, but could use some cleanup. Here's a breakdown of what I see:

In the HasCloseElements() function, you're looping over the slice twice, but there's no need. You can use a single loop and just check the current value against all the previous values.
In the SeparateParenGroups() function, you're using a rune slice instead of a string slice. This is fine, but you'll have to convert your slice to a string when you append it to your result slice.
In the TruncateNumber() function, you're using the math.Mod() function, which is correct, but you're not handling the case where the number is already an integer. In this case, you should return 0.0.
In the WillItFly() function, you're looping over the slice twice, but there's no need. You can use a single loop and just check the current value against all the previous values.

Here's the cleaned-up code:

func HasCloseElements(numbers []float64, threshold float64) bool {
    for i := 0; i < len(numbers); i++ {
        for j := 0; j < i; j++ {
            var distance float64 = math.Abs(numbers[i] - numbers[j])
            if distance < threshold {
                return true
            }
        }
    }
    return false
}

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
    return result
}

func TruncateNumber(number float64) float