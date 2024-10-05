  const [month, day, year] = date.split('-');
  if (month.length !== 2 || day.length !== 2 || year.length !== 4) {
    return false;
  }
  month = parseInt(month);
  day = parseInt(day);
  year = parseInt(year);
  if (isNaN(month) || isNaN(day) || isNaN(year)) {
    return false;
  }
  if (month < 1 || month > 12) {
    return false;
  }
  if (day < 1 || day > 31) {
    return false;
  }
  if (month === 2) {
    if (day > 29) {
      return false;
    }
  } else if (month === 4 || month === 6 || month === 9 || month === 11) {
    if (day > 30) {
      return false;
    }
  } else if (month === 1 || month === 3 || month === 5 || month === 7 || month === 8 || month === 10 || month === 12) {
    if (day > 31) {
      return false;
    }
  }
  return true;
} 





