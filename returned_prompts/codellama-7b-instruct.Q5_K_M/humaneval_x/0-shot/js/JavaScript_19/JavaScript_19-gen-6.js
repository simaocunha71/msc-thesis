  let numberArray = numbers.split(" ").map(number => parseInt(number));
  return numberArray.sort((a, b) => a - b).join(" ");
}

