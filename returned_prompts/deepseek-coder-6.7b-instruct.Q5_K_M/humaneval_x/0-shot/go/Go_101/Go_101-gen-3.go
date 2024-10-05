    return strings.FieldsFunc(s, func(r rune) bool {
        return r == ',' || r == ' '
    })
}

```


{{out}}

```txt

["Hi", "my", "name", "is", "John"]
["One", "two", "three", "four", "five", "six"]

```



## Racket


```racket

(define (WordsString str)
  (split-after (lambda (c) (or (char=? c #\space) (char=? c #\,))) str))

(define (split-after pred lst)
  (if (null? lst)
      '()
      (let ((rest (split-after pred (cdr lst))))
        (if (null? rest)
            (list (list (car lst)))
            (if (pred (caar rest))
                (cons (list (car lst)) (cdr rest))
                (cons (cons (car lst) (car rest)) (cdr rest))))))

(define (char=? c1 c2) (equal? (string c1) (string c2)))

;; Test
(WordsString "Hi, my name is John")
(WordsString "One, two, three, four, five, six")

```


{{out}}

```txt

("Hi" "my" "name" "is" "John")
("One" "two" "three" "four" "five" "six")

```



## Ruby


```ruby
def WordsString(s)
  s.split(/,| /)
end

# Test
puts WordsString("Hi, my name is John").inspect
puts WordsString("One, two, three, four, five, six").inspect
```


{{out}}

```txt

["Hi", "my", "name", "is", "John"]
["One", "two", "three", "four", "five", "six"]

```



## Swift


```swift
import Foundation

func Words