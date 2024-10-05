  let regex = /(\d\d)-(\d\d)-(\d\d\d\d)/;
  let match = date.match(regex);
  if (match == null) {
    return false;
  }
  let month = parseInt(match[1]);
  let day = parseInt(match[2]);
  let year = parseInt(match[3]);
  if (month < 1 || month > 12) {
    return false;
  }
  if (day < 1) {
    return false;
  }
  if (day > 31) {
    return false;
  }
  if (month == 4 || month == 6 || month == 9 || month == 11) {
    if (day > 30) {
      return false;
    }
  }
  if (month == 2) {
    if (day > 29) {
      return false;
    }
  }
  return true;
}