    sb := []rune(s)
    cb := []rune(c)
    cMap := make(map[rune]bool)
    for _, v := range cb {
        cMap[v] = true
    }
    var res []rune
    for _, v := range sb {
        if _, ok := cMap[v]; !ok {
            res = append(res, v)
        }
    }
    s = string(res)
    r := []rune(s)
    for i := 0; i < len(r)/2; i++ {
        if r[i] != r[len(r)-1-i] {
            return [2]interface{}{s, false}
        }
    }
    return [2]interface{}{s, true}
}

```



## Racket


```racket

#lang racket

(require racket/list)

(define (reverse-delete s c)
  (define c-set (set (string->list c)))
  (define r (filter (lambda (x) (not (set-member? c-set x))) (string->list s)))
  (define rr (reverse r))
  (define result-string (list->string r))
  (define is-palindrome (equal? r rr))
  (list result-string is-palindrome)
  )

(reverse-delete "abcde" "ae")
(reverse-delete "abcdef" "b")
(reverse-delete "abcdedcba" "ab")

```



## REXX


```REXX
/*REXX program deletes characters from one string that are in another string,   */
/*and then checks if the result is a palindrome.                             */

say 'abcde', 'ae'      /*Test the function with the strings "abcde" and "ae". */
say 'abcdef', 'b'      /*Test the function with the strings "abcdef" and "b". */
say 'abcdedcba', 'ab'  /*Test the function with the strings