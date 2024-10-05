  return text.replace(/ {2,}/g, '-').replace(/ /g, '_');

}

module.exports = fixSpaces;

// The function fixSpaces takes in a string text.
// It first replaces all instances of 2 or more spaces with a '-' using the replace method with a regular expression.
// Then, it replaces all instances of a single space with an underscore using the replace method with a regular expression.
// The result is returned.

// The regular expressions used in the replace method are as follows:
// {2,} means match 2 or more of the preceding token
// /g is a flag that means global, meaning match all instances, not just the first one.
// In this case, the first replace is for more than two spaces, the second replace is for single spaces.
```



## JavaScript

```javascript
// 