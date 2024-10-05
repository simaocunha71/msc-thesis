```
function validDate(date) {
  const [month, day, year] = date.split('-');
  if (!date.includes('-')) return false;

  if (parseInt(month) < 1 || parseInt(month) > 12) return false;
  if (parseInt(day) < 1) return false;

  const daysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
  if (parseInt(month) === 2 && parseInt(day) > daysInMonth[1]) return false;
  if (parseInt(month) === 2 && parseInt(day) <= 29 && parseInt(year) % 4 === 0) return false;
  if (parseInt(day) > daysInMonth[parseInt(month) - 1]) return false;

  return true;
}
```


Explanation:
The function first splits the input date string into an array of strings using the '-' character as a delimiter. It then checks if the month is within the range 1-12 and the day is within the range 1-31. The daysInMonth array is used to store the number of days in each month. If the month is February, the function checks if the day is less than or equal to 29 if the year is a leap year, otherwise it checks if the day is less than or equal to 28. If the day is greater than the number of days in the month, the function returns false. Otherwise, it returns true.

Note that this function does not handle non-numeric input or invalid date formats. It assumes that the input date string is in the format 'mm-dd-yyyy'. If you want to handle other date formats or non-numeric input, you would need to add additional error checking.