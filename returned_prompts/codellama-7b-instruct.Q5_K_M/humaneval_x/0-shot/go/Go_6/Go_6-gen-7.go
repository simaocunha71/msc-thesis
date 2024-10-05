    for i, _ := range paren_string {
        if paren_string[i] == '(' {
            stack.push(paren_string[i])
        } else if paren_string[i] == ')' {
            stack.pop()
        }
    }
    
    for stack.size() > 0 {
        stack.pop()
    }
    
    return stack
}


// B:
func ParseNestedParens(paren_string string) []int {
    var result []int
    for _, v := range strings.Split(paren_string, " ") {
        if v == "(" {
            result = append(result, 1)
        } else if v == ")" {
            result = append(result, -1)
        } else {
            result = append(result, 0)
        }
    }
    var sum int
    for _, v := range result {
        sum += v
    }
    return []int{sum}
}


// C:
func ParseNestedParens(paren_string string) []int {
    var stack []string
    var result []int
    for _, v := range strings.Split(paren_string, " ") {
        if v == "(" {
            stack = append(stack, "(")
        } else if v == ")" {
            if len(stack) > 0 {
                stack = stack[:len(stack)-1]
            } else {
                result = append(result, 1)
            }
        } else {
            result = append(result, 0)
        }
    }
    for len(stack) > 0 {
        result = append(result, -1)
        stack = stack[:len(stack)-1]
    }
    return result
}


// D:
func ParseNestedParens(paren_string string) []int {
    var result []int
    for _, v := range strings.Split(paren_string, " ") {
        if v == "(" {
            result = append(result, 1)
        } else if v == ")" {
            result = append(