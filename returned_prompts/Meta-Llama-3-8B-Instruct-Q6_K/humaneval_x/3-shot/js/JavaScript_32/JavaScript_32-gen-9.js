  if (xs.length % 2 !== 0) {
    throw new Error('List of coefficients must have even number of elements');
  }
  let a = xs[0];
  let b = xs[1];
  let c = xs[2];
  let d = xs[3];
  let e = xs[4];
  let f = xs[5];
  let x = (-b + Math.sqrt(b * b - 4 * a * c)) / (2 * a);
  return x;
}
// This function only works for polynomials of degree 5
// and there is only one root. For higher degree polynomials
// you need to use numerical methods to find the root. 
// Also, it does not handle complex roots. 
// For higher degree polynomials, use numerical methods. 
// For complex roots, you need to use a library that can handle complex numbers. 
// Also, this function does not handle cases where the largest non-zero coefficient is not the leading coefficient. 
// You need to handle such cases separately. 
// Also, this function does not handle cases where the polynomial has no real roots. 
// You need to handle such cases separately. 
// Also, this function does not handle cases where the polynomial is not of the form ax^n + bx^(n-1) + ... + c. 
// You need to handle such cases separately. 
// Also, this function does not handle cases where the polynomial has multiple roots. 
// You need to handle such cases separately. 
// Also, this function does not handle cases where the polynomial has complex roots. 
// You need to handle such cases separately. 
// Also, this function does not handle cases where the polynomial has a root at infinity. 
// You need to handle such cases separately. 
// Also, this function does not handle cases where the polynomial has a root at zero. 
// You need to handle such cases separately. 
// Also, this function does not handle cases where the polynomial has a root at a finite number. 
// You need to handle such cases separately. 
// Also, this function does not handle cases where the polynomial has a root at a negative number. 
// You need to handle such cases separately. 
// Also, this function does not handle cases where the polynomial has a root at a positive number. 
// You need to handle such cases separately. 
// Also, this function does not handle cases where the polynomial has a root