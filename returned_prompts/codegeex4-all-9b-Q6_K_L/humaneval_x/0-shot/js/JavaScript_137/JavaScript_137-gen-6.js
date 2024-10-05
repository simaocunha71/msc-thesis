You can use the isNaN function to check if the variables are numbers or strings. If they are strings, you can use the replace function to replace the commas with dots, then convert them to numbers. Then, you can compare the numbers and return the larger one. If the numbers are equal, return null.

```
const compareOne = (a, b) => {
  a = Number(a.toString().replace(',', '.'))
  b = Number(b.toString().replace(',', '.'))
  if (isNaN(a) || isNaN(b)) return null
  if (a === b) return null
  return a > b ? a : b
}
```