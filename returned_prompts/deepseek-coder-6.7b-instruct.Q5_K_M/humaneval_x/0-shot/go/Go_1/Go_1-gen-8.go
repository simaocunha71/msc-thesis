
1.  Initialize an empty list to store the result.
2.  Replace all spaces in the input string with nothing.
3.  Initialize a counter variable to keep track of the level of nested parentheses.
4.  Initialize an empty string to store the current group of parentheses.
5.  Iterate through each character in the input string.
6.  If the character is an open brace ('('), increment the counter and add the character to the current group of parentheses.
7.  If the character is a close brace (')'), decrement the counter.
8.  If the counter reaches zero (indicating the end of a group of parentheses), add the current group of parentheses to the result list, and reset the current group of parentheses.
9.  Return the result list.

Here is the Python code for this function:

```python
def separate_paren_groups(paren_string):
    result = []
    paren_string = paren_string.replace(' ', '')
    counter = 0
    current_group = ''
    for char in paren_string:
        if char == '(':
            counter += 1
            current_group += char
        elif char == ')':
            counter -= 1
            current_group += char
            if counter == 0:
                result.append(current_group)
                current_group = ''
    return result
```

This function works by iterating through the characters in the input string and updating a counter to keep track of the level of nested parentheses. When the counter reaches zero, it means that we've reached the end of a group of parentheses, so we add the current group to the result list and reset the current group for the next group of parentheses.

It's worth noting that this function assumes that the input string is well-formed and contains only parentheses and spaces. If there are any other characters in the string, it will not be correctly handled.
*/

func SeparateParenGroups(parenString string) []string {
	result := []string{}
	parenString = strings.ReplaceAll(parenString, " ", "")
	counter := 0
	currentGroup := ""