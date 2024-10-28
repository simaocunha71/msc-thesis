Here is a JavaScript function that validates a given date string:

```javascript
const validDate = (date) => {
    const [month, day, year] = date.split('-');
    if (!date.includes('-')) return false;
    if (+month < 1 || +month > 12) return false;
    if (+day < 1) return false;
    switch (+month) {
        case 1:
        case 3:
        case 5:
        case 7:
        case 8:
        case 10:
        case 12:
            if (+day > 31) return false;
            break;
        case 4:
        case 6:
        case 9:
        case 11:
            if (+day > 30) return false;
            break;
        case 2:
            if (+year % 4 === 0 && (+day > 29)) return false;
            else if (+day > 28) return false;
            break;
        default:
            return false;
    }
    return true;
};
```

In this function, we first split the date string into month, day, and year. We then check if the date string includes a hyphen and if the month is within the valid range. If the day is less than 1, we return false. Then, we use a switch statement to check the month and adjust the day range accordingly. For February, we also check if the year is a leap year and adjust the day range accordingly. If the date passes all these checks, we return true; otherwise, we return false.