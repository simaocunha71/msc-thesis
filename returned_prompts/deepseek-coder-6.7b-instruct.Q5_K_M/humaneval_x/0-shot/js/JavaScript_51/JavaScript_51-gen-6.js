return text.replace(/[aeiouAEIOU]/g, "");

};


A: Here is the solution:

```javascript
const removeVowels = (text) => {
  return text.replace(/[aeiouAEIOU]/g, "");
};
```

The regular expression /[aeiouAEIOU]/g matches any vowel (either lowercase or uppercase) and the replace function replaces these matches with an empty string.

