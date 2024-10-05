  let [numX, denX] = x.split('/').map(Number);
  let [numN, denN] = n.split('/').map(Number);
  let num = numX * numN;
  let den = denX * denN;
  return num % den === 0;
};

console.log(simplify("1/5", "5/1")); // true
console.log(simplify("1/6", "2/1")); // false
console.log(simplify("7/10", "10/2")); // false

// This function first splits each fraction into the numerator and denominator parts. It then multiplies each of these parts by the respective parts of the other fraction. If the numerator of the resulting fraction is divisible by the denominator, the function returns true; otherwise, it returns false.

// In JavaScript, the % operator gives the remainder of a division operation. If num % den is 0, that means num is divisible by den, so the function returns true. Otherwise, it returns false.

// The function uses the map function to convert the numerator and denominator parts of each fraction from strings to numbers. The split function is used to split each fraction into its numerator and denominator parts.

// The function uses an arrow function to define simplify.

// The function uses the remainder operator (%) to check if the numerator of the result is divisible by the denominator. If the result is 0, it means that the fraction is a whole number and the function returns true. Otherwise, it returns false.

// The function uses the map function to convert the numerator and denominator parts of each fraction from strings to numbers. The split function is used to split each fraction into its numerator and denominator parts.

// The function uses an arrow function to define simplify.

// The function uses the remainder operator (%) to check if the numerator of the result is divisible by the denominator. If the result is 0, it means that the fraction is a whole number and the function returns true. Otherwise, it returns false.

// The function uses the map function to convert the numerator and denominator parts of each fraction from strings to numbers. The split function is used to split each fraction into its numerator and denominator