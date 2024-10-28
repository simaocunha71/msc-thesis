const flipCase = (string) => {
  const flipped = string.split("").map(char => {
    if (char === char.toLowerCase()) {
      return char.toUpperCase();
    } else {
      return char.toLowerCase();
    }
  }).join("");
  return flipped;
};
