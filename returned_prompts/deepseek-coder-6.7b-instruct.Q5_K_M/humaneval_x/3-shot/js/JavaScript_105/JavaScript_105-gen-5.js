  const words = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"];
  return arr.filter(x => x >= 1 && x <= 9)
        .sort((a, b) => b - a)
        .map(x => words[x]);
}



