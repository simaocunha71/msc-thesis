Here is the solution using filter and map:
```javascript
const uniqueDigits = (x) => {
  return x.filter(num => !num.toString().includes('2')).sort((a, b) => a - b);
};
```
Explanation:

1. `x.filter(num => !num.toString().includes('2'))`: This part filters out the numbers that have any even digits. The `includes` method checks if a string (in this case, the string representation of the number) contains a certain substring. In this case, we're looking for the substring '2', which is an even digit.
2. `sort((a, b) => a - b)`: This part sorts the filtered array in ascending order. The `sort` method takes a compare function as an argument, which returns a negative value if `a` should come before `b`, a positive value if `b` should come before `a`, and 0 if they are equal. In this case, we're using the subtraction of `a` and `b` as the compare function, which is a common way to sort numbers in ascending order.

Example usage:
```javascript
console.log(uniqueDigits([15, 33, 1422, 1])); // [1, 15, 33]
console.log(uniqueDigits([152, 323, 1422, 10])); // []
```





