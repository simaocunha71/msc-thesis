  if  (date.length != 10 || date[2] != '-' || date[5] != '-')  return false;

  let [month, day, year] = [date.slice(0,2), date.slice(3,5), date.slice(6)];

  month = parseInt(month);
  day = parseInt(day);
  year = parseInt(year);

  if  (month < 1 || month > 12 || year < 1 || day < 1 || year > 9999)  return false;

  let  max_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];

  if  (day > max_days[month-1])  return false;

  return true;
}



