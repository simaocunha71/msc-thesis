  let map = { 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine' };
  return arr.filter(num => num >= 1 && num <= 9).sort((a, b) => b - a).map(num => map[num]);
}



