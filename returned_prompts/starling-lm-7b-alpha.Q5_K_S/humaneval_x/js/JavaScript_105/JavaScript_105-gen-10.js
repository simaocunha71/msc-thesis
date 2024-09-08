  const arr2 = arr.filter((x) => {
    return x >= 1 && x <= 9;
  });

  if (arr2.length === 0) {
    return [];
  }

  const arr3 = arr2.sort((a, b) => {
    return a - b;
  });

  const arr4 = arr3.reverse();

  return arr4.map((x) => {
    const arr5 = [
      "One",
      "Two",
      "Three",
      "Four",
      "Five",
      "Six",
      "Seven",
      "Eight",
      "Nine"
    ];
    return arr5[x];
  });
};



