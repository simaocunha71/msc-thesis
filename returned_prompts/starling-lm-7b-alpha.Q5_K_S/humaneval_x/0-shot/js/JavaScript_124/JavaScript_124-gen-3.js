function validDate(date) {
    const regex = /^(0?[1-9]|1[0-2])\-([0-2][0-9]|3[01])\-([0-9]{4})$/;
    return regex.test(date);
  }

  function isValidDate(day, month, year) {
    if (month === 2) {
      return year % 4 === 0 && day > 0 && day <= 29;
    } else if (month === 4 || month === 6 || month === 9 || month === 11) {
      return day > 0 && day <= 30;
    } else {
      return day > 0 && day <= 31;
    }
  }

  const parts = date.split('-');
  const month = Number(parts[0]);
  const day = Number(parts[1]);
  const year = Number(parts[2]);
  return (
    parts.length === 3 &&
    month >= 1 &&
    month <= 12 &&
    day >= 1 &&
    isValidDate(day, month, year)
  );
}


/*

You have to write a function which validates a given date string and
  returns true if the date is valid otherwise false.
  The date is valid if all of the following rules are satisfied:
  1. The date string is not empty.
  2. The number of days is not less than 1 or higher than 31 days for months 1,3,5,7,8,10,12. And the number of days is not less than 1 or higher than 30 days for months 4,6,9,11. And, the number of days is not less than 1 or higher than 29 for the month 2.
  3. The months should not be less than 1 or higher than 12.
  4. The date should be in the format: mm-dd-yyyy

  for example: 
  validDate('03-11-2000') => true

  validDate('15-01-2012')