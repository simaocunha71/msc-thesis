
	result := make([]int, len(l))
	for i, v := range l {
		result[i] = v + 1
	}
	return result
}

func main() {

	a := []int{1, 2, 3}
	b := []int{5, 3, 5, 2, 3, 3, 9, 0, 123}
	fmt.Println(IncrList(a))
	fmt.Println(IncrList(b))
}

```


{{out}}

```txt

[2, 3, 4]
[6, 4, 6, 3, 4, 4, 10, 1, 124]

```



## R


```R
# Return list with elements incremented by 1.
IncrList <- function(l) {
  return(l + 1)
}

a <- c(1, 2, 3)
b <- c(5, 3, 5, 2, 3, 3, 9, 0, 123)

print(IncrList(a))
print(IncrList(b))
```


{{out}}

```txt

[1] 2 3 4
[1]  6 4 6 3 4 4 10  1 124

```



## Racket


```racket
;; Return list with elements incremented by 1.
(define (IncrList lst)
  (map add1 lst))

(define a '(1 2 3))
(define b '(5 3 5 2 3 3 9 0 123))

(IncrList a)
(IncrList b)
```


{{out}}

```txt
'(2 3 4)
'(6 4 6 3 4 4 10 1 124)'
```



## REXX


```rexx
/*REXX program