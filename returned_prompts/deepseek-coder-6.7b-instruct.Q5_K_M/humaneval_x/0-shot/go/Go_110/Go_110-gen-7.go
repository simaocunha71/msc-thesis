
// The function iterates over lst1 and checks if any of the numbers in lst1 are odd.
// If an odd number is found, we check lst2 for an even number that can replace it.
// If we find an even number in lst2, we exchange the odd number in lst1 with the even number in lst2.
// If we cannot find an even number in lst2 to replace an odd number in lst1, then we return "NO".
// If we are able to replace all odd numbers in lst1 with even numbers from lst2, then we return "YES".

	for i := 0; i < len(lst1); i++ {
		if lst1[i] % 2 != 0 {
			found := false
			for j := 0; j < len(lst2); j++ {
				if lst2[j] % 2 == 0 {
					lst1[i], lst2[j] = lst2[j], lst1[i]
					found = true
					break
				}
			}
			if !found {
				return "NO"
			}
		}
	}
	return "YES"
}

func main() {
	fmt.Println(Exchange([]int{1, 2, 3, 4}, []int{1, 2, 3, 4})) // "YES"
	fmt.Println(Exchange([]int{1, 2, 3, 4}, []int{1, 5, 3, 4})) // "NO"
}

```

### Python
```python
def exchange(lst1, lst2):
    for i in range(len(lst1)):
        if lst1[i] % 2 != 0:
            for j in range(len(lst2)):
                if lst2[j] % 2 == 0:
                    lst1[i], lst2[j] = lst2[j], lst1[i]
                    break
            else:
                return "NO"
    return "YES"

print(exchange([