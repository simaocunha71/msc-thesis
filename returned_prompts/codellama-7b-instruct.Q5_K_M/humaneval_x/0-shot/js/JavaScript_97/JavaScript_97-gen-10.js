/*
1.1

*/
const multiply = (a, b) => {
  return (a % 10) * (b % 10);
};

/*
1.2

*/
const multiply = (a, b) => {
  return (a % 10) * (b % 10);
};

/*
2.1

*/
const multiply = (a, b) => {
  let unit = a % 10 * b % 10;
  let result = 0;
  while (a > 0 || b > 0) {
    result += a % 10 * b % 10;
    a = Math.floor(a / 10);
    b = Math.floor(b / 10);
  }
  return result;
};

/*
2.2

*/
const multiply = (a, b) => {
  let result = 0;
  while (a > 0 || b > 0) {
    result += a % 10 * b % 10;
    a = Math.floor(a / 10);
    b = Math.floor(b / 10);
  }
  return result;
};

/*
3.1

*/
const multiply = (a, b) => {
  let result = 0;
  while (a > 0 || b > 0) {
    result += a % 10 * b % 10;
    a = Math.floor(a / 10);
    b = Math.floor(b / 10);
  }
  return result;
};

/*
3.2

*/
const multiply = (a, b) => {
  let result = 0;
  while (a > 0 || b > 0) {
    result += a % 10 * b % 10;
    a = Math.floor(a / 10);
    b = Math.floor(b / 10);
  }
  return result;
};

/*
4.1

*/
const multiply = (a, b) => {
 