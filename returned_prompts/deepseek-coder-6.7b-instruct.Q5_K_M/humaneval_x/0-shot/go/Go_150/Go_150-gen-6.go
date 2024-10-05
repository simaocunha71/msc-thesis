
	isPrime := true

	for i := 2; i * i <= n; i++ {
		if n % i == 0 {
			isPrime = false
			break
		}
	}

	if isPrime {
		return x
	}
	return y
}

// main function to test XOrY function
func main() {

B:

	fmt.Println(XOrY(7, 34, 12))  // should return 34
	fmt.Println(XOrY(15, 8, 5))  // should return 5

}

```



## Racket


```racket

; A simple program which should return the value of x if n is
; a prime number and should return the value of y otherwise.
(define (XOrY n x y)
  (if (prime? n)
      x
      y))

; check if number is prime
(define (prime? n)
  (cond
    [(<= n 1) #f]
    [(<= n 3) #t]
    [(even? n) #f]
    [else
     (let loop ([i 3])
       (cond
         [(> (* i i) n) #t]
         [(zero? (modulo n i)) #f]
         [else (loop (+ i 2))]))]))

; main function to test XOrY function
(display (XOrY 7 34 12))  ; should return 34
(newline)
(display (XOrY 15 8 5))  ; should return 5
(newline)

```



## Rust


```rust
// A simple program which should return the value of x if n is
// a prime number and should return the value of y otherwise.
fn x_or_y(n: i32, x: i32, y: i32) -> i32 {
    if is_prime(n) {
        x
    } else {
        y
    }
}

fn is_prime(n: i