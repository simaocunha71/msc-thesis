  var date_parts = date.split('-');
  var month = parseInt(date_parts[0]);
  var day = parseInt(date_parts[1]);
  var year = parseInt(date_parts[2]);

  if (month < 1 || month > 12 || day < 1 || day > 31 || year < 1) {
    return false;
  }

  if (month == 2) {
    if (day > 29) {
      return false;
    }
  } else if (month == 4 || month == 6 || month == 9 || month == 11) {
    if (day > 30) {
      return false;
    }
  }

  return true;
}