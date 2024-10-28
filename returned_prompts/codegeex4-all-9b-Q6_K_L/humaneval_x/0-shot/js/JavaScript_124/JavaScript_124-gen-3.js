```java
const validDate = (date) => {
  if (date.length === 0) { return false; }
  const parts = date.split('-');
  if (parts.length !== 3) { return false; }
  const month = parseInt(parts[0], 10);
  const day = parseInt(parts[1], 10);
  const year = parseInt(parts[2], 10);
  if (month < 1 || month > 12) { return false; }
  if (day < 1 || day > 31) { return false; }
  if (month === 2) {
    if (year % 4 === 0 && (year % 100 !== 0 || year % 400 === 0)) {
      if (day > 29) { return false; }
    } else if (day > 28) { return false; }
  } else if ((month === 4 || month === 6 || month === 9 || month === 11) && day > 30) {
    return false;
  }
  return true;
}
```
