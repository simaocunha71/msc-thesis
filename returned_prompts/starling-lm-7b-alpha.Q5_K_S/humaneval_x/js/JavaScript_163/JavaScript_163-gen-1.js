  const result = [];
  for (let i = a; i <= b; i++) {
    const str = i.toString();
    for (const d of str) {
      if ((d | 0) % 2 == 0) {
        result.push(d);
      }
    }
  }
  return result.sort();
}



