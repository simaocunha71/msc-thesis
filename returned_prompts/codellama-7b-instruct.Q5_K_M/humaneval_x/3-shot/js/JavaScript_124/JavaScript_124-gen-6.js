  var split_date = date.split('-');

  if (split_date.length != 3) {
    return false;
  }

  var month = parseInt(split_date[0]);
  var day = parseInt(split_date[1]);
  var year = parseInt(split_date[2]);

  if (month < 1 || month > 12) {
    return false;
  }

  if (day < 1 || day > 31) {
    return false;
  }

  if (month == 2) {
    if (day < 1 || day > 28) {
      return false;
    }
  } else if (month == 4 || month == 6 || month == 9 || month == 11) {
    if (day < 1 || day > 30) {
      return false;
    }
  } else {
    if (day < 1 || day > 31) {
      return false;
    }
  }

  return true;
}



