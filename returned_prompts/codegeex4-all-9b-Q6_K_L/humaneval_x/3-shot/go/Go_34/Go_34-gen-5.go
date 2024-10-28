
Your HasCloseElements function looks good.  The only thing I'd suggest is to use a more descriptive variable name than distance, perhaps diff.  This makes it clear that you're calculating the difference between two numbers.
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

This loop looks correct.  You're iterating through each character in the string, and adding it to the current_string slice until you reach the end of a group of parentheses.  At that point, you add the current_string to the result slice and reset current_string to be empty.
Your TruncateNumber function is correct.  You're using the math.Mod function to calculate the remainder of the division of number by 1, which is the decimal part of the number.
Your Unique function is mostly correct, but there's a small issue.  When you're checking if l[i] != l[i-1], you're comparing the current element to the previous element.  This means that if you have a sequence of duplicate elements, it will only be added to the result slice once.  If you want to add all duplicates to the result slice, you should use a different approach.  One way to do this is to use a map to keep track of the elements you've seen so far.  Here's an example:
func Unique(l []int) []int {
    seen := make(map[int]bool)
    result := make([]int, 0)
    for _, num := range l {
        if !seen[num] {
            seen[num] = true
            result = append(result, num)
        }
    }
    return result
}

This function uses a map to keep track of the elements it has seen so far.  If an element hasn't been seen before, it adds it to the result slice and marks it as seen.  This ensures