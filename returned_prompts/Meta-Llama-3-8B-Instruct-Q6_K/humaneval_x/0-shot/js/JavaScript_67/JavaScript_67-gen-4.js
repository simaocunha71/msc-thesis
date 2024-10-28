```
const fruitDistribution = (s, n) => {
  let apples = 0, oranges = 0;
  const words = s.split(' ');
  for (let i = 0; i < words.length; i++) {
    if (words[i] === 'apples') {
      apples = parseInt(words[i - 1]);
    } else if (words[i] === 'oranges') {
      oranges = parseInt(words[i - 1]);
    }
  }
  return n - apples - oranges;
};
```



Here is the explanation of the solution:

The function `fruitDistribution` takes two arguments: `s` which is a string representing the number of apples and oranges, and `n` which is an integer representing the total number of fruits in the basket.

First, we initialize two variables `apples` and `oranges` to 0, which will store the number of apples and oranges respectively.

Then, we split the string `s` into an array of words using the `split` method with a space character as the separator.

We then iterate through the array of words using a for loop. If a word is 'apples', we parse the previous word as an integer and store it in the `apples` variable. Similarly, if a word is 'oranges', we parse the previous word as an integer and store it in the `oranges` variable.

Finally, we return the difference between the total number of fruits `n` and the sum of the number of apples and oranges.

For example, if the input string is "5 apples and 6 oranges" and the total number of fruits is 19, the function will return 19 - 5 - 6 = 8, which is the number of mango fruits in the basket.