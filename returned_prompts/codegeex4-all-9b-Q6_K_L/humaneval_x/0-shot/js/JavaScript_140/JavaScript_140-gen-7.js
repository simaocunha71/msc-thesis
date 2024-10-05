You can use a regular expression to achieve this. The regular expression will replace all spaces with underscores, and then replace all consecutive underscores with a single underscore and a dash.

```javascript
const fixSpaces = (text) => {
  return text.replace(/ /g, '_').replace(/_+/g, '_-');
}
```
This will replace all spaces in the string with underscores, and then replace all consecutive underscores with a single underscore and a dash. For example, "Example   3" will be converted to "_Example-3".