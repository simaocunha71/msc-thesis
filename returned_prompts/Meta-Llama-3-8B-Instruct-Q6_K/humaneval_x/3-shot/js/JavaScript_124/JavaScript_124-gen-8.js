  const [month, day, year] = date.split('-').map(Number);
  if (month <= 0 || month > 12 || day <= 0 || day > 31) {
    return false;
  }
  if (month == 2) {
    if (day > 29) {
      return false;
    }
  } else if ([1, 3, 5, 7, 8, 10, 12].includes(month)) {
    if (day > 31) {
      return false;
    }
  } else {
    if (day > 30) {
      return false;
    }
  }
  return true;
} 