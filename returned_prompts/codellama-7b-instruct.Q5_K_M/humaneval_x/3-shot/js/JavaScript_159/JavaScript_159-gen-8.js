  var total = number + remaining;
  var eaten = total - remaining;
  var left = 0;

  if (eaten >= need) {
    left = eaten - need;
  }

  return [total, left];
}



