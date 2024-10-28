  const dateRegex = /^(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])-[0-9]{4}$/;
  if(!date.match(dateRegex)) return false;
  
  const [month, day, year] = date.split('-');
  
  const isLeapYear = (year) => {
    return (year % 4 == 0 && year % 100 != 0) || (year % 400 == 0);
  };
  
  const daysInMonth = [
    null, 
    31, //January
    isLeapYear(year) ? 29 : 28, //February
    31, //March
    30, //April
    31, //May
    30, //June
    31, //July
    31, //August
    30, //September
    31, //October
    30, //November
    31  //December
  ];
  
  return day <= daysInMonth[month];
};

validDate('03-11-2000'); //true
validDate('15-01-2012'); //false
validDate('04-0-2040'); //false
validDate('06-04-2020'); //true
validDate('06/04/2020'); //false
```
This program works by using a regular expression to check if the date string is in the correct format. If it is not, it returns false. Then it splits the date into month, day, and year variables. It also creates a function to determine if the year is a leap year. Finally, it checks if the day is valid for the given month and year. If it is, it returns true; otherwise, it returns false.

This program will work for any date in the Gregorian calendar.
*/















































