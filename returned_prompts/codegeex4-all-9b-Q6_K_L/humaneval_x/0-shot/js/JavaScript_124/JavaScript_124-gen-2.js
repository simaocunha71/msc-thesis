```java
const validDate = (date) => {
  let [month, day, year] = date.split('-').map(Number);
  if (month < 1 || month > 12) { return false; }
  if (day < 1 || day > 31) { return false; }
  if ((month === 4 || month === 6 || month === 9 || month === 11) && day > 30) { return false; }
  if (month === 2) {
    if (day > 29) { return false; }
    if (day === 29 && !(year % 4 === 0 && (year % 100 !== 0 || year % 400 === 0))) { return false; }
  }
  return true;
}
```
