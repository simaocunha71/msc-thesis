```javascript
const solution = (lst) => {
  let sum = 0;
  for(let i = 0; i < lst.length; i++) {
    if(i % 2 === 0 && lst[i] % 2 !== 0) {
      sum += lst[i];
    }
  }
  return sum;
};
```A
Explanation:
The solution uses a for loop to iterate over the list of integers. For each element, it checks if the element is odd (using the modulus operator `%`) and if the position of the element is even (using the modulus operator `%` again). If both conditions are met, it adds the element to the sum. Finally, it returns the sum.

Note: The modulus operator `%` returns the remainder of the division of the number before it by the number after it. So, `i % 2 === 0` checks if the position of the element is even (0, 2, 4, ...), and `lst[i] % 2 !== 0` checks if the element is odd.