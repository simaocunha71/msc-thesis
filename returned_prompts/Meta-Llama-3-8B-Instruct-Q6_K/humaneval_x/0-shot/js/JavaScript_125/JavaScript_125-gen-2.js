```javascript
const splitWords = (txt) => {
  if (txt.includes(' ')) {
    return txt.split(' ');
  } else if (txt.includes(',')) {
    return txt.split(',');
  } else {
    return txt