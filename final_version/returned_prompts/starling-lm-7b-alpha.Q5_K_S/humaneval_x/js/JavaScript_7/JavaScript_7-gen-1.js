  const result = [];
  for (const s of strings) {
    if (s.includes(substring)) {
      result.push(s);
    }
  }
  return result;
}



