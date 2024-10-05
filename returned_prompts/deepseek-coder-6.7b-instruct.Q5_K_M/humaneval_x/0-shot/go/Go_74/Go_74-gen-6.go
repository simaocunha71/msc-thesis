
```go
func TotalMatch(lst1  []string,lst2  []string)  []string {
    var sum1, sum2 int
    for _, v := range lst1 {
        sum1 += len(v)
    }
    for _, v := range lst2 {
        sum2 += len(v)
    }
    if sum1 < sum2 {
        return lst1
    } else if sum2 < sum1 {
        return lst2
    } else {
        return lst1
    }
}
```

In the function `TotalMatch`, we are calculating the sum of all characters in both lists `lst1` and `lst2`. We then compare these sums and return the list with the smaller sum. If the sums are equal, we return `lst1`. 


```go
func main() {
    fmt.Println(TotalMatch([]string{}, []string{}))  // ➞ []
    fmt.Println(TotalMatch([]string{"hi", "admin"}, []string{"hI", "Hi"}))  // ➞ ["hI", "Hi"]
    fmt.Println(TotalMatch([]string{"hi", "admin"}, []string{"hi", "hi", "admin", "project"}))  // ➞ ["hi", "admin"]
    fmt.Println(TotalMatch([]string{"hi", "admin"}, []string{"hI", "hi", "hi"}))  // ➞ ["hI", "hi", "hi"]
    fmt.Println(TotalMatch([]string{"4"}, []string{"1", "2", "3", "4", "5"}))  // ➞ ["4"]
}
```

This code will print out the results of the TotalMatch function for each of the provided examples.

















































































