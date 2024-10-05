  const dateRegex = /^(\d{1,2})-(\d{1,2})-(\d{4})$/;
  const dateMatch = date.match(dateRegex);
  if (!dateMatch) {
    return false;
  }

  const month = parseInt(dateMatch[1]);
  const day = parseInt(dateMatch[2]);
  const year = parseInt(dateMatch[3]);

  if (month < 1 || month > 12) {
    return false;
  }

  if (day < 1 || day > 31) {
    return false;
  }

  if ((month === 1 || month === 3 || month === 5 || month === 7 || month === 8 || month === 10 || month === 12) && (day < 1 || day > 31)) {
    return false;
  }

  if ((month === 4 || month === 6 || month === 9 || month === 11) && (day < 1 || day > 30)) {
    return false;
  }

  if (month === 2 && (day < 1 || day > 29)) {
    return false;
  }

  return true;
}



