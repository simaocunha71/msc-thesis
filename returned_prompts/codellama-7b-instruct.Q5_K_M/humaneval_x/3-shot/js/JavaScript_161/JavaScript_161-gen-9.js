  let result = '';
  for (const c of s) {
    if (c.match(/[A-Za-z]/)) {
      result += c.toUpperCase() === c ? c.toLowerCase() : c.toUpperCase();
    } else {
      result += c;
    }
  }
  return result;
}



