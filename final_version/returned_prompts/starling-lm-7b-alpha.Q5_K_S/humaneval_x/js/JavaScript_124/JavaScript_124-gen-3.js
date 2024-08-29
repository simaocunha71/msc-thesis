  const [month, day, year] = date.split('-');
  const isLeap = (year % 4 == 0 && (year % 100 != 0 || year % 400 == 0));

  if (month.length != 2 || day.length != 2 || year.length != 4) {
    return false;
  }

  const monthNumber = parseInt(month, 10);
  const dayNumber = parseInt(day, 10);
  const yearNumber = parseInt(year, 10);

  if (monthNumber < 1 || monthNumber > 12 || yearNumber < 0 || dayNumber < 1 || dayNumber > (isLeap && monthNumber == 2 ? 29 : (monthNumber == 2 ? 28 : (monthNumber == 4 || monthNumber == 6 || monthNumber == 9 || monthNumber == 11 ? 30 : 31)))) {
    return false;
  }

  return true;
}



