Here is one possible solution:

```
function validDate(date) {
  if (!date || !date.match(/^(0[1-9]|1[0-2])-([0-2][0-9]|3[0-1])-\d{4}$/)) {
    return false;
  }

  const [month, day, year] = date.split('-').map(Number);

  if (month < 1 || month > 12) {
    return false;
  }

  if (month === 2) {
    if (year % 4 === 0 && (year % 100 !== 0 || year % 400 === 0)) {
      if (day < 1 || day > 29) {
        return false;
      }
    } else {
      if (day < 1 || day > 28) {
        return false;
      }
    }
  } else if (month in [1, 3, 5, 7, 8, 10, 12]) {
    if (day < 1 || day > 31) {
      return false;
    }
  } else {
    if (day < 1 || day > 30) {
      return false;
    }
  }

  return true;
}
```

This solution uses regular expressions to check if the date string matches the specified format. It then splits the date string into month, day, and year. The function checks if the month is within the valid range (1-12) and the day is valid for the given month and year.

For example, the date '03-11-2000' is valid because the month is within the valid range, the day is within the valid range for the month, and the format is correct. The date '15-01-2012' is not valid because the month is within the valid range but the day is not. The date '04-0-2040' is not valid because the format is incorrect. The date '06-04-2020' is valid because the month, day, and format are all