  let [month, day, year] = date.split('-');
  if (!month || !day || !year) {
    return false;
  }
  if (isNaN(parseInt(month)) || isNaN(parseInt(day)) || isNaN(parseInt(year))) {
    return false;
  }
  let months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
  if (parseInt(month) < 1 || parseInt(month) > 12) {
    return false;
  }
  if (parseInt(day) < 1 || parseInt(day) > months[parseInt(month) - 1]) {
    return false;
  }
  return true;
}