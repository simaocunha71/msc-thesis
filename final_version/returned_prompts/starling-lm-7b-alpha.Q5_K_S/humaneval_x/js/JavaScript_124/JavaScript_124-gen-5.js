  const regex = /\d{2}-\d{2}-\d{4}/;
  if (!regex.test(date)) {
    return false;
  }
  const parts = date.split('-');
  const month = parts[0];
  const day = parts[1];
  const year = parts[2];
  if (month < 1 || month > 12) {
    return false;
  }
  if (day < 1 || day > 31) {
    if (month != 2 && month != 4 && month != 6 && month != 9 && month != 11) {
      return false;
    }
  }
  if (day > 29 || (month == 2 && (year % 4 != 0 || year % 100 == 0 || year % 400 == 0))) {
    return false;
  }

  return true;
}



