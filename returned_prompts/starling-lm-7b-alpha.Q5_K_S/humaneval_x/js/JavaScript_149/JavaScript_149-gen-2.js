  let result = lst.filter(s => s.length % 2 === 0);
  result.sort((a, b) => (a.length - b.length) || a.localeCompare(b));
  return result;
}



