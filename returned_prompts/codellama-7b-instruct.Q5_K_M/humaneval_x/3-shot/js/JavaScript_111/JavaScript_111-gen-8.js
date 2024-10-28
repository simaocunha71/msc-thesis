  var hist = {};
  var temp = test.split(" ");
  var max = 0;
  var letters = [];

  for (const t of temp) {
    if (hist[t]) {
      hist[t] += 1;
      if (hist[t] > max) {
        max = hist[t];
      }
    } else {
      hist[t] = 1;
    }
  }

  for (const [key, value] of Object.entries(hist)) {
    if (value == max) {
      letters.push(key);
    }
  }

  return {'letters': letters, 'count': max};
}



