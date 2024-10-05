  let sum = 0;

  for(let i = 0; i < k; i++){
    if(arr[i].toString().length <= 2){
      sum += arr[i];
    }
  }

  return sum;
}

console.log(addElements([111,21,3,4000,5,6,7,8,9], 4));

```

## 3. Write a JavaScript function that takes an array of integers and returns the sum of all the elements that are multiples of either 3 or 5.

```javascript
