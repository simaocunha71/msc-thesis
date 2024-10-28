  if (n > m) {
    return -1;
  } else {
    var sum = 0;
    for (var i = n; i <= m; i++) {
      sum += i;
    }
    var avg = sum / (m - n + 1);
    return avg.toString(2);
  }
}



