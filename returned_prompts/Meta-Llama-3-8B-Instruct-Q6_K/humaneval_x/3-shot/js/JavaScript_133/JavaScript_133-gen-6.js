  return Math.ceil(lst.map(x => x).reduce((a, b) => a + b, 0)) ** 2;
}  //or
const sumSquares = (lst) => {
  return Math.ceil(lst.map(Math.ceil).reduce((a, b) => a + b, 0)) ** 2;
}  //or
const sumSquares = (lst) => {
  return Math.ceil(lst.reduce((a, b) => a + Math.ceil(b), 0)) ** 2;
}  //or
const sumSquares = (lst) => {
  return Math.pow(Math.ceil(lst.reduce((a, b) => a + b, 0)), 2);
}  //or
const sumSquares = (lst) => {
  return Math.pow(lst.map(Math.ceil).reduce((a, b) => a + b, 0), 2);
}  //or
const sumSquares = (lst) => {
  return Math.pow(lst.reduce((a, b) => Math.ceil(a + b), 0), 2);
}  //or
const sumSquares = (lst) => {
  let sum = 0;
  for (let i of lst) {
    sum += Math.ceil(i) ** 2;
  }
  return sum;
}  //or
const sumSquares = (lst) => {
  let sum = 0;
  for (let i of lst) {
    sum += Math.ceil(i);
  }
  return sum ** 2;
}  //or
const sumSquares = (lst) => {
  return lst.map(x => x).reduce((a, b) => a + Math.ceil(b) ** 2, 0);
}  //or
const sumSquares = (lst) => {
  return lst.map(x => Math.ceil(x)).reduce((a, b) => a + b ** 2, 0);
}  //or
const sumSquares = (lst) => {
  return lst.reduce((a, b) => a + Math.ceil(b) ** 2, 0);
}  //or
const sumSquares = (lst) => {
  return lst.reduce((a, b) => a + b ** 2, 0).toFixed().replace(/\D+/g, '').replace(/^0+/, '');
}  //or
const sumSquares = (lst) => {
