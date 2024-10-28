  const dateRegex = /^(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])-(\d{4})$/;
  if (!dateRegex.test(date)) return false;
  const [mm, dd, yyyy] = date.split('-');
  const isLeapYear = (year) => year % 400 === 0 || (year % 100 !== 0 && year % 4 === 0);
  const daysInMonth = [31, (isLeapYear(yyyy) ? 29 : 28), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
  return dd <= daysInMonth[mm - 1];
}

Explanation:
We first check if the date string matches the expected format (mm-dd-yyyy) using a regular expression. If it doesn't match, we return false immediately.

Then we split the date string into its components (mm, dd, yyyy).

We check if the year is a leap year by checking if it is divisible by 400 or not divisible by 100 but divisible by 4.

We then define an array daysInMonth which holds the number of days in each month. Note that February has 29 days if the year is a leap year and 28 otherwise.

Finally, we check if the day number dd is less than or equal to the number of days in the corresponding month mm. If it is, we return true; otherwise, we return false.

This function works for any date in the range 01-01-0000 to 12-31-9999.
*/

//Test Cases
console.log(validDate('03-11-2000')); //true
console.log(validDate('15-01-2012')); //false
console.log(validDate('04-0-2040')); //false
console.log(validDate