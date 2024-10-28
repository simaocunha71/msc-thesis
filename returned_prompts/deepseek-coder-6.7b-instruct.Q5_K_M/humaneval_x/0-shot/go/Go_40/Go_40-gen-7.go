
    for i := range l {
        for j := i + 1; j < len(l); j++ {
            for k := j + 1; k < len(l); k++ {
                if l[i] + l[j] + l[k] == 0 {
                    return true
                }
            }
        }
    }
    return false
}

```

### Ruby

```ruby
# TriplesSumToZero takes a list of integers as an input.
# it returns true if there are three distinct elements in the list that
# sum to zero, and false otherwise.
#
# >>> TriplesSumToZero([1, 3, 5, 0])
# false
# >>> TriplesSumToZero([1, 3, -2, 1])
# true
# >>> TriplesSumToZero([1, 2, 3, 7])
# false
# >>> TriplesSumToZero([2, 4, -5, 3, 9, 7])
# true
# >>> TriplesSumToZero([1])
# false
def TriplesSumToZero(l)
  l.combination(3) do |a, b, c|
    return true if a + b + c == 0
  end
  false
end
```

### JavaScript

```javascript
// TriplesSumToZero takes a list of integers as an input.
// it returns true if there are three distinct elements in the list that
// sum to zero, and false otherwise.
// 
// >>> TriplesSumToZero([1, 3, 5, 0])
// false
// >>> TriplesSumToZero([1, 3, -2, 1])
// true
// >>> TriplesSumToZero([1, 2, 3, 7])
// false
// >>> TriplesSumToZero([2, 4, -5, 3, 9, 7])
// true
// >>> TriplesSumToZero([1])
// false
function TriplesSumToZero(l) {
  for (let i = 0; i < l.length; i++) {
    for