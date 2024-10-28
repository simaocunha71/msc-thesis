	output := make([]string, len(lst))
	oddCount := 0
	for i, str := range lst {
		for _, ch := range str {
			if int(ch-'0') % 2 != 0 {
				oddCount++
			}
		}
		output[i] = fmt.Sprintf("the number of odd elements %don the str%dng %d of the %dput.", oddCount, oddCount, oddCount, oddCount)
		oddCount = 0
	}
	return output
}

func main() {
	fmt.Println(OddCount([]string{"1234567"}))
	fmt.Println(OddCount([]string{"3", "11111111"}))
}


```



## Racket


```Racket
(require racket/pretty)

(define (OddCount lst)
  (map
   (lambda (str)
     (let ((oddCount (apply + (map (lambda (ch)
 (if (odd? (string->number (string ch)))
                                          1
                                          0))
 (string->list str)))))
       (format "the number of odd elements ~an the string ~a of the input." oddCount oddCount)))
   lst))

(display (OddCount '("1234567"))) (newline)
(display (OddCount '("3" "11111111"))) (newline)
```



## REXX


```REXX
/*REXX program demonstrates a function to count the number of odd digits in a list of numeric strings.*/

numericStrings= '1234567' '3' '11111111'

call OddCount numericStrings

exit

OddCount: procedure; parse arg strings
           do j=1 to words(strings)
           string= word(strings, j)
           oddCount= 0
           do i=1 to length(string)
           digit= subword(string, i, 1)
           if