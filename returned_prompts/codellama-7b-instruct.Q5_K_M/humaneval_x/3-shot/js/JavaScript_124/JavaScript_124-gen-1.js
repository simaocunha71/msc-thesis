  var date_parts = date.split('-');
  var month = parseInt(date_parts[0]);
  var day = parseInt(date_parts[1]);
  var year = parseInt(date_parts[2]);

  // check if date is not empty
  if (date == '') {
    return false;
  }

  // check if the number of days is valid for the month
  if (month == 1 || month == 3 || month == 5 || month == 7 || month == 8 || month == 10 || month == 12) {
    if (day < 1 || day > 31) {
      return false;
    }
  } else if (month == 4 || month == 6 || month == 9 || month == 11) {
    if (day < 1 || day > 30) {
      return false;
    }
  } else if (month == 2) {
    if (day < 1 || day > 29) {
      return false;
    }
  }

  // check if the month is valid
  if (month < 1 || month > 12) {
    return false;
  }

  // check if the date is in the format mm-dd-yyyy
  if (date_parts.length != 3) {
    return false;
  }

  // check if the date is not in the format mm/dd/yyyy
  if (date.indexOf('/') != -1) {
    return false;
  }

  return true;
}



