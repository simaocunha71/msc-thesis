
The first function is correct. You iterate over all pairs of numbers and check if they are closer than the given threshold.
The second function has a logical error. You decrement the current_depth only when you encounter a closing parenthesis, but you should do it when you encounter an opening parenthesis as well. This will fix the logic:
for _, c := range paren_string {
    if c == '(' {
        current_depth += 1
    } else if c == ')' {
        current_depth -= 1
    }
    current_string = append(current_string, c)

    if current_depth == 0 {
        result = append(result, string(current_string))
        current_string = make([]rune, 0)
    }
}

The third function is correct. You use the math.Mod function to get the decimal part of the number.
The fourth function has a logical error. You are splitting the string by spaces, but the spaces in the input string are not consistent. You should split the string by the substring "apples" and "oranges" instead. This will fix the logic:
numbers := strings.Split(s, "apples")
apples, _ := strconv.Atoi(strings.TrimSpace(numbers[0]))
numbers = strings.Split(numbers[1], "oranges")
oranges, _ := strconv.Atoi(strings.TrimSpace(numbers[0]))
return n - apples - oranges