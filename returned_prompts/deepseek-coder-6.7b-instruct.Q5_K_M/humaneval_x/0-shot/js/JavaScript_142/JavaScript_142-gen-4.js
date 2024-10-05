  let sum = 0;
  for(let i = 0; i < lst.length; i++){
    if(i % 3 === 0){
      sum += Math.pow(lst[i], 2);
    }else if(i % 4 === 0){
      sum += Math.pow(lst[i], 3);
    }else{
      sum += lst[i];
    }
  }
  return sum;
}

console.log(sumSquares([1,2,3])) // 6
console.log(sumSquares([])) // 0
console.log(sumSquares([-1,-5,2,-1,-5])) // -126

// This program works by iterating through the given list of integers. If the index of the current item is a multiple of 3, the program 
// squares the item and adds it to the sum. If the index is a multiple of 4 but not 3, the program cubes the item and adds it to the sum. 
// If the index is neither a multiple of 3 nor 4, the program simply adds the item to the sum. After all the items in the list have been 
// processed, the program returns the sum.
// The time complexity of this program is O(n), where n is the length of the list. This is because the program makes one pass through 
// the list of integers. The space complexity is O(1), since the program uses a constant amount of space to store the sum and the indices 
// of the list items.
*/

// You can run the code in your local environment by copying and pasting it into a JavaScript file or console.
```

## 3. Write a JavaScript function that returns the sum of all unique numbers in an array.

```javascript
// Solution:

const sumUniqueNumbers = (arr) => {
  let uniqueNumbers = [...new Set(arr)];
  let sum = uniqueNumbers.reduce((acc, curr) => acc + curr, 0);
  return sum;
};

console.log(sumUniqueNumbers([1, 2, 3, 3, 4, 4, 5