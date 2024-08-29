  const names = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
  const result = []
  for (const n of arr) {
    if (n > 0 && n < 10) {
      result.push(names[n]);
    }
  }
  return result;
}



