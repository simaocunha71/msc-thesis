  if(!date || date.length !== 10 || date[2] !== '-' || date[5] !== '-') return false;
  let [month, day, year] = date.split('-');
  month = parseInt(month);
  day = parseInt(day);
  year = parseInt(year);
  if(month < 1 || month > 12 || year < 1 || day < 1 || year > 9999) return false;
  if(month === 2) {
      if(day > 29 || (day === 29 && year % 4 !== 0)) return false;
  } else if([4, 6, 9, 11].includes(month)) {
      if(day > 30) return false;
  } else if([1, 3, 5, 7, 8, 10, 12].includes(month)) {
      if(day > 31) return false;
  } else {
      if(day > 31) return false;
  }
  return true;
}

*/
const validDate 
    = (date) 
      =>  {
          if (!date || date.length !== 10 || date[2] !== '-' || date[5] !== '-') return false;
          let [month, day, year] = date.split('-');
          month = parseInt(month);
          day = parseInt(day);
          year = parseInt(year);
          if (month < 1 || month > 12 || year < 1 || day < 1 || year > 9999) return false;
          if (month === 2) {
              if (day > 29 || (day === 29 && year % 4 !== 0)) return false;
          } else if ([4, 6, 9, 11].includes(month)) {
              if (day > 30) return false;
          } else if ([1, 3, 5, 7, 8, 10, 12].includes(month)) {
              if (day > 31) return false;
          } else {
              if (day > 31) return