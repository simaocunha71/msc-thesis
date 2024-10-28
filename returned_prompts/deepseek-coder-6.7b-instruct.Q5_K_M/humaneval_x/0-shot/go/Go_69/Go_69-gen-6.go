
	sort.Ints(lst)
	for i := len(lst) - 1; i >= 0; i-- {
		count := 0
		for j := 0; j < len(lst); j++ {
			if lst[i] == lst[j] {
				count++
			}
		}
		if count >= lst[i] {
			return lst[i]
		}
	}
	return -1
}

func main() {
    fmt.Println(Search([]int{4, 1, 2, 2, 3, 1})) // 2
    fmt.Println(Search([]int{1, 2, 2, 3, 3, 3, 4, 4, 4})) // 3
    fmt.Println(Search([]int{5, 5, 4, 4, 4})) // -1
}
```

This function works by first sorting the list of integers. It then iterates over the list in descending order (from the greatest integer to the smallest). For each integer, it counts the number of occurrences of that integer in the list. If the count is greater than or equal to the integer itself, it returns the integer. If no such integer is found after checking all integers, it returns -1.

This solution has a time complexity of O(n log n) due to the sorting, and a space complexity of O(1) as it only uses a constant amount of extra space.

If you are not allowed to use sort, you can use a map to count the frequency of each integer. The time complexity will be O(n) and the space complexity will be O(n).

```go
func Search(lst []int) int {
    counts := make(map[int]int)
    for _, num := range lst {
        counts[num]++
    }
    for num := len(lst); num > 0; num-- {
        if counts[num] >= num {
            return num
        }
    }
    return -1
}
```

Remember to always test your functions with a variety of inputs to ensure they are working as expected.