```js
const fixSpaces = (text) => {
  return text.split(' ').map((item, index, arr) => {
    if (item === '') {
      if (arr[index - 1] === '' && arr[index + 1] === '') {
        return '-';
      } else {
        return '';
      }
    } else {
      return item;
    }
  }).join('_');
}
```