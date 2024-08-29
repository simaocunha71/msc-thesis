  const arr1 = arr.filter(num => num > 0 && num <= 9);
  if (arr1.length === 0) {
    return [];
  }
  const arr2 = arr1.sort((a, b) => a - b);
  const arr3 = arr2.reverse();
  const result = arr3.map(num => {
    const names = [
      "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"
    ];
    return names[num];
  });
  return result;
}



