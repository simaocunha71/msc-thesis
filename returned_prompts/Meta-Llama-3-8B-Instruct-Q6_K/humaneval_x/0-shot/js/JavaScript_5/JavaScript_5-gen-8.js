```
const intersperse = (numbers, delimeter) => {
  if (!numbers.length) return [];
  return [numbers[0], ...intersperse(numbers.slice(1), delimeter), delimeter];
};
``` 