  const result = [];
  for (let i = a; i <= b; i++) {
    const s = i.toString();
    for (const d of s) {
      if (parseInt(d) % 2 === 0) {
        result.push(parseInt(d));
      }
    }
  }
  return result;
}



