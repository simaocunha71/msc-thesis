const roundedAvg = (n, m) => {
  if (n > m) return -1;
  const avg = Math.round((n + m) / 2);
  return "0b" + avg.toString(2);
};

/*Test Cases*/
console.log(roundedAvg(1, 5)); // "0b11"
console.log(roundedAvg(7, 5)); // -1
console.log(roundedAvg(10, 20)); // "0b1111"
console.log(roundedAvg(20, 33)); // "0b11010"
console.log(roundedAvg(1, 1)); // "0b1"
console.log(roundedAvg(2, 3)); // "0b10"