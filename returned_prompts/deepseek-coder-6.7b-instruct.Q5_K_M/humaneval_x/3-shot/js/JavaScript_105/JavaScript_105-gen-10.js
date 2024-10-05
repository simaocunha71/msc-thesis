  const names = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"];

  return arr.sort((a, b) => a - b).reverse().map(num => {
    if (num < 1 || num > 9) {
      return;
    }
    return names[num];
  }).filter(Boolean);
}



