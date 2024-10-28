  const map = {
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

  return numbers.split(' ')
    .map((word) => map[word])
    .sort((a, b) => a - b)
    .map((num) => Object.keys(map).find((word) => map[word] === num))
    .join(' ');
}



