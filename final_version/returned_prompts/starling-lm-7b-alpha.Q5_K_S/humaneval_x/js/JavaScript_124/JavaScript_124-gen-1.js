  let date_parts = date.split('-');
  if (date_parts.length != 3 || date.length != 10) {
    return false;
  }

  let [month, day, year] = date_parts;
  if (!Number.isInteger(parseInt(month)) || !Number.isInteger(parseInt(day)) || !Number.isInteger(parseInt(year))) {
    return false;
  }

  if (month < 1 || month > 12 || day < 1 || day > 31 || year < 0) {
    return false;
  }

  if (month == 2 && day > 29) {
    return false;
  }

  if (month == 4 || month == 6 || month == 9 || month == 11) {
    if (day > 30) {
      return false;
    }
  }

  return true;
}



