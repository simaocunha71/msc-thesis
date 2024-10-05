
	for i := 0; i < len(l)-2; i++ {
		for j := i + 1; j < len(l)-1; j++ {
			for k := j + 1; k < len(l); k++ {
				if l[i]+l[j]+l[k] == 0 {
					return true
				}
			}
		}
	}
	return false
}
```
This code uses a triple nested loop to compare every triplet of numbers in the list. If any triplet of numbers sum to zero, the function returns true. If no such triplet is found after checking all triplets, the function