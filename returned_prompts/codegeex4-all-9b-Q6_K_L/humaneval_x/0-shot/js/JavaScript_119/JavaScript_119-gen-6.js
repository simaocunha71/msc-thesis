const matchParens = (lst) => {
  let parens = lst[0] + lst[1];
  let count = 0;
  for (let i = 0; i < parens.length; i++) {
    if (parens[i] === '(') {
      count++;
    } else if (parens[i] === ')') {
      count--;
    }
    if (count < 0) {
      return 'No';
    }
  }
  return count === 0 ? 'Yes' : 'No';
};