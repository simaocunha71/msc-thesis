Here is a possible solution in JavaScript:
```
const oddCount = (lst) => {
  return lst.map((str, i) => {
    const count = str.split('').filter(c => parseInt(c) % 2 !== 0).length;
    return `the number of odd elements ${count}n the str${i+1}ng ${i+1} of the ${i+1}nput.`;
  });
};
```
Here's an explanation of the code:

* `lst.map()` is used to iterate over the input list and create a new list with the transformed values.
* `str.split('')` is used to split each string into an array of individual characters.
* `filter(c => parseInt(c) % 2 !== 0)` is used to filter out the odd