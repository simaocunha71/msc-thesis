The problem can be solved by iterating over the list and checking if the element at the current index is odd and if the index is even. If both conditions are met, add the element to the sum.

Here is the JavaScript code to solve the problem:
```
const solution = (lst) => {
  let sum = 0;
  for (let i = 0; i < lst.length; i++) {
    if (lst[i] % 2 !== 0 && i % 2 === 0) {
      sum += lst[i];
    }
  }
  return sum;
};
```
Here's an explanation of the code:

* We initialize a variable `sum` to 0, which will store the sum of the odd elements in even positions.
* We iterate over the list using a `for` loop.
* Inside the loop, we check if the current element is odd using the modulo operator (`% 2 !== 0`). If it is odd, we check if the index is even using the modulo operator (`i % 2 === 0`). If both conditions are met, we add the element to the `sum`.
* Finally, we return the `sum` at the end of the function.

You can test the function with the examples provided:
```
console.log(solution([5, 8, 7, 1])); // 12
console.log(solution([3, 3, 3, 3, 3])); // 9
console.log(solution([30, 13, 24, 321])); // 0
```
I hope this helps! Let me know if you have any questions. 😊
```javascript
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python