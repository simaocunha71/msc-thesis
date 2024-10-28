  let count = 0
  for(let i = 0; i < lst.length - 1; i++){
    if(lst[i] > lst[i + 1]) count++
  }
  if(count > 1) return false
  return true
}
console.log(isSorted([5])) // ➞ true
console.log(isSorted([1, 2, 3, 4, 5])) // ➞ true
console.log(isSorted([1, 3, 2, 4, 5])) // ➞ false
console.log(isSorted([1, 2, 3, 4, 5, 6])) // ➞ true
console.log(isSorted([1, 2, 3, 4, 5, 6, 7])) // ➞ true
console.log(isSorted([1, 3, 2, 4, 5, 6, 7])) // ➞ false
console.log(isSorted([1, 2, 2, 3, 3, 4])) // ➞ true
console.log(isSorted([1, 2, 2, 2, 3, 4])) // ➞ false

```

## 2. Palindrome

```javascript
