  if  (/^\d\d-\d\d-\d\d\d\d$/.test(date) === false)  {
    return false;
  }

  const [month, day, year] = date.split('-').map(Number);

  if  (month  != Math.floor(month) 
    || day  != Math.floor(day) 
    || year  != Math.floor(year) 
    || month  < 1 
    || month  > 12 
    || year  < 1)  {
    return false;
  }

  const  days_in_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];

  if  (day  > days_in_month[month - 1] 
    || day  < 1)  {
    return false;
  }

  return true;
}



