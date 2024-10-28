Here is a JavaScript function that validates a given date string according to the rules mentioned:

```javascript
const validDate = (date) => {
    if (!date) return false;
    const [month, day, year] = date.split('-');
    if (!month || !day || !year) return false;
    if (parseInt(month) < 1 || parseInt(month) > 12) return false;
    if (parseInt(day) < 1 || parseInt(day) > 31) return false;
    if ([4, 6, 9, 11].includes(parseInt(month)) && parseInt(day) > 30) return false;
    if (parseInt(month) === 2) {
        if (parseInt(day) > 29) return false;
        if (isLeapYear(year) && parseInt(day) > 29) return false;
    }
    return true;
};

const isLeapYear = (year) => {
    return (year % 4 === 0 && year % 100 !== 0) || (year % 400 === 0);
};
```

This function first checks if the date string is not empty. Then it splits the date string into month, day, and year parts. It checks if the month, day, and year parts are not empty. Then it checks if the month is within the range 1-12. If not, it returns false.

Then it checks if the day is within the range 1-31. If not, it returns false. For months 4, 6, 9, and 11, it checks if the day is within the range 1-30. If not, it returns false. For the month 2, it checks if the day is within the range 1-29. If not, it returns false. However, it also checks if the year is a leap year and the day is 29. If both conditions are true, it returns true. Otherwise, it returns false.

The isLeapYear function checks if a year is a leap year. It returns true if the year is a leap year, otherwise it returns false.

This function can be used to validate a given date string. For example, validDate('03-11-2000') returns true, validDate('15-01-2012') returns false, validDate('04-0-2040') returns false, validDate('06-04-2020') returns true, and validDate('06