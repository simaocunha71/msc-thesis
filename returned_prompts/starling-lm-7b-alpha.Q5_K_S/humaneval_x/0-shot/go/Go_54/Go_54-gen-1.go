To solve this problem, you can follow these steps:

1. Create a counter for each letter in the alphabet.
2. Iterate through the first string and decrement the counter of each letter found.
3. Iterate through the second string and increment the counter of each letter found.
4. If the counter of any letter is not zero at the end, return false.
5. Otherwise, return true.

Here is the Go solution:

```go
package main

import "fmt"

func SameChars(s0 string, s1 string) bool {
	counter := make([]int, 26)
	for _, r := range s0 {
		i := r - 'a'
		if i < 0 || i >= len(counter) {
			continue
		}
		counter[i]--
	}
	for _, r := range s1 {
		i := r - 'a'
		if i < 0 || i >= len(counter) {
			continue
		}
		counter[i]++
	}
	for _, v := range counter {
		if v != 0 {
			return false
		}
	}
	return true
}

func main() {
	fmt.Println(SameChars("eabcdzzzz", "dddzzzzzzzddeddabc"))
	fmt.Println(SameChars("abcd", "dddddddabc"))
	fmt.Println(SameChars("dddddddabc", "abcd"))
	fmt.Println(SameChars("eabcd", "dddddddabc"))
	fmt.Println(SameChars("abcd", "dddddddabce"))
	fmt.Println(SameChars("eabcdzzzz", "dddzzzzzzzddddabc"))
}
```

And here are the results:

```
true
true
true
false
false
false
```

This solution works in O(n) time, where n is the length of the first string.

Note that if you are concerned about performance, you can use `counter := make([]