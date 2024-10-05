Here is a Go function that solves the problem. This function calculates the total number of characters in each list and returns the list with the total number of characters less than the other list. If the two lists have the same number of characters, it returns the first list.

```go
func TotalMatch(lst1 []string, lst2 []string) []string {
    total1 := 0
    total2 := 0
    for _, s := range lst1 {
        total1 += len(s)
    }
    for _, s := range lst2 {
        total2 += len(s)
    }
    if total1 < total2 {
        return lst1
    } else if total2 < total1 {
        return lst2
    } else {
        return lst1
    }
}
```

You can test this function with the examples you provided:

```go
fmt.Println(TotalMatch([]string{}, []string{})) // []
fmt.Println(TotalMatch([]string{"hi", "admin"}, []string{"hI", "Hi"})) // ["hI", "Hi"]
fmt.Println(TotalMatch([]string{"hi", "admin"}, []string{"hi", "hi", "admin", "project"})) // ["hi", "admin"]
fmt.Println(TotalMatch([]string{"hi", "admin"}, []string{"hI", "hi", "hi"})) // ["hI", "hi", "hi"]
fmt.Println(TotalMatch([]string{"4"}, []string{"1", "2", "3", "4", "5"})) // ["4"]
```