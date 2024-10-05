
// Return list of all prefixes from shortest to longest of the input string
// >>> AllPrefixes('abc')
// ['a', 'ab', 'abc']

func AllPrefixes(str string) []string {
	var result []string
	for i := 0; i < len(str); i++ {
		result = append(result, str[:i+1])
	}
	return result
}

func main() {
	fmt.Println(AllPrefixes("abc"))
}
