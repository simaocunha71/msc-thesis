```
const wordsString = (s) => {
  return s.split(/[,\s]+/).filter(word => word !== '');
};
```
Explanation:
The `split()` method is used to split the string into an array of words. The regular expression `/[,\s]+/` matches one or more occurrences of either a comma or a space. The `filter()` method is used to remove any empty strings that may result from the splitting process. The `filter()` method returns a new array with all elements that pass the test implemented by the provided function. In this case, the function checks if the word is not empty (`word !== ''`). If the word is not empty, it is included in the resulting array. The `wordsString()` function returns the resulting array of words.