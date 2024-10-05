```
const flipCase = (string) => {
  return string.split('').map(c => c.toLowerCase() === c ? c.toUpperCase() : c.toLowerCase()).join('');
};
```


Test:
```
console.log(flipCase('Hello')); // Output: "hELLO"
```
Explanation:
This function uses the `split` method to break the string into an array of characters. Then it uses the `map` method to iterate over each character, checking if it's lowercase using `c.toLowerCase() === c`. If it is, it converts it to uppercase using `c.toUpperCase()`, otherwise it leaves it as is. Finally, it uses the `join` method to concatenate the characters back into a string.