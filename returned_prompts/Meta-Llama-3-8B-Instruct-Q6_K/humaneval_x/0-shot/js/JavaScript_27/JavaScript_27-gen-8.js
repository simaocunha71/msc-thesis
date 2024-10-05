```
  return string.split('').map(char => char.toLowerCase() === char ? char.toUpperCase() : char.toLowerCase()).join('');
```


This code uses the `split` method to split the string into an array of individual characters. Then, it uses the `map` method to iterate over this array, applying a transformation to each character.

The transformation checks if the character is already in lowercase (using the `toLowerCase` method) and, if so, converts it to uppercase using the `toUpperCase` method. If the character is not in lowercase (i.e., it's already uppercase), it simply converts it to lowercase using the `toLowerCase` method.

Finally, the `join` method is used to concatenate the transformed characters back into a single string.

For example, if we call `flipCase('Hello')`, the output would be `'hELLO'`.