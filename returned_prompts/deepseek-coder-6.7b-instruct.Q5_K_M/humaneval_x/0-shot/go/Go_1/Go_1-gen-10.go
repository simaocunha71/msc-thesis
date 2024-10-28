
// We use a stack data structure to solve this problem. 
// We iterate over the input string and push onto the stack when we encounter an open parenthesis. 
// When we encounter a closed parenthesis, we pop off from the stack until we encounter the matching open parenthesis, 
// and form a group.
// We repeat this process until the string is exhausted.
// At the end, we have a list of separate balanced groups.

var stack []string
    result := []string{}
    temp := ""
    for _, ch := range paren_string {
        if string(ch) == " " {
            continue
        }
        temp += string(ch)
        if string(ch) == "(" {
            stack = append(stack, string(ch))
        }
        if string(ch) == ")" {
            stack = stack[:len(stack)-1]
            if len(stack) == 0 {
                result = append(result, temp)
                temp = ""
            }
        }
    }
    return result
}

// This solution works in O(n) time complexity where n is the length of the input string as we go through the string once.
// And we use an additional space to store the stack and the result which in the worst case is equal to the length of the input string.
// So, the space complexity is O(n).



































































































































































































