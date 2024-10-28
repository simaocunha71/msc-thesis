```javascript
const validDate = (date) => {
  if (!date) return false;
  const [month, day, year] = date.split('-');
  if (!isValidMonth(month)) return false;
  if (!isValidDay(day, month)) return false;
  return true;
};

const isValidMonth = (month) => {
  return parseInt(month) >= 1 && parseInt(month) <= 12;
};

const isValidDay = (day, month) => {
  if ([1, 3, 5, 7, 8, 10, 12].includes(parseInt(month))) {
    return parseInt(day) >= 1 && parseInt(day) <= 31;
  } else if ([4, 6, 9, 11].includes(parseInt(month))) {
    return parseInt(day) >= 1 && parseInt(day) <= 30;
  } else if (parseInt(month) === 2) {
    return isValidLeapYear(parseInt(year)) ? parseInt(day) >= 1 && parseInt(day) <= 29 : parseInt(day) >= 1 && parseInt(day) <= 28;
  }
  return false;
};

const isValidLeapYear = (year) => {
  return (year % 4 === 0 && year % 100 !== 0) || year % 400 === 0;
};
```
This solution first checks if the date is not empty. Then it splits the date string into month, day, and year. It checks if the month is valid (between 1 and 12), and if the day is valid for the given month. If the month is February, it also checks if the year is a leap year. If the date is valid, it returns true, otherwise it returns false. The helper functions isValidMonth, isValidDay, and isValidLeapYear are used to check the validity of the month, day, and year respectively.