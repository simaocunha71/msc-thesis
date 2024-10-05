To solve this Kata, you should follow these steps:

1. Initialize a variable called `total1` to store the total number of characters in all strings of `lst1`. You can calculate this by iterating over `lst1` and summing up the length of each string using the built-in `len` function.
2. Initialize a variable called `total2` to store the total number of characters in all strings of `lst2`. You can calculate this in a similar way to `total1`.
3. If `total1` is less than `total2`, return `lst1`. Otherwise, return `lst2`.
4. If `total1` is equal to `total2`, return the first list, which is `lst1`.

Here's the implementation of the solution in Go:

```go
func TotalMatch(lst1 []string, lst2 []string) []string {
    total1 := 0
    for _, s := range lst1 {
        total1 += len(s)
    }

    total2 := 0
    for _, s := range lst2 {
        total2 += len(s)
    }

    if total1 < total2 {
        return lst1
    } else if total1 == total2 {
        return lst1
    } else {
        return lst2
    }
}
```

You can test the function with the provided examples:

```go
fmt.Println(TotalMatch([]string{}, []string{}))        // []
fmt.Println(TotalMatch([]string{"hi", "admin"}, []string{"hI", "Hi"})) // [hI Hi]
fmt.Println(TotalMatch([]string{"hi", "admin"}, []string{"hi", "hi", "admin", "project"})) // [hi admin]
fmt.Println(TotalMatch([]string{"hi", "admin"}, []string{"hI", "hi", "hi"})) // [hI hi hi]
fmt.Println(TotalMatch([]string{"4"}, []string{"1", "2", "3", "4", "5"})) // [4]
```

The output will match the expected results from the Kata description.

Note that this solution assumes that