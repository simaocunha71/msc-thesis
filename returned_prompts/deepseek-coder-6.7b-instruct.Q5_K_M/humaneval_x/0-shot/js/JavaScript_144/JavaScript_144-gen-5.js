  let num1 = Number(x.split("/")[0]);
  let den1 = Number(x.split("/")[1]);
  let num2 = Number(n.split("/")[0]);
  let den2 = Number(n.split("/")[1]);

  let num = num1 * num2;
  let den = den1 * den2;

  return num % den === 0;
}

// Test cases:
console.log(simplify("1/5", "5/1")); // true
console.log(simplify("1/6", "2/1")); // false
console.log(simplify("7/10", "10/2")); // false

// This function works by first splitting the input strings into their numerator and denominator parts.
// Then, it multiplies the numerators together and the denominators together.
// Finally, it checks if the new numerator is divisible by the new denominator (i.e., if the fraction is a whole number).
// If the new numerator is divisible by the new denominator, it returns true. Otherwise, it returns false.
// This is done using the modulus operator (%), which returns the remainder of division. If the remainder is 0, the division is exact, so the fraction is a whole number.
// This function assumes that the input fractions are valid, and do not have zero as the denominator.
// If this is not the case, the function may not work correctly.

// This function works with the assumption that the input fractions are valid, and do not have zero as the denominator.
// If this is not the case, the function may not work correctly.

// This function works by first splitting the input strings into their numerator and denominator parts.
// Then, it multiplies the numerators together and the denominators together.
// Finally, it checks if the new numerator is divisible by the new denominator (i.e., if the fraction is a whole number).
// If the new numerator is divisible by the new denominator, it returns true. Otherwise, it returns false.
// This is done using the modulus operator (%), which returns the remainder of division. If the remainder is 0, the division is exact,