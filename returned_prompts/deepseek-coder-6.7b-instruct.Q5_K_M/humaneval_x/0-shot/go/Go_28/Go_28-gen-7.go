
// Concatenate concatenates a slice of strings into a single string.
func Concatenate(strings []string) string {
	return strings.Join(strings, "")
}

func main() {
	fmt.Println(Concatenate([]string{}))        // ''
	fmt.Println(Concatenate([]string{"a", "b", "c"}))  // 'abc'
}


```


## 4.2.2: 

```go
