  let result = true;

  let parts = date.split('-');
  if (parts.length != 3) {
    result = false;
  }

  let month = parseInt(parts[0]);
  let day = parseInt(parts[1]);
  let year = parseInt(parts[2]);

  if (month < 1 || month > 12) {
    result = false;
  }
  if (day < 1 || day > 31) {
    result = false;
  }

  if (month == 2) {
    if (day > 29) {
      result = false;
    }
  } else if (month == 4 || month == 6 || month == 9 || month == 11) {
    if (day > 30) {
      result = false;
    }
  } else if (month != 2 && month != 4 && month != 6 && month != 9 && month != 11) {
    if (day > 31) {
      result = false;
    }
  }

  return result;
}



