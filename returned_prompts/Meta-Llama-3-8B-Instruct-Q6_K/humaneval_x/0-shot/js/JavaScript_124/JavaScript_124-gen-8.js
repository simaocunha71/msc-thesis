Here is the solution in JavaScript:

```javascript
const validDate = (date) => {
    const [month, day, year] = date.split('-');
    if (!date || month.length !== 2 || day.length !== 2 || year.length !== 4) {
        return false;
    }
    month = parseInt(month);
    day = parseInt(day);
    year = parseInt(year);
    if (month < 1 || month > 12 || day < 1 || day > 31) {
        return false;
    }
    if ([4, 6, 9, 11].includes(month) && day > 30) {
        return false;
    }
    if (month === 2 && day > 29) {
        return false;
    }
    if (year % 4 !== 0 || (year % 100 === 0 && year % 400 !== 0)) {
        if (month === 2 && day > 28) {
            return false;
        }
    }
    return true;
};
```

This function splits the date string into month, day, and year. It then checks if the date string is empty, or if the month, day, or year is not in the correct format. If any of these checks fail, it returns false. If the date is in the correct format, it then checks if the month is between 1 and 12, if the day is between 1 and 31, and if the day is within the correct range for the month (e.g., 31 for January, 28 or 29 for February, etc.). If any of these checks fail, it returns false. If all checks pass, it returns true. The function also handles leap years, so it returns false for dates in February that are not valid for a leap year.