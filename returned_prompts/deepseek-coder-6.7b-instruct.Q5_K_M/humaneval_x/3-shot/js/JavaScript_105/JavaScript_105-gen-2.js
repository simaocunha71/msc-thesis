  const names = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"];
  return arr
    .filter(n => n >= 1 && n <= 9)
    .sort((a, b) => b - a)
    .map(n => names[n - 1]);
}



