  let words = numbers.split(' ');
  let sortedWords = words.sort((a, b) => {
    let num1 = { zero: 0, one: 1, two: 2, three: 3, four: 4, five: 5, six: 6, seven: 7, eight: 8, nine: 9 }[a];
    let num2 = { zero: 0, one: 1, two: 2, three: 3, four: 4, five: 5, six: 6, seven: 7, eight: 8, nine: 9 }[b];
    return num1 - num2;
  });
  return sortedWords.join(' ');
}