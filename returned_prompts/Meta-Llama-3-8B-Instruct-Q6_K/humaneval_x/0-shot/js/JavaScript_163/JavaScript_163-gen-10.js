```
function generateIntegers(a, b) {
  let evenDigits = [];
  for (let i = Math.min(a, b); i <= Math.max(a, b); i++) {
    let str = i.toString();
    for (let j = 0; j < str.length; j++) {
      if (+str[j] % 2 === 0) {
        evenDigits.push(i);
        break;
      }
    }
  }
  return evenDigits.filter((num) => num >= a && num <= b).sort((a, b) => a - b);
}
```



This function works by iterating over all the numbers between a and b (inclusive), converting each number to a string, and checking each digit to see if it is even. If a number has an even digit, it is added to the array. After all numbers have been checked, the array is filtered to only include numbers within the range [a, b] and then sorted in ascending order. The result is an array of all the even digits between a and b, in ascending order.