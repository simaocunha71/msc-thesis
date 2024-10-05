  const [month, day, year] = date.split('-');
  if (!month || !day || !year) return false;
  if (parseInt(month) < 1 || parseInt(month) > 12) return false;
  if (parseInt(day) < 1 || parseInt(day) > 31) return false;
  if (parseInt(month) === 2 && parseInt(day) > 29) return false;
  if (parseInt(month) === 4 || parseInt(month) === 6 || parseInt(month) === 9 || parseInt(month) === 11 && parseInt(day) > 30) return false;
  if (parseInt(month) === 1 || parseInt(month) === 3 || parseInt(month) === 5 || parseInt(month) === 7 || parseInt(month) === 8 || parseInt(month) === 10 || parseInt(month) === 12 && parseInt(day) > 31) return false;
  return true;
}