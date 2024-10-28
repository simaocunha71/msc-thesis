To solve this Kata, you'll need to:

Compare the total length of the strings in each list.
If the total length of the strings in `lst1` is less than the total length of the strings in `lst2`, return `lst1`. Otherwise, return `lst2`. If the total length of the strings in each list is the same, return the first list.

Here's a step-by-step explanation of the solution:

Create a variable named `total1` and assign to it the total length of all strings in `lst1`. Similarly, create a variable named `total2` and assign to it the total length of all strings in `lst2`.

Compare the values of `total1` and `total2`. If `total1` is less than `total2`, return `lst1`. Otherwise, return `lst2`. If `total1` and `total2` are equal, return the first list.

Here's the implementation of the solution in Go:

```go
func TotalMatch(lst1 []string, lst2 []string) []string {
    total1 := 0
    for _, v := range lst1 {
        total1 += len(v)
    }

    total2 := 0
    for _, v := range lst2 {
        total2 += len(v)
    }

    if total1 < total2 {
        return lst1
    } else if total1 > total2 {
        return lst2
    } else {
        return lst1
    }
}
```

And here are some test cases to verify the correctness of the solution:

```go
fmt.Println(TotalMatch([]string{}, []string{}))  // []
fmt.Println(TotalMatch([]string{"hi", "admin"}, []string{"hI", "Hi"}))  // [hI Hi]
fmt.Println(TotalMatch([]string{"hi", "admin"}, []string{"hi", "hi", "admin", "project"}))  // [hi admin]
fmt.Println(TotalMatch([]string{"hi", "admin"}, []string{"hI", "hi", "hi"}))  // [hI hi hi]
fmt.Println(TotalMatch([]