You can solve this problem by using a regular expression to find spaces and replace them with underscores or hyphens. Here's how you can do it:

```javascript
const fixSpaces = (text) => {
  // Replace spaces with underscores
  text = text.replace(/\s+/g, '_');
  // Replace consecutive underscores with a single underscore
  text = text.replace(/_+/g, '_');
  // Replace more than 2 consecutive underscores with a hyphen
  text = text.replace(/_+/g, (_, g) => g.length > 2 ? '-' : '_');
  return text;
}
```

In this code, we first replace all spaces with underscores using the regular expression `/\s+/g`. Then, we replace consecutive underscores with a single underscore using the regular expression `/_+/g`. Finally, we replace more than 2 consecutive underscores with a hyphen using the regular expression `/_+/g` and a callback function that checks the length of the match.