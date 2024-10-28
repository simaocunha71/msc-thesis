The solution is:

```
const selectWords = (s, n) => {
  const consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ';
  return s.split(' ').filter(word => word.split('').filter(c => consonants.includes(c)).length === n);
}
```

Explanation:

- We start by defining a string `consonants` that contains all the consonants.
- We split the input string `s` into an array of words using the `split(' ')` method.
- We then use the `filter` method to filter out the words that don't contain exactly `n` consonants.
- For each word, we use the `split('')` method to convert it into an array of characters.
- We then use the `filter` method to filter out the characters that are not consonants.
- We use the `length` property to count the number of consonants in the word.
- If the number of consonants is equal to `n`, we keep the word in the resulting array.
- Finally, we return the resulting array.