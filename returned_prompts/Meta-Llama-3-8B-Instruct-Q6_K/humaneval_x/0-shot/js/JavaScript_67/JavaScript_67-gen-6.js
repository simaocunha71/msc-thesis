The solution for this task is:

```javascript
const fruitDistribution = (s, n) => {
  const words = s.split(' ');
  let apples = 0;
  let oranges = 0;
  for (let i = 0; i < words.length; i++) {
    if (words[i].includes('apples')) {
      apples = parseInt(words[i].replace('apples', '').trim());
    }
    if (words[i].includes('oranges')) {
      oranges = parseInt(words[i].replace('oranges', '').trim());
    }
  }
  return n - apples - oranges;
};
```


This function splits the string into words and then iterates over each word to find the number of apples and oranges. It then subtracts the number of apples and oranges from the total number of fruits in the basket. The result is the number of mango fruits in the basket.