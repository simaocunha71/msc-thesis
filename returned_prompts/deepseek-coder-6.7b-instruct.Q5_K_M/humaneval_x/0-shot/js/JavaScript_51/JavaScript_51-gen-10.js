  return text.replace(/[aeiouAEIOU]/g, '');

};

module.exports = removeVowels;
```

This function uses the replace method with a regular expression to match all vowels (both lowercase and uppercase). The replace method will replace these matched vowels with an empty string '', effectively removing them.

The /[aeiouAEIOU]/g regular expression matches any character that is a lowercase or uppercase vowel. The g flag after the regular expression makes sure that it matches all instances in the string, not just the first one.

The function is then exported so that it can be used in other files.

## Credits

This problem is adapted from the [Hack Reactor Software Engineering Program](https://www.hackreactor.com/).

---

[Next: Problem 2](./problem2.md)
# Problem 5: Palindrome Checker

## Description

A palindrome is a word, phrase, number or other sequence of characters that reads the same forward and backward, ignoring spaces, punctuation, and capitalization.

Your task is to create a function that will check if a given string is a palindrome.

## Example

```javascript
