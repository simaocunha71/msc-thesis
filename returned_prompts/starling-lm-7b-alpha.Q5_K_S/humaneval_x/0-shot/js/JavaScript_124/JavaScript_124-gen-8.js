const [month, day, year] = date.split('-');

if (month === '' || day === '' || year === '') {
  return false;
}

if (month < 1 || month > 12 || day < 1 || day > 31 || year.length !== 4) {
  return false;
}

if (month === '02' && day > 28) {
  return false;
}

if (month === '02' && day === '29' && (year % 4 === 0 && (year % 100 !== 0 || year % 400 === 0)) === false) {
  return false;
}

if (month === '03' || month === '05' || month === '07' || month === '08' || month === '10' || month === '12' && day > 31) {
  return false;
}

if (month === '04' || month === '06' || month === '09' || month === '11' && day > 30) {
  return false;
}

return true;
};

/*
 * 
 * The above code will validate a date string if it's valid or not.
 * It splits the date string into month, day and year and checks if any of the fields are empty.
 * It also checks if the month is between 1 to 12, the day is between 1 to 31 for months 1,3,5,7,8,10,12. And the day is between 1 to 30 for months 4,6,9,11.
 * It also checks if the day is 29 for the month 2 if the year is a leap year.
 * If all the conditions are met, it returns true or false.
 */



/*
 * 
 * The above code will validate a date string if it's valid or not.
 * It splits the date string into month, day and year and checks if any of the fields are empty.
 * It also checks if the month is between 1 to 12, the day is between 1 to 31