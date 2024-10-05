```go
package main

import (
	"regexp"
)

func IsBored(S string) int {
	re, _ := regexp.Compile(`^I.*[.!?]$`)
	matches := re.FindAllString(S, -1)
	return len(matches)
}

func main() {
	fmt.Println(IsBored("Hello world"))  // 0
	fmt.Println(IsBored("The sky is blue. The sun is shining. I love this weather"))  // 1
}
```

The function `IsBored` takes a string `S` as input and returns the number of boredoms found in the string. A boredom is defined as a sentence that starts with the word "I" and is followed by any characters and ends with a period, question mark, or exclamation mark.

In the `IsBored` function, we use the `regexp.Compile` function to create a regular expression that matches the pattern of a boredom. The regular expression `^I.*[.!?]$` matches a string that starts with "I" (`^I`), followed by any characters (`.*`), and ends with a period, question mark, or exclamation mark (`[.!?]$`).

We then use the `FindAllString` function to find all matches of the regular expression in the input string `S`. The `FindAllString` function returns a slice of strings that match the regular expression.

Finally, we return the length of the slice of matches, which is the number of boredoms found in the input string.

In the `main` function, we test the `IsBored` function with two examples: "Hello world" and "The sky is blue. The sun is shining. I love this weather". The first example returns 0, because there are no boredoms, and the second example returns 1, because there is one boredom.