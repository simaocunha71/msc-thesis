  const numberMap = {
    zero: 0,
    one: 1,
    two: 2,
    three: 3,
    four: 4,
    five: 5,
    six: 6,
    seven: 7,
    eight: 8,
    nine: 9,
  };

  const words = numbers.split(' ');
  const numbersList = words.map((word) => numberMap[word]);

  numbersList.sort((a, b) => a - b);

  return numbersList.map((number) => Object.keys(numberMap).find((word) => numberMap[word] === number)).join(' ');
}



