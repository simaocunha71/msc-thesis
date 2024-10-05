  var parts = date.split('-');

  if (parts.length != 3) {
    return false;
  }

  var month = parseInt(parts[0]);
  var day = parseInt(parts[1]);
  var year = parseInt(parts[2]);

  if (month < 1 || month > 12) {
    return false;
  }

  if (day < 1 || day > 31) {
    return false;
  }

  if (month == 2) {
    if (day > 29) {
      return false;
    }
  } else if (day == 31 && (month == 4 || month == 6 || month == 9 || month == 11)) {
    return false;
  }

  if (year < 1900 || year > 2099) {
    return false;
  }

  return true;
}