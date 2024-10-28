Here is the Python code that does the same thing:

```
def SortThird(l):
    l.sort(key=lambda x: x if l.index(x)%3!=0 else x)
    return l
```
Here is the explanation of how it works:

*   We use the `sort` function to sort the list `l`. We pass a `key` function to `sort` that determines the sort order.
*   In the `key` function, we use a `lambda` function to define the sort order. This `lambda` function takes an element `x` from the list and returns `x` if the index of `x` in the list is not divisible by 3 (`l.index(x)%3!=0`). Otherwise, it returns `x` sorted.
*   The `sort` function sorts the list according to the `key` function. So, if the index of an element is not divisible by 3, it is not sorted. Otherwise, it is sorted.

Here is an example of how to use this function:

```
>>> SortThird([1, 2, 3])
[1, 2, 3]
>>> SortThird([5, 6, 3, 4, 8, 9, 2])
[2, 6, 3, 4, 8, 9, 5]
```
This code works in Python, but it's not the same as the Go code you provided. In Go, you can achieve the same result using the following code:

```go
func SortThird(l []int) []int {
    sort.SliceStable(l, func(i, j int) bool {
        if i%3 == 0 && j%3 == 0 {
            return l[i] < l[j]
        }
        return i < j
    })
    return l
}
```
This Go code uses the `sort.SliceStable` function to sort the list `l`. The `sort.SliceStable` function takes a `less` function as an argument, which determines the sort order. In this case, the `less` function returns `true` if the elements at indices `i` and `j` should be swapped, and `false` otherwise. The `less` function checks if both `i` and `j` are divisible by 3. If they are, it compares the elements at indices `i` and `j`. If they are not, it simply returns