  if (n > m) {
    return -1;
  }
  let avg = Math.round((n + m) / 2);
  let result = avg.toString(2);
  while (result.length < 8) {
    result = '0' + result;
  }
  return '0b' + result;
}



