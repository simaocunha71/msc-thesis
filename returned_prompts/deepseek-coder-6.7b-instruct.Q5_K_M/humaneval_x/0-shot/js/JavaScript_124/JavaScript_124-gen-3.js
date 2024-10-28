  const dateRegex = /^(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])-[0-9]{4}$/;
  if(!dateRegex.test(date)) return false;

  const [month, day, year] = date.split('-');

  const isLeapYear = (year) => (year % 4 == 0 && year % 100 != 0) || (year % 400 == 0);
  const daysInMonth = [31, isLeapYear(year) ? 29 : 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
  
  return day <= daysInMonth[month - 1];
};

console.log(validDate('03-11-2000')); // true
console.log(validDate('15-01-2012')); // false
console.log(validDate('04-0-2040'));  // false
console.log(validDate('06-04-2020')); // true
console.log(validDate('06/04/2020')); // false

In this function, we first use a regular expression to check if the date string matches the 'mm-dd-yyyy' format. If it doesn't, we return false.

Then we split the date string into its components (month, day, and year) and check if the day is less than or equal to the number of days in the corresponding month.

To check if the year is a leap year, we use the formula (year % 4 == 0 && year % 100 != 0) || (year % 400 == 0). This formula checks if a year is divisible by 4, but not by 100, or if it's divisible by 400.

If the day is less than or equal to the number of days in the month, the function returns true; otherwise, it returns false.
*/
