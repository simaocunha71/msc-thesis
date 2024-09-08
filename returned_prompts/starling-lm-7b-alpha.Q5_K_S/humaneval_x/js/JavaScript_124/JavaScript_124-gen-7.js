  const date_parts = date.split("-");
  const month = parseInt(date_parts[0]);
  const day = parseInt(date_parts[1]);
  const year = parseInt(date_parts[2]);

  if (date.length == 0) {
    return false;
  }

  if (day < 1 || day > 31) {
    if (month != 1 && month != 3 && month != 5 && month != 7 && month != 8 && month != 10 && month != 12) {
      return false;
    }
  }

  if (day < 1 || day > 30) {
    if (month == 4 || month == 6 || month == 9 || month == 11) {
      return false;
    }
  }

  if (day < 1 || day > 29) {
    if (month == 2) {
      return false;
    }
  }

  if (month < 1 || month > 12) {
    return false;
  }

  return true;
}



