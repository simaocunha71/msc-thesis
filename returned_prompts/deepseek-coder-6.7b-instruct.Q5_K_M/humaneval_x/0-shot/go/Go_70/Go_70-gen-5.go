    if len(lst) == 0 {
        return lst
    }

    sort.Ints(lst)

    result := make([]int, len(lst))
    min, max := 0, len(lst)-1

    for i := 0; min <= max; i++ {
        if i%2 == 0 {
            result[i] = lst[min]
            min++
        } else {
            result[i] = lst[max]
            max--
        }
    }

    return result
}

```


### Similar Test Case:
```

Test Case: 1
Input:
StrangeSortList([1, 2, 3, 4])
Expected Output:
[1, 4, 2, 3]

Test Case: 2
Input:
StrangeSortList([5, 5, 5, 5])
Expected Output:
[5, 5, 5, 5]

Test Case: 3
Input:
StrangeSortList([])
Expected Output:
[]

Test Case: 4
Input:
StrangeSortList([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
Expected Output:
[1, 10, 2, 9, 3, 8, 4, 7, 5, 6]

Test Case: 5
Input:
StrangeSortList([11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
Expected Output:
[1, 11, 2, 10, 3, 9, 4, 8, 5, 7, 6]

```


### Similar Test Case:
```

Test Case: 1
Input:
StrangeSortList([1, 2, 3, 4])
Expected Output:
[1, 4, 2, 3]

Test Case: 2
Input:
StrangeSortList([5, 5, 5