  const [month, day, year] = date.split('-');
  if (!month || !day || !year) {
    return false;
  }
  if (+month < 1 || +month > 12) {
    return false;
  }
  if (+day < 1 || (+month === 2 && +day > 29) || (+month === 4 || +month === 6 || +month === 9 || +month === 11) && +day > 30 || (+month === 1 || +month === 3 || +month === 5 || +month === 7 || +month === 8 || +month === 10 || +month === 12) && +day > 31) {
    return false;
  }
  return true;
}  // This function will validate the date in mm-dd-yyyy format. It will check if the date is in the correct format and if the month and day are within the valid range.