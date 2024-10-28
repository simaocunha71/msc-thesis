Here is the solution to the problem:

```javascript
const validDate = (date) => {
  if (!date) return false; // 1. The date string is not empty.
  const [month, day, year] = date.split('-').map(Number);
  if (month < 1 || month > 12) return false; // 3. The months should not be less than 1 or higher than 12.
  if (day < 1 || (month === 2 && day > 29) || (month === 4 || month === 6 || month === 9 || month === 11 && day > 30) || (month === 1 || month === 3 || month === 5 || month === 7 || month === 8 || month === 10 || month === 12 && day > 31)) return false; // 2. The number of days is not less than 1 or higher than the number of days in the month.
  return true;
};
```


This function first checks if the input date string is not empty. Then it splits the date string into month, day, and year components and checks if the month is within the valid range (1-12). Then it checks if the day is within the valid range for the given month. If all checks pass, the function returns true, indicating that the date is valid. Otherwise, it returns false.