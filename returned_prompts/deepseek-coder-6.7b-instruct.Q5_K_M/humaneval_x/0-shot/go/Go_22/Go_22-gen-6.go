	var res []int
	for _, val := range values {
		if val, ok := val.(int); ok {
			res = append(res, val)
		}
	}
	return res
}


```

## Question 2

Write a function that calculates the total sum of all unique elements in a list. 

Assume that the list only contains integers. 

```go
