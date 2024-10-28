```
const digitSum = (s) => {
  let sum = 0;
  for (let i = 0; i < s.length; i++) {
    const charCode = s.charCodeAt(i);
    if (charCode >= 65 && charCode <= 90) { // check if char is uppercase
      sum += charCode; // add charCode to sum
    }
  }
  return sum;
};
```


The provided function `digitSum` iterates over each character in the input string `s`. It uses the `charCodeAt` method to get the ASCII code of each character. Then, it checks if the ASCII code is within the range of uppercase letters (65-90). If it is, it adds the ASCII code to the `sum`. Finally, it returns the total `sum`.

You can test this function with the provided examples to see that it produces the expected results. For instance, `digitSum("abAB")` should return `131`, which is the sum of the ASCII codes of the uppercase characters 'A' and 'B'. Similarly, `digitSum("aAaaaXa")` should return `153`, which is the sum of the ASCII codes of the uppercase characters 'A', 'X', and 'A'.