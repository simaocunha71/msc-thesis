  let oneToNine = [
    { number: 1, name: "One" },
    { number: 2, name: "Two" },
    { number: 3, name: "Three" },
    { number: 4, name: "Four" },
    { number: 5, name: "Five" },
    { number: 6, name: "Six" },
    { number: 7, name: "Seven" },
    { number: 8, name: "Eight" },
    { number: 9, name: "Nine" },
  ];

  let result = arr
    .filter((n) => n > 0 && n <= 9)
    .sort()
    .reverse()
    .map((n) => oneToNine.find((oneToNine) => oneToNine.number == n).name);

  return result;
}