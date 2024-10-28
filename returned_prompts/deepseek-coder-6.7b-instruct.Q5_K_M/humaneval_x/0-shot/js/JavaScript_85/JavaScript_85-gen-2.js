  let sum = 0;
  for(let i = 1; i < lst.length; i += 2){
    if(lst[i] % 2 === 0) sum += lst[i];
  }
  return sum;
}


console.log(add([4, 2, 6, 7])) // 2
console.log(add([1, 2, 3, 4, 5, 6, 7, 8, 9])) // 12


//Explanation:

In the given examples, the numbers at odd indices are 2, 6, 8, and their sum is 2.

And in the example [1, 2, 3, 4, 5, 6, 7, 8, 9], the numbers at odd indices are 2, 4, 6, 8 and their sum is 2 + 4 + 6 + 8 = 20.
*/
```

### JavaScript Arrays: `.slice()`

```javascript
/*
