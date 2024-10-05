  var sortedThird = [...l];
  var third = sortedThird.filter((item, index) => index % 3 === 2);
  third.sort((a, b) => a - b);
  for (var i = 0; i < sortedThird.length; i++) {
    if (i % 3 === 2) {
      sortedThird[i] = third.shift();
    }
  }
  return sortedThird;
}