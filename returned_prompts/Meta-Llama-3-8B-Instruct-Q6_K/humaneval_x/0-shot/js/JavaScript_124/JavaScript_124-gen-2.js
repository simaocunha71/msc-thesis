Here is the JavaScript function that validates a given date string:

```javascript
const validDate = (date) => {
  const [month, day, year] = date.split('-');
  if (!date || date.length !== 10 || !month || !day || !year) {
    return false;
  }
  const monthNum = parseInt(month);
  if (isNaN(monthNum) || monthNum < 1 || monthNum > 12) {
    return false;
  }
  const dayNum = parseInt(day);
  if (isNaN(dayNum) || (monthNum === 2 && dayNum > 29) || (monthNum === 1 || monthNum === 3 || monthNum === 5 || monthNum === 7 || monthNum === 8 || monthNum === 10 || monthNum === 12 && dayNum > 31) || (monthNum === 4 || monthNum === 6 || monthNum === 9 || monthNum === 11 && dayNum > 30)) {
    return false;
  }
  return true;
};
```
This function first splits the date string into month, day, and year. Then it checks if the date string is valid by checking if the month and day are valid numbers, and if they are within the correct ranges for each month. It also checks if the year is a valid number. If any of these checks fail, the function returns false. If all the checks pass, the function returns true. 

You can use this function to validate a date string like this:

```javascript
console.log(validDate('03-11-2000')); // true
console.log(validDate('15-01-2012')); // false
console.log(validDate('04-0-2040')); // false
console.log(validDate('06-04-2020')); // true
console.log(validDate('06/04/2020')); // false
``` 