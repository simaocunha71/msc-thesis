  const sorted_map = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
  };

  const numbers_arr = numbers.split(" ").map(n => sorted_map[n]);
  const sorted_numbers_arr = numbers_arr.sort((a,b) => a - b);

  return sorted_numbers_arr.map(n => Object.keys(sorted_map).filter(k => sorted_map[k] === n)[0]).join(" ");
}



