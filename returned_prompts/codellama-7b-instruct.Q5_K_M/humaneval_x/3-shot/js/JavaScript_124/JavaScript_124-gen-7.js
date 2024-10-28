  if (date === '') return false;
  let [month, day, year] = date.split('-');
  if (month > 12 || month < 1) return false;
  if (day > 31 && month !== '02') return false;
  if (day > 30 && month === '02') return false;
  if (year > 2019 || year < 2000) return false;
  if (day === '00') return false;
  return true;
}



