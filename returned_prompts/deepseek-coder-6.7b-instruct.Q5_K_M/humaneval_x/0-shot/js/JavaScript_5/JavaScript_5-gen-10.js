  let newArray = []
  for(let i = 0; i < numbers.length; i++){
    newArray.push(numbers[i])
    if(i < numbers.length - 1){
      newArray.push(delimeter)
    }
  }
  return newArray
}

console.log(intersperse([], 4)) // []
console.log(intersperse([1, 2, 3], 4)) // [1, 4, 2, 4, 3]

// The above code works by iterating over the elements in the input list 'numbers', and for each element, it adds the element and the delimiter to a new list 'newArray'. If the current element is the last one in the input list, it does not add the delimiter after the element.

// The time complexity of the solution is O(n), where n is the number of elements in the input list 'numbers', because we are iterating over the elements of the input list once.

// The space complexity of the solution is O(n), because the new list 'newArray' stores all the elements of the input list 'numbers' plus the delimiters.

// It is important to note that this solution does not modify the input list 'numbers'. Instead, it creates and returns a new list.
```

### Solution 2
```javascript
