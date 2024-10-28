
	res := []rune{}
	spaceCount := 0

	for _, c := range text {

		switch c {
		case ' ':
			spaceCount++
		default:
			for i := 0; i < spaceCount; i++ {
				if spaceCount > 2 {
					res = append(res, '_')
				} else {
					res = append(res, ' ')
				}
			}
			spaceCount = 0
			res = append(res, c)
		}
	}

	for i := 0; i < spaceCount; i++ {
		res = append(res, ' ')
	}

	return string(res)
}
```

## Test cases
```go
func main() {
	fmt.Println(FixSpaces("Example")) // "Example"
	fmt.Println(FixSpaces("Example 1")) // "Example_1"
	fmt.Println(FixSpaces(" Example 2")) // "_Example_2"
	fmt.Println(FixSpaces(" Example  3")) // "_Example-3"
	fmt.Println(FixSpaces("Example  3  ")) // "Example-3_"
}
```

## Explanation
This problem involves string manipulation. The main idea is to loop through the string and process each character. If the character is a space, we increment a counter. If the character is not a space, we append the appropriate number of spaces or underscores to the result array, depending on the value of the counter. We also reset the counter after appending. After the loop, we append the remaining spaces to the result array. Finally, we convert the result array back into a string and return it.

## Complexity
The time complexity of this solution is O(n), where n is the length of the string. This is because we are looping through the string once. The space complexity is also O(n), where n is the length of the string. This is because we are creating a new array to store the result.

## Note
The solution assumes that the input string only contains printable ASCII characters and does not contain any special characters or escape sequences. If the input string could contain such characters, the