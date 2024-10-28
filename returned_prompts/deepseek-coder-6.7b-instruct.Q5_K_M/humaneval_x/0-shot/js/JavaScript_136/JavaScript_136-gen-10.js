  let minPositive = null;
  let maxNegative = null;
  
  for(let i = 0; i < lst.length; i++){
    if(lst[i] > 0){
      if(minPositive === null || lst[i] < minPositive){
        minPositive = lst[i];
      }
    } else if(lst[i] < 0){
      if(maxNegative === null || lst[i] > maxNegative){
        maxNegative = lst[i];
      }
    }
  }
  
  return [maxNegative, minPositive];
}

console.log(largestSmallestIntegers([2, 4, 1, 3, 5, 7])); //== [null, 1]
console.log(largestSmallestIntegers([])); //== [null, null]
console.log(largestSmallestIntegers([0])); //== [null, null]

```

### Code Explanation
This code goes through the input list and checks each element to see if it is a positive or negative integer. If it is a positive integer and it's smaller than the current smallest positive integer (which is initially null), it becomes the new smallest positive integer. If it's a negative integer and it's larger than the current largest negative integer (which is initially null), it becomes the new largest negative integer. After going through all the elements, it returns a list with the largest negative integer and the smallest positive integer.

### Complexity Analysis
The time complexity of the code is O(n), where n is the length of the list because it iterates through the list once. The space complexity is O(1), because it only uses a constant amount of extra space to store the largest negative integer, smallest positive integer, and the list itself.

### Testing
The provided code has been tested with the given examples and the test cases provided and works as expected.

```

```

## 11. Write a JavaScript function that takes a number as an argument and returns the factorial of that number.

```javascript
// 