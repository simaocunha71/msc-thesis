
HasCloseElements
This code is correct, but it can be simplified by using two for loops with a single range.
for i := range numbers {
    for j := i + 1; j < len(numbers); j++ {
        var distance float64 = math.Abs(numbers[i] - numbers[j])
        if distance < threshold {
            return true
        }
    }
}

SeparateParenGroups
This code is correct, but it can be simplified by using a single for loop with a range.
for i, c := range paren_string {
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

TruncateNumber
This code is correct, but it can be simplified by using the math.Floor function.
return number - math.Floor(number)

AnyInt
This code is incorrect. It always returns false, regardless of the input. It needs to be fixed to check if any of the numbers is equal to the sum of the other two, and all numbers are integers.