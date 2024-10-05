```
const antiShuffle = (s) => {
  return s.split(' ').map(word => [...word].sort((a, b) => a.charCodeAt(0) - b.charCodeAt(0)).join('')).join(' ');
};
```
In this function, we first split the string into an array of words using the `split(' ')` method. Then, we use `map` to apply a transformation to each word in the array. The transformation is to sort the characters in the word in ascending order based on their ASCII values. We do this by converting each word to an array of characters using ` [...word]`, sorting the array using `sort`, and then joining the sorted array back into a string using `join('')`. Finally, we join the array of sorted words back into a string using `join(' ')`. This gives us the ordered version of the original string.