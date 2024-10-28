    levels := []int{}

    paren_string = strings.Replace(paren_string, "()", " X ", -1)
    paren_string = strings.Replace(paren_string, ")", " Y ", -1)
    paren_string = strings.Replace(paren_string, "(", " ", -1)
    paren_string = strings.Replace(paren_string, " ", "", -1)
    paren_string = strings.Replace(paren_string, "X", ")", -1)
    paren_string = strings.Replace(paren_string, "Y", "(", -1)

    for _, paren := range strings.Split(paren_string, "") {
        if paren == ")" {
            levels = append(levels, levels[len(levels)-1]-1)
        } else {
            levels = append(levels, levels[len(levels)-1]+1)
        }
    }
    return levels
}








// Test Cases:

fmt.Println(ParseNestedParens("()"))                    // [0]
fmt.Println(ParseNestedParens("((()))"))                 // [3]
fmt.Println(ParseNestedParens("(()())"))                 // [2]
fmt.Println(ParseNestedParens("()()()"))                // [2, 1]
fmt.Println(ParseNestedParens("(((())))"))              // [4]
fmt.Println(ParseNestedParens("(((())))()()()"))       // [4, 2]
fmt.Println(ParseNestedParens("(()())((()))()()()()()()()")) // [2, 3, 1, 3]


























































































