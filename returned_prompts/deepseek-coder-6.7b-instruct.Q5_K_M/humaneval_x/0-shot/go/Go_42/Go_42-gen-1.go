
	incrList := make([]int, len(l))
	for i, v := range l {
		incrList[i] = v + 1
	}
	return incrList
}

func main() {
	
	// Test cases
	l1 := []int{1, 2, 3}
	fmt.Println(IncrList(l1)) // [2, 3, 4]

	l2 := []int{5, 3, 5, 2, 3, 3, 9, 0, 123}
	fmt.Println(IncrList(l2)) // [6, 4, 6, 3, 4, 4, 10, 1, 124]

}


```


{{Out}}

```txt

[2, 3, 4]
[6, 4, 6, 3, 4, 4, 10, 1, 124]

```



## R


```R
IncrList <- function(l) {
    return(l + 1)
}

# Test cases
l1 <- c(1, 2, 3)
print(IncrList(l1))  # [1] 2 3 4

l2 <- c(5, 3, 5, 2, 3, 3, 9, 0, 123)
print(IncrList(l2))  # [1] 6 4 6 3 4 4 10 1 124
```



## Racket


```racket

#lang racket
(define (IncrList lst)
  (map add1 lst))

(IncrList '(1 2 3)) ; '(2 3 4)
(IncrList '(5 3 5 2 3 3 9 0 123)) ; '(6 4 6 3 4 4 10 1 124)

```



