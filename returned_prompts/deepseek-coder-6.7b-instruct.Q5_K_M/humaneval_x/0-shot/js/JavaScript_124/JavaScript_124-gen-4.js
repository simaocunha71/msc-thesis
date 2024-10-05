  if (date.length === 0) return false;
  const parts = date.split("-");
  if (parts.length !== 3) return false;
  const [month, day, year] = parts;
  if (!/^\d+$/.test(month) || !/^\d+$/.test(day) || !/^\d+$/.test(year)) return false;
  const monthNum = parseInt(month, 10);
  const dayNum = parseInt(day, 10);
  const yearNum = parseInt(year, 10);
  if (monthNum < 1 || monthNum > 12 || dayNum < 1 || yearNum < 1) return false;
  if ([1, 3, 5, 7, 8, 10, 12].includes(monthNum)) {
    if (dayNum > 31) return false;
  } else if ([4, 6, 9, 11].includes(monthNum)) {
    if (dayNum > 30) return false;
  } else if (monthNum === 2) {
    if (dayNum > 29) return false;
  } else {
    return false;
  }
  return true;
};
*/

/*
