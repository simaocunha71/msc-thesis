Here's one way you can solve this problem:

```javascript
const validDate = (date) => {
  const regex = /^(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])-(19|20)\d{2}$/;
  const [month, day, year] = date.split('-');

  if (!regex.test(date)) return false;
  if (month < 1 || month > 12) return false;
  if (day < 1 || day > 31) return false;
  if ((month === 4 || month === 6 || month === 9 || month === 11) && day > 30) return false;
  if (month === 2) {
    if ((year % 4 === 0 && year % 100 !== 0) || year % 400 === 0) {
      if (day > 29) return false;
    } else {
      if (day > 28) return false;
    }
  }

  return true;
};
```

This solution first checks if the date is in the correct format using a regular expression. Then it checks if the month and day values are within the valid ranges. Finally, it checks if the date is valid for February by taking into account leap years.