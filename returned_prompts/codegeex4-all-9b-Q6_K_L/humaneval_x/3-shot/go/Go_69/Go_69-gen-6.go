
First, your second function is not complete. You are missing the closing parenthesis of the function. I assume you are using some text editor that's why you have not noticed that.

Second, you can optimize your second function. You don't need to keep track of the current depth, you just need to count the number of open and close parenthesis. When the number of open parenthesis is equal to the number of close parenthesis, then you have found a group.

Here is the optimized version of your second function:

func SeparateParenGroups(paren_string string) []string {
    result := make([]string, 0)
    open_count := 0
    close_count := 0
    current_string := make([]rune, 0)

    for _, c := range paren_string {
        if c == '(' {
            open_count += 1
            current_string = append(current_string, c)
        } else if c == ')' {
            close_count += 1
            current_string = append(current_string, c)

            if open_count == close_count {
                result = append(result, string(current_string))
                current_string = make([]rune, 0)
                open_count = 0
                close_count = 0
            }
        }
    }

    return result
}

Now, let's move to your third function. It seems that you are trying to find the greatest integer that has a frequency greater than or equal to the value of the integer itself. However, your implementation is not correct. You are checking if the key is less than or equal to the value, but you should be checking if the value is greater than or equal to the key.

Here is the correct version of your third function:

func Search(lst []int) int {
    m := make(map[int]int)

    for _, e := range lst {
        m[e]++
    }

    var max int
    for k, v := range m {
        if v >= k {
            max = k
        }
    }

    return max
}