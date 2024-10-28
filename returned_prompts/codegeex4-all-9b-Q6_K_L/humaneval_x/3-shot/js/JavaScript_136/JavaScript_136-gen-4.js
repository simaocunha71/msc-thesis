  var negative = lst.filter(num => num < 0);
  var positive = lst.filter(num => num > 0);

  if (negative.length == 0) {
    negative = null;
  } else {
    negative = Math.max(...negative);
  }

  if (positive.length == 0) {
    positive = null;
  } else {
    positive = Math.min(...positive);
  }

  return [negative, positive];
}



