const decimalToBinary = (decimal) => {
  return 'db' + (decimal >>> 0).toString(2) + 'db';
};

