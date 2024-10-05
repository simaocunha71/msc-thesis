   let even = 0, odd = 0;
   let numArr = Math.abs(num).toString().split('');
   for(let i = 0; i < numArr.length; i++){
     if(numArr[i] % 2 === 0){
       even++;
     } else {
       odd++;
     }
   }
   return [even, odd];
}

console.log(evenOddCount(-12));
console.log(evenOddCount(123));
console.log(evenOddCount(1223445566));
```

The `evenOddCount` function takes an integer as an argument. It converts the integer to a string and splits the string into an array of characters. It then iterates through the array and increments the `even` count if the character is an even number, and the `odd` count if it is an odd number. Finally, it returns an array containing the counts of even and odd numbers.

The `Math.abs` function is used to ensure that the function works correctly even if a negative number is passed in.

The `%` operator is used to check if a number is even or odd. If `numArr[i] % 2 === 0` is true, then `numArr[i]` is an even number. Otherwise, `numArr[i]` is an odd number.

The `return` statement returns an array containing the counts of even and odd numbers.

Finally, the function is called with some sample inputs and the results are logged to the console.

## Task 2

```javascript
