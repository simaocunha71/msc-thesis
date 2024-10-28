
const evenOddCount = (num) => {
  const numStr = num.toString();
  const evenDigits = numStr.match(/[02468]/g);
  const oddDigits = numStr.match(/[13579]/g);
  return [evenDigits.length, oddDigits.length];
};
