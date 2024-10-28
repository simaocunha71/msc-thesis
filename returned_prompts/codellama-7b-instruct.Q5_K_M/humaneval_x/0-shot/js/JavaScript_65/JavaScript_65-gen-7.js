const circularShift = (x, shift) => {
  if (shift > String(x).length) return String(x).split("").reverse().join("");
  return String(x).substr(shift) + String(x).substr(0, shift);
}
