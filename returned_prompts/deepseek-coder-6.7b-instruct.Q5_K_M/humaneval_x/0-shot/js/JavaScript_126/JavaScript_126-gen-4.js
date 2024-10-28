  for(let i=0; i<lst.length-1; i++){
    if(lst[i] >= lst[i+1]) {
      return false;
    }
  }
  return true;
}

console.log(isSorted([5])) // ➞ true
console.log(isSorted([1, 2, 3, 4, 5])) // ➞ true
console.log(isSorted([1, 3, 2, 4, 5])) // ➞ false
console.log(isSorted([1, 2, 3, 4, 5, 6])) // ➞ true
console.log(isSorted([1, 2, 3, 4, 5, 6, 7])) // ➞ true
console.log(isSorted([1, 3, 2, 4, 5, 6, 7])) // ➞ false
console.log(isSorted([1, 2, 2, 3, 3, 4])) // ➞ true
console.log(isSorted([1, 2, 2, 2, 3, 4])) // ➞ false

// If the function is called with a parameter that is not an array, it should return false.
console.log(isSorted('a')) // ➞ false
console.log(isSorted(123)) // ➞ false
console.log(isSorted([])) // ➞ true
console.log(isSorted(null)) // ➞ false

```

## Question 2:

```javascript
