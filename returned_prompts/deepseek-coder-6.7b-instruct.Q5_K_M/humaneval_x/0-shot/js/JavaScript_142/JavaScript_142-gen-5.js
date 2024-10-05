  let sum = 0;

  for(let i = 0; i < lst.length; i++){
    if(i % 3 === 0){
      sum += lst[i] ** 2;
    }else if(i % 4 === 0){
      sum += lst[i] ** 3;
    }else{
      sum += lst[i];
    }
  }

  return sum;
}
*/

//Testing
console.log(sumSquares([1,2,3])); //6
console.log(sumSquares([])); //0
console.log(sumSquares([-1,-5,2,-1,-5])); //-126

//This function works by looping through each element in the array and checking if the index is divisible by 3 or 4. 
//If the index is divisible by 3, the element is squared and added to the sum. 
//If the index is divisible by 4 but not by 3, the element is cubed and added to the sum. 
//If the index is not divisible by 3 or 4, the element is added to the sum as is. 
//The final sum is returned at the end of the function.
```

## 10. Write a JavaScript function that will reverse an array.

```javascript
//Question
/*
