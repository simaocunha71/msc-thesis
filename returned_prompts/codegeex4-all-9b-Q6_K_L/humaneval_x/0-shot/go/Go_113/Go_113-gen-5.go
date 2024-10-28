```go
func OddCount(lst []string) []string {
    for i := range lst {
        count := 0
        for _, c := range lst[i] {
            if (c - '0') % 2 == 1 {
                count++
            }
        }
        lst[i] = "the number of odd elements " + strconv.Itoa(count) + "n the str" + strconv.Itoa(count) + "ng " + strconv.Itoa(count) + " of the " + strconv.Itoa(count) + "nput."
    }
    return lst
}
```
