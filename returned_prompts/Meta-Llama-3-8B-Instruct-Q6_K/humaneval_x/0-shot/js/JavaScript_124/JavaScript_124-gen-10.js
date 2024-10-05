Here is a JavaScript function that implements the rules you specified:

```javascript
const validDate = (date) => {
  const [month, day, year] = date.split('-');
  if (!date || date.length !== 10 || !/[0-9]/.test(date)) {
    return false;
  }
  if (isNaN(Number(year)) || year.length > 4) {
    return false;
  }
  if (isNaN(Number(month)) || month.length > 2 || month.length < 2 || !/[0-9]/.test(month)) {
    return false;
  }
  if (isNaN(Number(day)) || day.length > 2 || day.length < 1 || !/[0-9]/.test(day)) {
    return false;
  }
  const monthNumber = Number(month);
  const dayNumber = Number(day);
  if (monthNumber < 1 || monthNumber > 12) {
    return false;
  }
  if (monthNumber === 2 && dayNumber > 29) {
    return false;
  }
  if (monthNumber === 4 || monthNumber === 6 || monthNumber === 9 || monthNumber === 11) {
    if (dayNumber > 30) {
      return false;
    }
  } else if (monthNumber === 1 || monthNumber === 3 || monthNumber === 5 || monthNumber === 7 || monthNumber === 8 || monthNumber === 10 || monthNumber === 12) {
    if (dayNumber > 31) {
      return false;
    }
  }
  return true;
};
```

This function first splits the date string into month, day, and year components. It then checks each component to ensure it is a number and within the correct range. It also checks that the date string is in the correct format and contains only numbers. Finally, it checks the validity of the date according to the rules you specified. If the date is valid, the function returns true; otherwise, it returns false.