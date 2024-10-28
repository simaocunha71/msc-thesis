const changeBase = (x, base) => {
  const numBase = base.toString().length;
  if (numBase > 10) return 'Invalid base';
  const digit = '0123456789ABCDEF'.split('');
  const num = x.toString();
  let output = [];
  for (let i = 0; i < num.length; i++) {
    output.push(digit[parseInt(num[i])]);
  }
  return output.join('').toUpperCase();
};
