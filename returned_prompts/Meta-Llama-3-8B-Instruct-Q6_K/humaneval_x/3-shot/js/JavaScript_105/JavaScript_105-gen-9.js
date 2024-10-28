  let result = [];
  let sortedArray = arr.filter(num => num >= 1 && num <= 9).sort((a, b) => a - b).reverse();
  for (const num of sortedArray) {
    result.push(['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine'][num - 1]);
  }
  return result;
}