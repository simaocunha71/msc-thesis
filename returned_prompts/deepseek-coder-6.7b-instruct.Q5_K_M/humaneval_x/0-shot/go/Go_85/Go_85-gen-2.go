
    sum := 0
    for i := 1; i < len(lst); i += 2 {
        if lst[i] % 2 == 0 {
            sum += lst[i]
        }
    }
    return sum
}

```



## R

```R
# Given a non-empty list of integers lst. Add the even elements that are at odd indices..
# 
# Examples:
# Add([4, 2, 6, 7]) ==> 返回 2

Add <- function(lst) {
  sum = 0
  for (i in seq(1, length(lst), by=2)) {
    if (lst[i] %% 2 == 0) {
      sum = sum + lst[i]
    }
  }
  return(sum)
}

```



## Racket

```racket
;; Given a non-empty list of integers lst. Add the even elements that are at odd indices..
;; 
;; Examples:
;; (add '(4 2 6 7)) ==> 返回 2

#lang racket
(define (add lst)
  (let ([sum 0])
    (for ((i (in-range 1 (length lst) 2)))
         (when (even? (list-ref lst i))
           (set！sum (+ sum (list-ref lst i)))))
    sum))
```



## Swift

```swift
// Given a non-empty list of integers lst. Add the even elements that are at odd indices..
// 
// Examples:
// add([4, 2, 6, 7]) ➞ 2

func add(lst: [Int]) -> Int {
    var sum = 0
    for i in stride(from: 1, to: lst.count, by: 2) {
        if lst[i] % 2 == 0 {
            sum += lst[i]
        }
    }
    return sum
}
```



## TypeScript
