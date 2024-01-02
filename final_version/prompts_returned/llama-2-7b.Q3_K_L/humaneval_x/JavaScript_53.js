/*Add two numbers x and y
  >>> add(2, 3)
  5
  >>> add(5, 7)
  12
  */
const add = (x, y) => {
  return Number(x) + Number(y);
};

/*Subtract two numbers x and y

  >>> sub(4, 1)
  3
  >>> sub(-5, -7)
  2
 */
const sub = (x, y) => {
  return Number(x) - Number(y);
};

/*Multiply two numbers x and y
>>> mul(8, 4)
32
>>> mul(-10, -5)
50
 */
const mul = (x, y) => {
  return Number(x) * Number(y);
};

/*Divide two number x and y
>>> div(16, 4)
4
>>> div(38, -2)
19
*/
const div = (x, y) => {
  return Number(x) / Number(y);
}

/*Return the modulus of two number x and y
>>> mod(6, 3)
3
>>> mod(-5, -2)
-1
*/
const mod = (x, y) => {
  return Math.floor((Number(x) % Number(y)));
}

/*Return the remainder of two number x and y
>>> rem(64, 3)
16
>>> rem(-20, -5)
-3
*/
const rem = (x, y) => {
  return Number(Number(x) % Number(y));
}

/*Add the two numbers x and y.
>>> sum(8, 4)
12
>>> sum(-10,-5)
-3
*/
const sum = (x, y) => {
  return Number(Number(x) + Number(y));
}
/*Add the two numbers x and y.
>>> avg(8, 4)
5
>>> avg(-10,-5)
-2
*/
const avg = (x, y) => {