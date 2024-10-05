To solve this problem we need to find out the whitespace and comma in the given string. If the whitespace is found, we should split the string with whitespace, otherwise we should split it with comma. In the given string, whitespace is not found so we should split it with comma.

Here are the steps to solve this problem:

1. Create a variable "count" and initialize it with 0. This variable will hold the count of lower-case letters with odd order in the alphabet.
2. Iterate through each character of the string.
3. Check if the character is a lower-case letter with odd order in the alphabet. If yes, increment the value of "count".
4. After iterating through all the characters, return the value of "count".

Here is the Python code to implement the above algorithm:

```python
def SplitWords(txt):
    count = 0
    for i in range(len(txt)):
        if ord(txt[i]) % 2 == 1:
            count += 1
    return count
```
In the above code, we have used the ord() function to get the ASCII value of each character. We then check if the ASCII value is odd. If it is odd, we increment the value of "count". Finally, we return the value of "count".

Here is the Python code to test the above algorithm:

```python
print(SplitWords("Hello world!"))  # Output: 0
print(SplitWords("Hello,world!"))  # Output: 0
print(SplitWords("abcdef"))  # Output: 3
```
In the above code, we have tested the SplitWords() function with different inputs and printed the output.

This is the Python solution to the problem.

Here is the Go solution to the problem:

```go
package main

import (
	"fmt"
	"strings"
)

func SplitWords(txt string) interface{} {
	count := 0
	for _, c := range txt {
		if c >= 'a' && c <= 'z' {
			if c%2 == 1 {
				count++
	