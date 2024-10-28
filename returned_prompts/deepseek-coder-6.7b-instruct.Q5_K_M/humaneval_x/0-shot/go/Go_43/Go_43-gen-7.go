
    for i, num1 := range l {
        for _, num2 := range l[i+1:] {
            if num1 + num2 == 0 {
                return true
            }
        }
    }
    return false
}

```

### JavaScript

```javascript

// PairsSumToZero takes a list of integers as an input.
// it returns true if there are two distinct elements in the list that
// sum to zero, and false otherwise.
// PairsSumToZero([1, 3, 5, 0]) // false
// PairsSumToZero([1, 3, -2, 1]) // false
// PairsSumToZero([1, 2, 3, 7]) // false
// PairsSumToZero([2, 4, -5, 3, 5, 7]) // true
// PairsSumToZero([1]) // false
function PairsSumToZero(l) {
    for (let i = 0; i < l.length; i++) {
        for (let j = i + 1; j < l.length; j++) {
            if (l[i] + l[j] === 0) {
                return true
            }
        }
    }
    return false
}

```

### Java

```java

// PairsSumToZero takes a list of integers as an input.
// it returns true if there are two distinct elements in the list that
// sum to zero, and false otherwise.
// PairsSumToZero(new int[]{1, 3, 5, 0}) // false
// PairsSumToZero(new int[]{1, 3, -2, 1}) // false
// PairsSumToZero(new int[]{1, 2, 3, 7}) // false
// PairsSumToZero(new int[]{2, 4, -5, 3, 5, 7}) // true
// PairsSumToZero(new int[]{1}) // false
public boolean PairsSumToZero(int[] l) {
    for (int i = 0; i < l.length; i++) {
        for (int j = i + 