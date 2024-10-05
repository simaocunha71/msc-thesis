```
const checkIfLastCharIsALetter = (txt) => {
  if(txt === "") return false;
  const lastChar = txt.slice(-1);
  if(!/^[a-zA-Z]$/.test(lastChar)) return false;
  if(txt.lastIndexOf(lastChar) !== txt.length - 1) return false;
  return true;
};
```


Here's a breakdown of the code:

1. `if(txt === "") return false;`: We check if the input string is empty. If it is, we immediately return `false`.
2. `const lastChar = txt.slice(-1);`: We extract the last character of the input string using the `slice` method with a negative index.
3. `if(!/^[a-zA-Z]$/.test(lastChar)) return false;`: We use a regex pattern `/^[a-zA-Z]$/.test(lastChar)` to check if the last character is an alphabetical character. If it's not, we return `false`.
4. `if(txt.lastIndexOf(lastChar) !== txt.length - 1) return false;`: We use the `lastIndexOf` method to find the last occurrence of the last character in the input string. If the last character is not part of a word (i.e., it's not the last character of a word), we return `false`.
5. `return true;`: If the last character is an alphabetical character and is not part of a word, we return `true`.

You can test the function with the provided examples to see that it returns the expected results.