
    sort.Ints(lst)
    count := 1
    for i := len(lst) - 1; i > 0; i-- {
        if lst[i] == lst[i-1] {
            count += 1
        } else {
            if lst[i] < count {
                count = 1
            } else {
                return lst[i]
            }
        }
    }
    if lst[0] >= count {
        return lst[0]
    }
    return -1
}

// Explaination:
// 1. Sort the list in ascending order.
// 2. Start from the end of the list, count the frequency of each integer.
// 3. If the integer is not greater than the count, reset the count to 1.
// 4. If the integer is greater than the count, return the integer.
// 5. If no such integer is found, return -1.

```

---

#### Solution 2

```go

