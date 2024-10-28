```java
const validDate = (date) => {
  const [month, day, year] = date.split('-').map(Number);
  if (month < 1 || month > 12) return false;
  if ((month === 4 || month === 6 || month === 9 || month === 11) && (day < 1 || day > 30)) return false;
  if ((month === 1 || month === 3 || month === 5 || month === 7 || month === 8 || month === 10 || month === 12) && (day < 1 || day > 31)) return false;
  if (month === 2) {
    if (day < 1 || day > 29) return false;
    if (year % 4 !== 0 && day === 29) return false;
    if (year % 100 === 0 && day === 29) return false;
    if (year % 400 === 0 && day === 29) return false;
  }
  return true;
}
```
