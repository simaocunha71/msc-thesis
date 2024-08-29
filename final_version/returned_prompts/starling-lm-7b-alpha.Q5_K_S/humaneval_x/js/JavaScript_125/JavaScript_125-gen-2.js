  let result = [];
  let count = 0;
  for (const c of txt) {
    if (c == ' ') {
      result.push('');
    } else if (c == ',') {
      result.push(',');
    } else if (c >= 'a' && c <= 'z') {
      if ((c - 'a') % 2 == 1) {
        count += 1;
      }
    }
  }
  if (result.length == 0) {
    return count;
  } else {
    return result;
  }
}



