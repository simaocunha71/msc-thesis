```js
const removeDuplicates = (numbers) => {
  let uniqueNumbers = [];
  for (let number of numbers) {
    if (!uniqueNumbers.includes(number)) {
      uniqueNumbers.push(number);
    }
  }
  return uniqueNumbers;
};
```