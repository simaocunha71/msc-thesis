  const numberToWord = {
    1: 'One',
    2: 'Two',
    3: 'Three',
    4: 'Four',
    5: 'Five',
    6: 'Six',
    7: 'Seven',
    8: 'Eight',
    9: 'Nine'
  };
  const filteredArr = arr.filter(n => n > 0 && n < 10);
  const sortedArr = filteredArr.sort((a, b) => a - b);
  const reversedArr = sortedArr.reverse();
  const wordArr = reversedArr.map(n => numberToWord[n]);
  return wordArr;
}