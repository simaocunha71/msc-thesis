Here is the JavaScript function that validates a date string according to the rules provided:

```javascript
const validDate = (date) => {
  const [month, day, year] = date.split('-');
  if (!date || !month || !day || !year) {
    return false;
  }
  if (+month < 1 || +month > 12) {
    return false;
  }
  if (+day < 1) {
    return false;
  }
  const maxDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
  if (+day > maxDays[+month - 1]) {
    return false;
  }
  if (+month === 2 && (+day > 29 || (+year % 4 !== 0 && +day > 28))) {
    return false;
  }
  return true;
};
```

This function splits the date string into month, day, and year parts, and then checks each part against the rules. If any of the checks fail, the function returns `false`. If all checks pass, the function returns `true`. The `maxDays` array is used to determine the maximum number of days for each month. For February, the function also checks if the year is a leap year and adjusts the maximum number of days accordingly.