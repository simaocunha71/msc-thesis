  let sortedNumbers = arr.filter(num => 1 <= num && num <= 9).sort((a, b) => a - b);
  let reversedNumbers = sortedNumbers.reverse();
  let result = reversedNumbers.map(num => {
    let digitNames = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"];
    return digitNames[num];
  });
  return result;
}