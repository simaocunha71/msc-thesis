You can use a combination of the map() function and the reduce() function to solve this problem. Here is a possible solution:
```
const oddCount = (lst) => {
  return lst.map((str, i) => {
    const count = str.split('').filter((digit) => digit % 2 !== 0).length;
    return `the number of odd elements ${count}n the str${i+1}ng ${i+1} of the ${i+1}nput.`;
  });
};
```
Here's an explanation of how the