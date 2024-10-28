Here is the JavaScript function that solves the problem:
```javascript
const fruitDistribution = (s, n) => {
  const [_, apples, oranges] = s.match(/(\d+) (apples|oranges)/g);
  const applesCount = parseInt(apples);
  const orangesCount = parseInt(oranges.replace('s', '')); // remove the 's' from 'oranges'
  return n - applesCount - orangesCount;
};
```
Here's an explanation of the code:

* The regular expression `/(\d+) (apples|oranges)/g` matches one or more digits followed by either "apples" or "oranges" in the input string `s`. The parentheses around the digits and the "apples" or "oranges" part create capture groups, which are used to extract the matched text.
* The `match` method returns an array of matches, and we use destructuring to extract the first element of the array (`_` is a convention for an unused variable), the second element (apples count), and the third element (oranges count).
* We use `parseInt` to convert the strings to integers.
* Finally, we subtract the apples count and oranges count from the total number of fruits `n` to get the number of mango fruits.

You can test the function with the examples provided in the problem statement:
```javascript
console.log(fruitDistribution("5 apples and 6 oranges", 19)); // 8
console.log(fruitDistribution("0 apples and 1 oranges", 3)); // 2
console.log(fruitDistribution("2 apples and 3 oranges", 100)); // 95
console.log(fruitDistribution("100 apples and 1 oranges", 120)); // 19
```I hope this helps! Let me know if you have any questions.```javascript
```javascript
```javascript
```javascript
```javascript
```javascript
```javascript
```javascript
```javascript
```javascript
```javascript
```javascript
```javascript
```javascript
```javascript
```javascript
```javascript
```javascript
```javascript
```javascript
```javascript
```javascript
```javascript
```javascript
```javascript
```javascript
```javascript
```javascript
```javascript
```javascript
```javascript
```javascript
```javascript
```javascript
```javascript
```javascript
```javascript
```javascript
```javascript
```javascript
```javascript
```javascript
```javascript
```javascript
