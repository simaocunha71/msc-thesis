  var date_parts = date.split('-');
  if (date_parts.length != 3) {
    return false;
  }

  var month = parseInt(date_parts[0]);
  var day = parseInt(date_parts[1]);
  var year = parseInt(date_parts[2]);

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
  } else if (day > 30) {
    return false;
  }

  return true;
}