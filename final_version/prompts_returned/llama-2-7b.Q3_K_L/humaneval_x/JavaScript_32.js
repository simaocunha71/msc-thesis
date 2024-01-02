/*
  Evaluates polynomial with coefficients xs at point x.
  return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
  */
const poly = (xs, x) => {
  return xs.reduce((prev, item, index) => {
    return prev + item * Math.pow(x, index);
  }, 0);
}

/*
  xs are coefficients of a polynomial.
  findZero find x such that poly(x) = 0.
  findZero returns only only zero point, even if there are many.
  Moreover, findZero only takes list xs having even number of coefficients
  and largest non zero coefficient as it guarantees
  a solution.
  >>> round(findZero([1, 2]), 2) # f(x) = 1 + 2x
  -0.5
  >>> round(findZero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
  1.0
  */
const findZero = (xs) => {
  const {length} = xs;
  if(length % 2 !== 0){
    console.log('error: odd number of points');
    return {};
  }
  let maxPow = Math.pow(Math.max(...xs), length - 1);
  //console.log('maxPower', maxPow);
  //findRoot finds a real solution to the equation f(x) = 0
  const findRoot = (minPow, maxPow, minX, maxX) => {
    while((maxPow - minPow) * (maxX - minX) > 0){
      //console.log('newMaxPower', Math.pow(Math.max(...xs), minPow));
      let newMinPow = minPow + 1;
      if(newMinPow < maxPow) {
        newMinPow++;
      }
      const newMinX = (newMinPow > minX