  let result = "";
  let isReversed = false;
  for (const c of s) {
    if (c.match(/[a-z]/i)) {
      if (isReversed) {
        result += c.toUpperCase();
      } else {
        result += c.toLowerCase();
      }
      isReversed = !isReversed;
    } else {
      result += c;
    }
  }
  if (!isReversed) {
    result = result.split('').reverse().join('');
  }
  return result;
}



