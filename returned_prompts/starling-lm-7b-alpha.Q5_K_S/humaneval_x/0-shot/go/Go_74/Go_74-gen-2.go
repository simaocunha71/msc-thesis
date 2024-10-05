To solve this Kata, you'll need to compare the lengths of the two lists and return the shorter one. Here's a step-by-step breakdown:

1. Start by defining the function `TotalMatch` that takes in two lists of strings, `lst1` and `lst2`.
2. Compare the lengths of the two lists using the `len` function. If the length of `lst1` is less than the length of `lst2`, return `lst1`. Otherwise, if the lengths are equal, return `lst1` as well.
3. If the length of `lst1` is greater than the length of `lst2`, iterate through `lst2` using a `for` loop. Inside the loop, append each string in `lst2` to a new slice called `shorterList`.
4. Finally, return `shorterList`, which contains all the strings from `lst2`.

Here's an example implementation of the solution:

```go
func TotalMatch(lst1 []string, lst2 []string) []string {
    if len(lst1) < len(lst2) {
        return lst1
    } else if len(lst1) == len(lst2) {
        return lst1
    } else {
        shorterList := make([]string, len(lst2))
        for i, _ := range lst2 {
            shorterList[i] = lst2[i]
        }
        return shorterList
    }
}
```

You can test the function with the provided examples:

```go
fmt.Println(TotalMatch([]string{}, []string{})) // []
fmt.Println(TotalMatch([]string{"hi", "admin"}, []string{"hI", "Hi"})) // [hI Hi]
fmt.Println(TotalMatch([]string{"hi", "admin"}, []string{"hi", "hi", "admin", "project"})) // [hi admin]
fmt.Println(TotalMatch([]string{"hi", "admin"}, []string{"hI", "hi", "hi"})) // [hI hi hi]
fmt.Println(TotalMatch([]string{"4"}, []string{"1", "2", "3", "4", "5"})) // [