  const [month, day, year] = date.split('-');
  const dateParts = [parseInt(month), parseInt(day), parseInt(year)];

  if (dateParts.some(part => isNaN(part) || part < 1)) {
    return false;
  }

  if (dateParts[1] > 31) {
    if (dateParts[0] === 1 || dateParts[0] === 3 || dateParts[0] === 5 || dateParts[0] === 7 || dateParts[0] === 8 || dateParts[0] === 10 || dateParts[0] === 12) {
      return false;
    }
  }

  if (dateParts[1] > 30) {
    if (dateParts[0] === 4 || dateParts[0] === 6 || dateParts[0] === 9 || dateParts[0] === 11) {
      return false;
    }
  }

  if (dateParts[1] > 29) {
    if (dateParts[0] === 2) {
      return false;
    }
  }

  if (dateParts[0] < 1 || dateParts[0] > 12) {
    return false;
  }

  return true;
}