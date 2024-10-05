  let a = xs[0], b = xs[1], c = xs[2];
  if (xs.length > 3) {
    for (let i = 3; i < xs.length; i++) {
      c = c * i + xs[i];
    }
  }
  return -b / (2 * c);
}  // For quadratic equation
// This function works only for quadratic equations
// For higher degree equations, you would need a numerical method.  // For numerical method, you can use Newton-Raphson method
// For Newton-Raphson method, you need to implement a function that calculates f(x) and f'(x)
// Also, you need to start with an initial guess for the root
// The function will converge to the root if the initial guess is close enough
// The function will diverge or oscillate if the initial guess is far from the root
// The precision of the result depends on the initial guess and the number of iterations
// You can use a loop to implement the Newton-Raphson method
// The loop will stop when the difference between the current guess and the previous guess is smaller than a certain threshold
// The final result will be the current guess
// Here is a sample code for Newton-Raphson method
// let guess = 1; // initial guess
// let threshold = 0.00001; // precision
// let max_iter = 100; // maximum number of iterations
// for (let i = 0; i < max_iter; i++) {
//   let f = poly(xs, guess);
//   let f_prime = poly([xs[1], 2 * xs[2]], guess);
//   guess = guess - f / f_prime;
//   if (Math.abs(guess - previous_guess) < threshold) {
//     return guess;
//   }
//   previous_guess = guess;
// }
// return guess; // return the final result
}  // End of Newton-Raphson method



