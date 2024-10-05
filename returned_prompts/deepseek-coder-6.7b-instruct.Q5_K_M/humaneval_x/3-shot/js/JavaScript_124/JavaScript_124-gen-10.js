  if  (/^(0[1-9]|1[0-2])-([0-2][0-9]|30|31)-\d{4}$/.test(date)) {
    let [month, day, year] = date.split('-').map(Number);
    if  (day > 31 || (month === 2 && day > 29) || (month === 4 || month === 6 || month === 9 || month === 11) && day > 30)
      return false;
    return true;
   }
   return false;
}



