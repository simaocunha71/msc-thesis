  let result = [];
  lst.forEach(s => {
    if (s.length % 2 === 0) {
      result.push(s);
    }
  });
  result.sort((a, b) => {
    if (a.length === b.length) {
      return a.localeCompare(b);
    }
    return a.length - b.length;
  });
  return result;
}



