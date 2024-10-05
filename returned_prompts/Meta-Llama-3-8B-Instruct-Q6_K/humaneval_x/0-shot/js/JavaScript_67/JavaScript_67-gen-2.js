Here is the solution to the problem:

```javascript
const fruitDistribution = (s, n) => {
  const words = s.split(' ');
  let totalApples = 0;
  let totalOranges = 0;

  for (let i = 0; i < words.length; i++) {
    if (words[i].includes('apples')) {
      totalApples = parseInt(words[i].split(' ')[0]);
    }
    if (words[i].includes('oranges')) {
      totalOranges = parseInt(words[i].split(' ')[0]);
    }
  }

  return n - totalApples - totalOranges;
};
```


This function takes a string `s` and an integer `n` as inputs. It first splits the string into words using the `split()` method with a space character as the separator. Then, it iterates over the words to find the numbers of apples and oranges. The numbers are parsed using the `parseInt()` method. Finally, it returns the difference between `n` and the total number of apples and oranges.

For example, if the input is `fruitDistribution("5 apples and 6 oranges", 19)`, the function will split the string into `["5", "apples", "and", "6", "oranges"]`, find the numbers `5` and `6`, and return `19 - 5 - 6 = 8`. Similarly, for `fruitDistribution("0 apples and 1 oranges", 3)`, the function will return `3 - 0 - 1 = 2`. And so on.