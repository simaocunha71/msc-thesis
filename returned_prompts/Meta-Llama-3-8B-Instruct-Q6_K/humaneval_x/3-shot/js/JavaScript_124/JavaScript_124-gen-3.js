  const [month, day, year] = date.split('-');
  if (!month || !day || !year) return false;

  if (isNaN(parseInt(month)) || isNaN(parseInt(day)) || isNaN(parseInt(year))) return false;

  month = parseInt(month);
  day = parseInt(day);
  year = parseInt(year);

  if (month < 1 || month > 12) return false;

  if (month === 2) {
    if (day < 1 || day > 29) return false;
  } else if (month === 4 || month === 6 || month === 9 || month === 11) {
    if (day < 1 || day > 30) return false;
  } else {
    if (day < 1 || day > 31) return false;
  }

  return true;
}  // end of function  validDate



