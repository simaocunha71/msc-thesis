  const date_parts = date.split('-');

  if (date_parts.length != 3) return false;

  const month = parseInt(date_parts[0]);
  const day = parseInt(date_parts[1]);
  const year = parseInt(date_parts[2]);

  if (month < 1 || month > 12) return false;
  if (day < 1 || day > 31) return false;
  if (year < 1 || year > 9999) return false;

  switch (month) {
    case 1:
    case 3:
    case 5:
    case 7:
    case 8:
    case 10:
    case 12:
      if (day < 1 || day > 31) return false;
      break;
    case 4:
    case 6:
    case 9:
    case 11:
      if (day < 1 || day > 30) return false;
      break;
    case 2:
      if (year % 4 == 0 && day > 29) return false;
      if (year % 4 != 0 && day > 28) return false;
      break;
  }

  return true;
}



