  let result = 0;
  for (let i = 0; i < string.length; i++) {
    if (string.slice(i, i + substring.length) === substring) {
      result += 1;
    }
  }
  return result;
}



