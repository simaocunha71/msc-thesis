  if (date.length === 0) {
    return false;
  }

  const date_parts = date.split('-');
  if (date_parts.length !== 3) {
    return false;
  }

  const month = parseInt(date_parts[0]);
  if (month < 1 || month > 12) {
    return false;
  }

  const day = parseInt(date_parts[1]);
  if (day < 1 || day > 31) {
    return false;
  }

  const year = parseInt(date_parts[2]);
  if (year < 1000 || year > 9999) {
    return false;
  }

  const days_in_month = (month, year) => {
    switch (month) {
      case 1:
      case 3:
      case 5:
      case 7:
      case 8:
      case 10:
      case 12:
        return 31;
      case 4:
      case 6:
      case 9:
      case 11:
        return 30;
      case 2:
        if (year % 4 === 0 && (year % 100 !== 0 || year % 400 === 0)) {
          return 29;
        } else {
          return 28;
        }
    }
  }

  const days_in_current_month = days_in_month(month, year);
  if (day > days_in_current_month) {
    return false;
  }

  return true;
}



