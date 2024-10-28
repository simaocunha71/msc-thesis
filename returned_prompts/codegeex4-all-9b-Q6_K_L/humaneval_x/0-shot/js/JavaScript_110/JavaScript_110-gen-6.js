You can solve this problem by creating two variables, one to keep track of the total number of odd numbers in lst1 and another to keep track of the total number of even numbers in lst2. Then, you can iterate over lst1 and lst2 and exchange the elements if necessary. If the total number of odd numbers in lst1 is less than or equal to the total number of even numbers in lst2, you can return "YES", otherwise "NO".
Here is the code:
```
const exchange = (lst1, lst2) => {
  let oddCount = 0;
  let evenCount = 0;
  for (let num of lst1) {
    if (num % 2 !== 0) {
      oddCount++;
    }
  }
  for (let num of lst2) {
    if (num % 2 === 0) {
      evenCount++;
    }
  }
  if (oddCount <= evenCount) {
    return "YES";
  } else {
    return "NO";
  }
};
```