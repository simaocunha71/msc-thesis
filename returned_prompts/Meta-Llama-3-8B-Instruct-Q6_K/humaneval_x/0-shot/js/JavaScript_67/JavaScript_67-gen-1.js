The problem can be solved by parsing the input string to extract the number of apples and oranges, and then subtracting this number from the total number of fruits in the basket.

Here is the solution in JavaScript:
```
const fruitDistribution = (s, n) => {
  const [apples, oranges] = s.match(/(\d+) apples and (\d+) oranges/);
  const totalApples = parseInt(apples);
  const totalOranges = parseInt(oranges);
  return n - totalApples - totalOranges;
};
```
Here's an explanation of the code:

1. The regular expression `/(\d+) apples and (\d+) oranges/` is used to extract the number of apples and oranges from the input string. The parentheses around `\d+` create capture groups that can be accessed using the `match` method.
2. The `match` method is called on the input string `s` and the regular expression. The method returns an array of matches, where the first element is the entire match and the subsequent elements are the capture groups.
3. The `parseInt` method is used to convert the captured numbers to integers.
4. The total number of fruits in the basket is subtracted from the sum of the total apples and oranges to get the number of mango fruits.

You can test the function with the examples you provided:
```
console.log(fruitDistribution("5 apples and 6 oranges", 19)); // 8
console.log(fruitDistribution("0 apples and 1 oranges", 3)); // 2
console.log(fruitDistribution("2 apples and 3 oranges", 100)); // 95
console.log(fruitDistribution("100 apples and 1 oranges", 120)); // 19
```
I hope this helps! Let me know if you have any questions. 😊

