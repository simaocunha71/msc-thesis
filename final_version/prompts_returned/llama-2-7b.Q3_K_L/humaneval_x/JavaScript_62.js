/* xs represent coefficients of a polynomial.
  xs[0] + xs[1] * x + xs[2] * x^2 + ....
   Return derivative of this polynomial in the same form.
  >>> derivative([3, 1, 2, 4, 5])
  [1, 4, 12, 20]
  >>> derivative([1, 2, 3])
  [2, 6]
  */
const derivative = (xs) => {
  let xs2 = [];
  for (let i in xs) xs2.push(xs[i]);
  return derivative2(xs2);
}
// function to calculate a polynomial's derivative
function derivative2(xs2) {
  // initialize the first derivative at x=1,
  let xs21 = xs2;

  // initialize the second derivative at x=0,
  let xs22 = [];
  for (let i in xs21) xs22.push(xs21[i]/Math.pow(x, 2));

  // recursive function to calculate higher derivatives
  let fd;
  if (xs22[0] === undefined || xs22[0] === null) {
    fd = xs22[0];
  } else {
    for (let i in xs2) {
      const xi = Math.pow(x, i);
      let fxi = 0;
      for (let j in xs2) {
        fxi += ((xs2[j]/Math.pow(x, j))/Math.pow(xi, j)); // jth derivatives term of polynomial
      }
      if (i !== 1) fd[i - 2] = fxi;
      else fd[0] = fxi;
    }
  }
  return fd;
}
// x^0 is the derivative of zero, which is just 0.
let fD = [0];
for (let i in xs) { // for each value of x
  if (i !== 0) {
    const xi = Math.pow(x, i);
    let fxi = 0;
    for (let j in xs[0])