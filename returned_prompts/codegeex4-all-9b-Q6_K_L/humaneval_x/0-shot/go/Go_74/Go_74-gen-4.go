func TotalMatch(lst1 []string, lst2 []string) []string {
	if len(lst1) == 0 && len(lst2) == 0 {
		return []string{}
	}
	if len(lst1) == 0 {
		return lst2
	}
	if len(lst2) == 0 {
		return lst1
	}
	total1 := 0
	for _, v := range lst1 {
		total1 += len(v)
	}
	total2 := 0
	for _, v := range lst2 {
		total2 += len(v)
	}
	if total1 <= total2 {
		return lst1
	}
	return lst2
}

func main() {
	fmt.Println(TotalMatch([]string{}, []string{}))
	fmt.Println(TotalMatch([]string{"hi", "admin"}, []string{"hI", "Hi"}))
	fmt.Println(TotalMatch([]string{"hi", "admin"}, []string{"hi", "hi", "admin", "project"}))
	fmt.Println(TotalMatch([]string{"hi", "admin"}, []string{"hI", "hi", "hi"}))
	fmt.Println(TotalMatch([]string{"4"}, []string{"1", "2", "3", "4", "5"}))
}

func main() {
	fmt.Println(TotalMatch([]string{}, []string{})) // ➞ []
	fmt.Println(TotalMatch([]string{"hi", "admin"}, []string{"hI", "Hi"})) // ➞ ["hI", "Hi"]
	fmt.Println(TotalMatch([]string{"hi", "admin"}, []string{"hi", "hi", "admin", "project"})) // ➞ ["hi", "admin"]
	fmt.Println(TotalMatch([]string{"hi", "admin"}, []string{"hI", "hi", "hi"})) // ➞ ["hI", "hi", "hi"]
	fmt.Println(TotalMatch([]string{"4"}, []string{"1", "2", "3", "4", "5"})) // ➞ ["4"]
}