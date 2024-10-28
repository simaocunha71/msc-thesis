```java
const validDate = (date) => {
  let dateArr = date.split('-');
  if (dateArr.length !== 3 || dateArr[0].length !== 2 || dateArr[1].length !== 2 || dateArr[2].length !== 4) return false;
  let month = Number(dateArr[0]);
  let day = Number(dateArr[1]);
  let year = Number(dateArr[2]);
  if (isNaN(month) || isNaN(day) || isNaN(year)) return false;
  if (month < 1 || month > 12) return false;
  if ((month == 4 || month == 6 || month == 9 || month == 11) && (day < 1 || day > 30)) return false;
  if ((month == 1 || month == 3 || month == 5 || month == 7 || month == 8 || month == 10 || month == 12) && (day < 1 || day > 31)) return false;
  if (month == 2) {
    let leapYear = year % 4 == 0 && (year % 100 != 0 || year % 400 == 0);
    if (day < 1 || (day > 29 && !leapYear) || (day > 28 && leapYear)) return false;
  }
  return true;
}
```
