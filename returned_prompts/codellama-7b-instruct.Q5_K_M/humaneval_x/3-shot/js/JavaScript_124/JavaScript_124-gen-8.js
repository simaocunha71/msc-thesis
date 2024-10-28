  if (date.length == 0) {
    return false;
  }

  let parts = date.split('-');
  if (parts.length != 3) {
    return false;
  }

  let month = parseInt(parts[0]);
  let day = parseInt(parts[1]);
  let year = parseInt(parts[2]);

  if (month < 1 || month > 12) {
    return false;
  }

  if (day < 1) {
    return false;
  }

  let max_days;
  switch (month) {
    case 1:
    case 3:
    case 5:
    case 7:
    case 8:
    case 10:
    case 12:
      max_days = 31;
      break;
    case 4:
    case 6:
    case 9:
    case 11:
      max_days = 30;
      break;
    case 2:
      if (year % 4 == 0) {
        max_days = 29;
      } else {
        max_days = 28;
      }
      break;
  }

  if (day > max_days) {
    return false;
  }

  return true;
}



