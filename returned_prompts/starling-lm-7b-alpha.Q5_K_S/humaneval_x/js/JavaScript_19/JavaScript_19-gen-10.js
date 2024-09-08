  const numToIndex = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
  };

  return numbers
    .split(" ")
    .map(num => numToIndex[num])
    .sort((a, b) => a - b)
    .map(index => Object.keys(numToIndex).find(key => numToIndex[key] === index))
    .join(" ");
}



