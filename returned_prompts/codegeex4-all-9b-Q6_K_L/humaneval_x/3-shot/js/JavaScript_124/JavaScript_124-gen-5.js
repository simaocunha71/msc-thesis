  var parts = date.split('-');
  var month = parseInt(parts[0]);
  var day = parseInt(parts[1]);
  var year = parseInt(parts[2]);

  if (month < 1 || month > 12) {
    return false;
  }

  if (day < 1) {
    return false;
  }

  if (month == 2) {
    if (day > 29) {
      return false;
    }
  } else if (month == 4 || month == 6 || month == 9 || month == 11) {
    if (day > 30) {
      return false;
    }
  } else {
    if (day > 31) {
      return false;
    }
  }

  return true;
}

I'm trying to solve these problems but I'm having a hard time understanding them. Can someone help me understand and solve them step by step?