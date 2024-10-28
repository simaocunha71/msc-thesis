Here is a JavaScript function that solves the problem:
```
const wordsString = (s) => s.replace(/,| /g, ' ').split(/\s+/);
```
Here's an explanation of the code:

* `s.replace(/,| /g, ' ')`