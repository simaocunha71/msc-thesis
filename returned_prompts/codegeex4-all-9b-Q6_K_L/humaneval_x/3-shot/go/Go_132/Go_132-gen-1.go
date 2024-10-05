
for _, c := range paren_string {
        if c == '(' {
            current_depth += 1
            current_string = append(current_string, c)
        }else if c== ')'{
            current_depth -= 1
            current_string = append(current_string, c)

            if current_depth == 0{
                result = append(result, string(current_string))
                current_string =  make([]rune, 0)
            }
        }

    }
    return result
}

This is an implementation of the SeparateParenGroups function. The function takes a string as input which contains only square brackets. The function separates the groups of nested parentheses into separate strings and returns the list of those.
The function uses a loop to iterate over each character in the input string. If the character is an opening bracket, the function increments the current_depth variable and appends the character to the current_string. If the character is a closing bracket, the function decrements the current_depth variable and appends the character to the current_string. If the current_depth is 0, the function appends the current_string to the result list and resets the current_string.
The function then returns the result list, which contains the separate groups of nested parentheses.