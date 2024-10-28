
func Concatenate(strings []string) string {
  result := ""
  for _, str := range strings {
    result += str
  }
  return result
}

```


## Problem 2:

Write a function `CountChars` that counts the number of occurrences of each character in a string. Return the result as a `map` where the keys are characters and the values are the counts.

Example:

```python
// 