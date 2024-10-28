  var datePattern = /^([0-9]{2})-([0-9]{2})-([0-9]{4})$/;
  var dateArray = date.match(datePattern);
  if (dateArray == null) {
    return false;
  }
  var month = parseInt(dateArray[1]);
  var day = parseInt(dateArray[2]);
  var year = parseInt(dateArray[3]);
  if (month < 1 || month > 12) {
    return false;
  }
  if (day < 1 || day > 31) {
    return false;
  }
  if (month == 2) {
    if ((year % 4 == 0 && year % 100 != 0) || year % 400 == 0) {
      if (day > 29) {
        return false;
      }
    } else {
      if (day > 28) {
        return false;
      }
    }
  } else if (month == 4 || month == 6 || month == 9 || month == 11) {
    if (day > 30) {
      return false;
    }
  }
  return true;
}



