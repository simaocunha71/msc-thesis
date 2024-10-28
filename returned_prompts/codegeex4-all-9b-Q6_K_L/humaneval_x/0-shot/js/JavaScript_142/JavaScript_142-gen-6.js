The solution to this problem will be to iterate over the list and for each element, check if its index is a multiple of 3 or 4. If it's a multiple of 3, square the number and if it's a multiple of 4 but not a multiple of 3, cube the number. Finally, add all the numbers to get the sum. Here is the JavaScript code for the same:
```
const sumSquares = (lst) => {
  let sum = 0;
  for(let i = 0; i < lst.length; i++) {
    if(i % 3 === 0) {
      sum += lst[i] * lst[i];
    }
    else if(i % 4 === 0) {
      sum += lst[i] * lst[i] * lst[i];
    }
    else {
      sum += lst[i];
    }
  }
  return sum;
}
```
This solution will work for all the examples given in the problem statement.