  if (n > m) {
    return -1;
  } else {
    var sum = 0;
    for (var i = n; i <= m; i++) {
      sum += i;
    }
    var average = sum / (m - n + 1);
    var rounded = Math.round(average);
    return rounded.toString(2);
  }
}



