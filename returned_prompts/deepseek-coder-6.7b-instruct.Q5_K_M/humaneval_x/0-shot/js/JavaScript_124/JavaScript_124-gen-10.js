  if(!date || date.length != 10 || date[2] != '-' || date[5] != '-') return false;

  let [month, day, year] = date.split('-');

  if(year.length != 4 || month < 1 || month > 12 || day < 1) return false;

  if([4,6,9,11].includes(parseInt(month)) && day > 30) return false;

  if([1,3,5,7,8,10,12].includes(parseInt(month)) && day > 31) return false;

  if(parseInt(month) === 2) {
    if(day > 29) return false;
    if(year % 4 != 0 || (year % 100 === 0 && year % 400 != 0)) return false;
  }

  return true;
};
*/

// This function checks if a year is a leap year or not
const isLeapYear = (year) => {
  return (year % 4 === 0 && year % 100 !== 0) || year % 400 === 0;
};

// This function validates the date
const validDate = (date) => {
  if (!date || date.length !== 10 || date[2] !== '-' || date[5] !== '-') return false;

  const [month, day, year] = date.split('-').map(Number);

  if (year < 1 || year > 9999 || month < 1 || month > 12 || day < 1) return false;

  const maxDays = [31, month === 2 && (isLeapYear(year) ? 29 : 28) || 30, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];

  return day <= maxDays[month];
};

module.exports = validDate;

// Test cases
console.log(validDate('03-11-2000