     newL := make([]int, len(l))
     copy(newL, l)
     sort.Ints(newL)

     for i, v := range l {
         if i%3 == 0 {
             newL[i] = v
         }
     }
     return newL
}

This is not the best solution because it sorts the whole slice and then replaces the values at indices divisible by three with the original values. This is not efficient.

Let's say that we sort the values at indices divisible by three only and leave the others unchanged.

Here is the solution:

```
func SortThird(l []int) []int {
    newL := make([]int, len(l))
    copy(newL, l)
    for i := 0; i < len(l); i += 3 {
        newL[i] = l[i]
    }
    sort.Ints(newL[3:])
    for i, v := range newL[3:] {
        newL[3*i+3] = v
    }
    return newL
}
```
In this solution, we first copy the original list to a new list. Then we sort the values at indices divisible by three in the new list. After that, we sort the values at non-divisible indices (excluding the first one because it is not divisible by three) in the new list. Finally, we replace the values at non-divisible indices in the new list with the sorted values.

This solution is more efficient than the previous one because it only sorts the values at indices divisible by three and does not sort the whole list.
```

This solution sorts the values at indices divisible by three in the new list and then replaces the values at non-divisible indices in the new list with the sorted values. 

The time complexity of this solution is O(n log n) because of the sorting operation. The space complexity is O(n) because of the new list.

Here is the Python version of the solution:

```python
def sort_third(l):
    new_l = l[:]
    for i in range(0, len(l), 3):
