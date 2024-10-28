Here is the JavaScript function to validate a date string:

```javascript
const validDate = (date) => {
    const [month, day, year] = date.split('-');
    if (!month || !day || !year) return false;
    if (parseInt(month) < 1 || parseInt(month) > 12) return false;
    if (parseInt(day) < 1 || parseInt(day) > 31) return false;
    if (parseInt(month) === 2) {
        if (parseInt(day) > 29) return false;
        const isLeapYear = (year % 4 === 0 && year % 100 !== 0) || (year % 400 === 0);
        if (!isLeapYear && parseInt(day) > 28) return false;
    } else if ([4, 6, 9, 11].includes(parseInt(month))) {
        if (parseInt(day) > 30) return false;
    } else if ([1, 3, 5, 7, 8, 10, 12].includes(parseInt(month))) {
        if (parseInt(day) > 31) return false;
    }
    return true;
}
```
This function takes a date string in the format 'mm-dd-yyyy' and checks if it is valid according to the rules specified. It first splits the date string into month, day, and year, and then checks if each part is present and valid. It also checks if the month and day are within their valid ranges. For February, it checks if the year is a leap year and adjusts the day range accordingly. For the other months, it checks if the day is within the valid range. If the date is valid, it returns true; otherwise, it returns false.