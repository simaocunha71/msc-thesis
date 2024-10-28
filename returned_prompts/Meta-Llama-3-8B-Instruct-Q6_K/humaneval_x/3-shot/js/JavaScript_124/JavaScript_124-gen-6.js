  if (!date) return false;

  let [month, day, year] = date.split('-');
  month = parseInt(month);
  day = parseInt(day);
  year = parseInt(year);

  if (month < 1 || month > 12) return false;
  if (day < 1 || day > 31) return false;

  if ([1, 3, 5, 7, 8, 10, 12].includes(month)) {
    if (day > 31) return false;
  } else if ([4, 6, 9, 11].includes(month)) {
    if (day > 30) return false;
  } else if (month == 2) {
    if (day > 29) return false;
  }

  return true;
}
// validDate('03-11-2000') => true
// validDate('15-01-2012') => false
// validDate('04-0-2040') => false
// validDate('06-04-2020') => true
// validDate('06/04/2020') => false
// validDate('05-05-2015') => true
// validDate('02-30-2010') => false
// validDate('12-31-2010') => true
// validDate('01-01-2010') => true
// validDate('12-35-2010') => false
// validDate('') => false
// validDate('13-05-2015') => false
// validDate('05-05-0000') => false
// validDate('05-05-9999') => true
// validDate('05-05-') => false
// validDate('05-05') => false
// validDate('05-05-2010-') => false
// validDate('05-05-2010-5') => false
// validDate('05-05-2010-05-05') => false
// validDate('05-05-2010-05-05-2010') => false
// validDate('05-05-2010-05-05-2010-05') => false
// validDate('05-05-2010-05-05-2010-05-05') => false
// validDate('05-05-2010-