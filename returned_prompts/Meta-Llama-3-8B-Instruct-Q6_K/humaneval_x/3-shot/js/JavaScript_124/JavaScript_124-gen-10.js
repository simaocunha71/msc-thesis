  const [month, day, year] = date.split('-');
  if (!month || !day || !year) return false;

  const daysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
  if (+month < 1 || +month > 12) return false;
  if (+day < 1 || +day > daysInMonth[+month - 1]) return false;

  return true;
}