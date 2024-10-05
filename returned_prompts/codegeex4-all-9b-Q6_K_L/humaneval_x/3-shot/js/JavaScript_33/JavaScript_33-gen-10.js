  var l_sorted = l.map((value, index) => [value, index]);
  l_sorted.sort((a, b) => a[0] - b[0]);
  var result = l.map((value, index) => {
    if (index % 3 == 2) {
      return l_sorted[index][0];
    } else {
      return value;
    }
  });
  return result;
}

