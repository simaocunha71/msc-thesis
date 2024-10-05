
	dict := map[int]string{
		1:    "i",
		4:    "iv",
		5:    "v",
		9:    "ix",
		10:   "x",
		40:   "xl",
		50:   "l",
		90:   "xc",
		100:  "c",
		400:  "cd",
		500:  "d",
		900:  "cm",
		1000: "m",
	}

	res := ""
	for number > 0 {
		divisor := 0
		for key := range dict {
			if key > number {
				break
			}
			divisor = key
		}
		res += dict[divisor]
		number -= divisor
	}
	return strings.ToLower(res)
}

func main() {
	fmt.Println(IntToMiniRoman(19))
	fmt.Println(IntToMiniRoman(152))
	fmt.Println(IntToMiniRoman(426))
}

```

The function works by iterating over the map keys in ascending order, and for each key, checking if it is smaller or equal to the number. If it is, the corresponding value (the roman numeral equivalent) is appended to the result string and the key is subtracted from the number. This process repeats until the number becomes zero.

The function returns the result string in lowercase.

This solution has a time complexity of O(1) since it has a constant number of operations, and a space complexity of O(1) since it has a constant amount of space used.



```go
func IntToMiniRoman(number int) string {
	dict := map[int]string{
		1:    "i",
		4:    "iv",
		5:    "v",
		9:    "ix",
		10:   "x",
		40:   "xl",
		50:   "l",
		90:   "xc",
		100