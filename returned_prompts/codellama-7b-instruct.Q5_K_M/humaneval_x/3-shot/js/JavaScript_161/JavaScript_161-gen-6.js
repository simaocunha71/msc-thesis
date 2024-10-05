  const lower = 'a';
  const upper = 'A';
  const result = [];

  for (const c of s) {
    if (c.match(/[a-zA-Z]/)) {
      if (c.match(/[a-z]/)) {
        result.push(c.toUpperCase());
      } else {
        result.push(c.toLowerCase());
      }
    } else {
      result.push(c);
    }
  }

  return result.join('');
}



