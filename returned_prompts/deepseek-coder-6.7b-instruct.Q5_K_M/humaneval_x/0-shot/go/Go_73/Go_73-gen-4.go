
	count := 0

	for i := 0; i < len(arr)/2; i++ {
		if arr[i] != arr[len(arr)-1-i] {
			count++
		}
	}
	return count
}

```


## 11. Given an array of integers, write a function that finds the missing number in the series.

Example:

```
