  const [month, day, year] = date.split('-').map(Number);

  if (month < 1 || month > 12 || day < 1 || day > 31) {
    return false;
  }

  if (month === 2) {
    if (day < 1 || day > 29) {
      return false;
    }
  } else if ([4, 6, 9, 11].includes(month)) {
    if (day < 1 || day > 30) {
      return false;
    }
  } else if ([1, 3, 5, 7, 8, 10, 12].includes(month)) {
    if (day < 1 || day > 31) {
      return false;
    }
  }

  return true;
}
