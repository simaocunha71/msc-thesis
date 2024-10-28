```
const flipCase = (string) => {
  return string.split('').map(char => char.toLowerCase() === char ? char.toUpperCase() : char.toLowerCase()).join('');
};
```


Explanation:
The solution uses the `split` method to split the input string into an array of individual characters. Then, it uses the `map` method to iterate over each character and apply the desired transformation.

The condition `char.toLowerCase() === char` checks if the character is currently lowercase. If it is, the `map` method calls `toUpperCase()` on it to convert it to uppercase. If the character is not lowercase (i.e., it's uppercase), the `map` method calls `toLowerCase()` on it to convert it to lowercase.

Finally, the `join`` method is used to concatenate the transformed characters back into a string. This string is then returned by the `flipCase` function.