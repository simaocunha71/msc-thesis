  const [month, day, year] = date.split('-');

  if (month.length !== 2 || day.length !== 2 || year.length !== 4) {
    return false;
  }

  if (month < '0' || month > '12') {
    return false;
  }

  if (day < '0' || day > '31') {
    if (month === '02') {
      if (year % 4 === 0 && year % 100 !== 0 || year % 400 === 0) {
        return false;
      } else {
        return true;
      }
    }
    if (month === '01' || month === '03' || month === '05' || month === '07' || month === '08' || month === '10' || month === '12') {
      return false;
    } else {
      return true;
    }
  } else {
    return true;
  }
};



