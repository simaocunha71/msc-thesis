  const regex = /([0-9]{2}-[0-9]{2}-[0-9]{4})/;
  if (date.match(regex) === null) return false;
  const month = parseInt(date.split('-')[0]);
  const day = parseInt(date.split('-')[1]);
  const year = parseInt(date.split('-')[2]);
  if (month < 1 || month > 12) return false;
  if (day < 1 || day > 31) return false;
  if (year < 1900 || year > 2100) return false;
  if (month === 2 && day > 28) return false;
  if (month === 4 || month === 6 || month === 9 || month === 11) {
    if (day > 30) return false;
  }
  if (month === 1 || month === 3 || month === 5 || month === 7 || month === 8 || month === 10 || month === 12) {
    if (day > 31) return false;
  }
  return true;
}



