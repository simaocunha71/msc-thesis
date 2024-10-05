  const digitMap = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
  };
  const filtered = arr.filter((x) => x >= 1 && x <= 9);
  const sorted = filtered.sort((a, b) => a - b);
  const reversed = sorted.reverse();
  const result = reversed.map((x) => digitMap[x.toString()]);
  return result;
}

