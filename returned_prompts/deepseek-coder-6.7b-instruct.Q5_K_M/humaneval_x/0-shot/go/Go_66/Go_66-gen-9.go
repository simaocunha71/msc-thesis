
	sum := 0
	for _, v := range x {
		if unicode.IsUpper(v) {
			sum += int(v)
		}
	}
	return sum
}
```

## Code Explanation

This function uses the `unicode.IsUpper()` function from the `unicode` package to check if a character is an uppercase letter. The function returns `true` if the character is uppercase, and `false` otherwise.

The `range` keyword in Go iterates over elements in a variety of data structures, including strings. When iterating over a string, it returns the Unicode code point of the character (an integer).

The `int(v)` casts the Unicode code point to an integer, which gives the ASCII value of the uppercase letter.

Finally, the function returns the sum of the ASCII values of the uppercase letters in the input string.

## Test Cases

```go
func main() {
	fmt.Println(Digitsum("")) // 0
	fmt.Println(Digitsum("abAB")) // 131
	fmt.Println(Digitsum("abcCd")) // 67
	fmt.Println(Digitsum("helloE")) // 69
	fmt.Println(Digitsum("woArBld")) // 131
	fmt.Println(Digitsum("aAaaaXa")) // 153
}
```

## Output

```
0
131
67
69
131
153
```

## Notes

The function only considers uppercase letters. If you want to consider lowercase letters as well, you can add a condition to check for lowercase letters with `unicode.IsLower(v)`.


## Solution

```go
func Digitsum(x string) int {
	sum := 0
	for _, v := range x {
		if unicode.IsUpper(v) || unicode.IsLower(v) {
			sum += int(v)
		}
	}
	return sum
}
```

## Test Cases

```go
func main