Here is the JavaScript function that satisfies the problem statement:
```
const sumSquares = (lst) => {
  let sum = 0;
  for (let i = 0; i < lst.length; i++) {
    if (i % 3 === 0 && i % 4 !== 0) {
      sum += lst[i] ** 2;
    } else if (i % 4 === 0 && i % 3 !== 0) {
      sum += lst[i] ** 3;
    } else {
      sum += lst[i];
    }
  }
  return sum;
};
```
Here's an explanation of the code:

* We initialize a variable `sum` to 0, which will store the sum of the modified list.
* We use a `for` loop to iterate over the elements of the input list `lst`.
* For each element, we check three conditions:
	+ If the index `i` is a multiple of 3 and not a multiple of 4, we square the element and add it to the sum.
	+ If the index `i` is a multiple of 4 and not a multiple of 3, we cube the element and add it to the sum.
	+ If the index `i` is not a multiple of 3 or 4, we simply add the original element to the sum.
* Finally, we return the sum.

You can test this function with the examples you provided to see that it produces the expected output.