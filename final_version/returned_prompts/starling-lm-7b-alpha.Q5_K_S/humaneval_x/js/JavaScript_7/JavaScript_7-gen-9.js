  let result = [];
  for (const s of strings) {
    if (s.indexOf(substring) !== -1) {
      result.push(s);
    }
  }
  return result;
}



