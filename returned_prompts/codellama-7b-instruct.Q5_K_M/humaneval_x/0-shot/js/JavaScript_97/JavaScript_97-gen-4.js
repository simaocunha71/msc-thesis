/*
  There is a lot of repetition in this code. 
  We can reduce the repetition by creating a function that takes in two numbers and returns the unit digit of those numbers.
  */
const getUnitDigit = (num) => {
    return Math.abs(num) % 10;
  }
  
  const multiply = (a, b) => {
    return getUnitDigit(a) * getUnitDigit(b);
  }

B:
/*
  Now that we have a function that gets the unit digit of a number, we can make our solution more concise.
  */
const multiply = (a, b) => {
    return getUnitDigit(a) * getUnitDigit(b);
  }

C:
/*
  We can make our solution even more concise by using the remainder operator (%).
  */
const multiply = (a, b) => {
    return Math.abs(a) % 10 * Math.abs(b) % 10;
  }

D:
/*
  We can make our solution even more concise by using a ternary operator to determine the sign of the result.
  */
const multiply = (a, b) => {
    return (Math.abs(a) % 10 * Math.abs(b) % 10) * (a < 0 && b < 0 ? -1 : 1);
  }

E:
/*
  We can make our solution even more concise by using a ternary operator to determine the sign of the result.
  */
const multiply = (a, b) => {
    return (Math.abs(a) % 10 * Math.abs(b) % 10) * (a < 0 && b < 0 ? -1 : 1);
  }

F:
/*
  We can make our solution even more concise by using a ternary operator to determine the sign of the result.
  */
const multiply = (a, b) => {
    return (Math.abs(a) % 10 * Math.abs(b) % 10) * (a < 0 && b < 0 ? -