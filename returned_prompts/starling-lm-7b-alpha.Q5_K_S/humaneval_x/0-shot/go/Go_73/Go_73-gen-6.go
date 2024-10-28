
```go
func SmallestChange(arr []int) int {
	set := make(map[int]int)
	for _, v := range arr {
		set[v]++
	}
	count := 0
	for i := 0; i < len(arr)/2; i++ {
		if set[arr[i]] > 1 {
			count += set[arr[i]] - 1
			set[arr[i]]--
		} else {
			count += 1
		}
		if set[arr[len(arr)-i-1]] > 1 {
			count += set[arr[len(arr)-i-1]] - 1
			set[arr[len(arr)-i-1]]--
		} else {
			count += 1
		}
	}
	if len(arr)%2 == 1 {
		if set[arr[len(arr)/2]] == 0 {
			count++
		}
	}
	return count
}
```

In this solution, we create a map to store the counts of each element in the array. Then we iterate over the first half of the array and the second half of the array. If the count of an element is greater than one, we subtract one from the count and decrease the change count by one. Otherwise, we increment the change count by one. After the loop, if the length of the array is odd, we check if the count of the middle element is zero and increment the change count by one if it is. Finally, we return the change count.

This solution has a time complexity of O(n) and a space complexity of O(n), where n is the length of the array.

```go
```

Explanation:
To solve this problem, we first create a map called `set` to store the counts of each element in the input array. We then iterate over the first half of the array and the second half of the array. If the count of an element is greater than one, we subtract one from the count and decrease the change count by one. Otherwise, we increment the change count by one. After the loop