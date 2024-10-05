const triangleArea = (a, b, c) => {

B:
const triangleArea = (a, b, c) => {
  const sum = a + b;
  if (sum > c) {
    const area = Math.sqrt(sum * c);
    return area.toFixed(2);
  }
  return -1;
};

C:
const triangleArea = (a, b, c) => {
  if (a + b > c && b + c > a && a + c > b) {
    const area = Math.sqrt(a * b * c);
    return area.toFixed(2);
  }
  return -1;
};

D:
const triangleArea = (a, b, c) => {
  if (a + b > c && b + c > a && a + c > b) {
    return (a * b * Math.sqrt(1 - (Math.pow(a - b, 2) / (a * b)))) / 2;
  }
  return -1;
};
