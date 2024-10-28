  if (xs.length % 2 != 0) {
    throw new Error("List of coefficients must have even number of elements");
  }
  let a = xs[xs.length - 1];
  let b = xs[xs.length - 2];
  let c = xs[xs.length - 3];
  let d = xs[xs.length - 4];
  let x = (-b + Math.sqrt(b * b - 4 * a * c)) / (2 * a);
  return x;
}  // It is important to check if this function is correct or not. This function assumes that the given coefficients are for a cubic polynomial. This function also assumes that the polynomial has a real root. If the polynomial does not have a real root, this function will return a complex number. If the polynomial is not a cubic polynomial, this function will not work correctly. It is also important to note that the function does not check if the given coefficients are a valid cubic polynomial. It is the responsibility of the caller to ensure that the given coefficients are a valid cubic polynomial.