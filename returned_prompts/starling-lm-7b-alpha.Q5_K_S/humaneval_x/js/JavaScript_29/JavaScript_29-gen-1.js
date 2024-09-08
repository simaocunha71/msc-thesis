  const result = [];
  for (const s of strings) {
    if (s.startsWith(prefix)) {
      result.push(s);
    }
  }
  return result;
}



