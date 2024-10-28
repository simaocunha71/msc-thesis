
You can solve this problem by using a brute force approach. The idea is to iterate over all possible triples and check if their sum is a multiple of 3. Here is a sample implementation in Go:

```go
func GetMaxTriples(n int) int {
    a := make([]int, n)
    for i := 0; i < n; i++ {
        a[i] = i*i - i + 1
    }
    count := 0
    for i := 0; i < n; i++ {
        for j := i + 1; j < n; j++ {
            for k := j + 1; k < n; k++ {
                if (a[i] + a[j] + a[k]) % 3 == 0 {
                    count++
                }
            }
        }
    }
    return count
}
```

This solution has a time complexity of O(n^3), where n is the input number. This is because we are iterating over all possible triples of the array. The space complexity is O(n), as we are storing the array a of length n. 

Note that this solution is not efficient for large inputs, as the time complexity is cubic. For larger inputs, a more efficient solution would be needed. 

Also, the problem statement does not specify the range of the input number n. If the range of n is limited, this solution might be acceptable. But if the range of n is not limited, a more efficient solution would be needed. 

One possible optimization is to sort the array a first, and then iterate over the array to find the triples. This can reduce the time complexity to O(n^2 log n), as we can use binary search to find the next element in the array that satisfies the condition a[i] + a[j] + a[k] is a multiple of 3. However, this optimization is only useful if the range of n is large. For small inputs, the original solution might be sufficient. 

Another possible optimization is to use a hash map to store the elements of the array a, and then iterate over the array to find the triples. This can reduce the time complexity to O(n^2), as we can use the hash map to find the next element in the array that satisfies the condition a[i] + a[j] + a[k] is a multiple of 3. However, this optimization is only useful if the range of n